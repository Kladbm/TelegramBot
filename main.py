import logging
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Get API_TOKEN
with open('config.json') as file:
    token = json.load(file)
API_TOKEN = token['bot.token']

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)

DOOM_TOWER, CLAN_BOSS, ARENA, EVENTS_TOURNAMENTS, CLAN, OTHER = range(6)


@dispatcher.message_handler(commands='start')
async def start_handler(message: types.Message) -> None:
    buttons = [
        [
            KeyboardButton("Роковая башня"),
            KeyboardButton("Клан босс")
        ],
        [
            KeyboardButton("Арена"),
            KeyboardButton("События / Турниры")
        ],
        [
            KeyboardButton("Клан"),
            KeyboardButton("Другое")
        ]
    ]
    await message.reply("It's /start command", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))


@dispatcher.message_handler(commands='help')
async def help(message: types.Message) -> None:
    await message.reply("It's /help command")


@dispatcher.message_handler(content_types=types.ContentTypes.TEXT)
async def mess(message: types.Message):
    if message.text == "Роковая башня":
        keyboard = InlineKeyboardMarkup(row_width=2)\
            .add(InlineKeyboardButton(text="Легкая", callback_data="doom_tower_easy"),
                 InlineKeyboardButton(text="Сложная", callback_data="doom_tower_hard"))\
            .row(InlineKeyboardButton(text="Закрыть", callback_data="close"))
        await message.answer("Роковая башня", reply_markup=keyboard)

    if message.text == "Клан босс":
        keyboard = InlineKeyboardMarkup(row_width=3)\
            .add(InlineKeyboardButton(text="4 КБ", callback_data="clan_boss_4CB"),
                 InlineKeyboardButton(text="5 КБ", callback_data="clan_boss_5CB"),
                 InlineKeyboardButton(text="6 КБ", callback_data="clan_boss_6CB"))\
            .row(InlineKeyboardButton(text="Закрыть", callback_data="close"))
        await message.answer("Клан босс", reply_markup=keyboard)

    if message.text == "Арена":
        keyboard = InlineKeyboardMarkup(row_width=2)\
            .add(InlineKeyboardButton(text="Обычная", callback_data="arena_normal"),
                 InlineKeyboardButton(text="Групповая", callback_data="arena_group"))\
            .row(InlineKeyboardButton(text="Закрыть", callback_data="close"))
        await message.answer("Арена", reply_markup=keyboard)

    if message.text == "События / Турниры":
        keyboard = InlineKeyboardMarkup(row_width=2)\
            .add(InlineKeyboardButton(text="События", callback_data="events"),
                 InlineKeyboardButton(text="Турниры", callback_data="tournaments"))\
            .row(InlineKeyboardButton(text="Закрыть", callback_data="close"))
        await message.answer("События / Турниры", reply_markup=keyboard)

    if message.text == "Клан":
        keyboard = InlineKeyboardMarkup(row_width=2)\
            .add(InlineKeyboardButton(text="Турнир кланов", callback_data="clan_wars"),
                 InlineKeyboardButton(text="Сундук", callback_data="clan_chest"),
                 InlineKeyboardButton(text="Магазин", callback_data="clan_shop"))\
            .row(InlineKeyboardButton(text="Закрыть", callback_data="close"))
        await message.answer("Клан", reply_markup=keyboard)

    if message.text == "Другое":
        keyboard = InlineKeyboardMarkup(row_width=2)\
            .add(InlineKeyboardButton(text="Подземка", callback_data="1"),
                 InlineKeyboardButton(text="Рынок", callback_data="2"),
                 InlineKeyboardButton(text="Вход", callback_data="3"),
                 InlineKeyboardButton(text="Миссии", callback_data="4"),
                 InlineKeyboardButton(text="Задания", callback_data="5"),
                 InlineKeyboardButton(text="Магазин", callback_data="6"))\
            .row(InlineKeyboardButton(text="Закрыть", callback_data="close"))
        await message.answer("Другое", reply_markup=keyboard)


@dispatcher.callback_query_handler(text="close")
async def close_call(callback: types.CallbackQuery):
    await callback.message.edit_text("До встречи")
    await callback.answer()


@dispatcher.callback_query_handler(text="doom_tower_easy")
async def doom_tower_easy_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text="Синий", callback_data="doom_tower_hard_ancient"),
             InlineKeyboardButton(text="Войд", callback_data="doom_tower_hard_void")) \
        .row(InlineKeyboardButton(text="Закрыть", callback_data="close"))
    await callback.message.edit_text("Легкая", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="doom_tower_hard")
async def doom_tower_hard_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text="Синий", callback_data="doom_tower_hard_ancient"),
             InlineKeyboardButton(text="Войд", callback_data="doom_tower_hard_void"),
             InlineKeyboardButton(text="Сакрал", callback_data="doom_tower_hard_sacred")) \
        .row(InlineKeyboardButton(text="Закрыть", callback_data="close"))
    await callback.message.edit_text("Сложная", reply_markup=keyboard)
    await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
