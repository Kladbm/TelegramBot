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

ANCIENT, VOID, SACRED = "💙 Древний", "💜 Темный", "💛 Сакрал"
CLOSED, RETURN = "❌ Закрыть", "↩ Вернуться"

close_keyboard_button = InlineKeyboardButton(text=CLOSED, callback_data="close")


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
            KeyboardButton("Другие активности")
        ]
    ]
    await message.reply("It's /start command", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))


@dispatcher.message_handler(commands='help')
async def help(message: types.Message) -> None:
    await message.reply("It's /help command")


@dispatcher.message_handler(content_types=types.ContentTypes.TEXT)
async def messages(message: types.Message):
    if message.text == "Роковая башня":
        keyboard = InlineKeyboardMarkup(row_width=2) \
            .add(InlineKeyboardButton(text="Легкая", callback_data="doom_tower_easy"),
                 InlineKeyboardButton(text="Сложная", callback_data="doom_tower_hard")).row(close_keyboard_button)
        await message.answer("Роковая башня", reply_markup=keyboard)

    if message.text == "Клан босс":
        keyboard = InlineKeyboardMarkup(row_width=3) \
            .add(InlineKeyboardButton(text="4 КБ", callback_data="clan_boss_4CB"),
                 InlineKeyboardButton(text="5 КБ", callback_data="clan_boss_5CB"),
                 InlineKeyboardButton(text="6 КБ", callback_data="clan_boss_6CB")).row(close_keyboard_button)
        await message.answer("Клан босс", reply_markup=keyboard)

    if message.text == "Арена":
        keyboard = InlineKeyboardMarkup(row_width=2) \
            .add(InlineKeyboardButton(text="Обычная", callback_data="arena_normal"),
                 InlineKeyboardButton(text="Групповая", callback_data="arena_group")).row(close_keyboard_button)
        await message.answer("Арена", reply_markup=keyboard)

    if message.text == "События / Турниры":
        keyboard = InlineKeyboardMarkup(row_width=2) \
            .add(InlineKeyboardButton(text="События", callback_data="events"),
                 InlineKeyboardButton(text="Турниры", callback_data="tournaments")).row(close_keyboard_button)
        await message.answer("События / Турниры", reply_markup=keyboard)

    if message.text == "Клан":
        keyboard = InlineKeyboardMarkup(row_width=2) \
            .add(InlineKeyboardButton(text="Сундук", callback_data="clan_chest"),
                 InlineKeyboardButton(text="Магазин", callback_data="clan_shop"),
                 InlineKeyboardButton(text="Турнир кланов", callback_data="clan_wars")).row(close_keyboard_button)
        await message.answer("Клан", reply_markup=keyboard)

    if message.text == "Другие активности":
        keyboard = InlineKeyboardMarkup(row_width=2) \
            .add(InlineKeyboardButton(text="Подземка", callback_data="other_dungeons"),
                 InlineKeyboardButton(text="Рынок", callback_data="other_bazaar"),
                 InlineKeyboardButton(text="Вход", callback_data="other_input"),
                 InlineKeyboardButton(text="Миссии", callback_data="other_missions"),
                 InlineKeyboardButton(text="Задания", callback_data="other_tasks"),
                 InlineKeyboardButton(text="Магазин", callback_data="other_shop")).row(close_keyboard_button)
        await message.answer("Другие активности", reply_markup=keyboard)


@dispatcher.callback_query_handler(text="close")
async def close_call(callback: types.CallbackQuery):
    await callback.message.edit_text("До встречи")
    await callback.answer()


@dispatcher.callback_query_handler(text="doom_tower_easy")
async def doom_tower_easy_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="doom_tower_return"), close_keyboard_button)
    await callback.message.edit_text("Легкая", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="doom_tower_hard")
async def doom_tower_hard_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void"),
             InlineKeyboardButton(text=SACRED, callback_data="sacred")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="doom_tower_return"), close_keyboard_button)
    await callback.message.edit_text("Сложная", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="doom_tower_return")
async def doom_tower_return_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text="Легкая", callback_data="doom_tower_easy"),
             InlineKeyboardButton(text="Сложная", callback_data="doom_tower_hard")).row(close_keyboard_button)
    await callback.message.edit_text("Роковая башня", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="clan_boss_4CB")
async def clan_boss_4CB_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="clan_boss_return"), close_keyboard_button)
    await callback.message.edit_text("4 Клан босс", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="clan_boss_5CB")
async def clan_boss_5CB_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void"),
             InlineKeyboardButton(text=SACRED, callback_data="sacred")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="clan_boss_return"), close_keyboard_button)
    await callback.message.edit_text("5 Клан босс", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="clan_boss_6CB")
async def clan_boss_6CB_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void"),
             InlineKeyboardButton(text=SACRED, callback_data="sacred")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="clan_boss_return"), close_keyboard_button)
    await callback.message.edit_text("6 Клан босс", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="clan_boss_return")
async def clan_boss_return_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3) \
        .add(InlineKeyboardButton(text="4 КБ", callback_data="clan_boss_4CB"),
             InlineKeyboardButton(text="5 КБ", callback_data="clan_boss_5CB"),
             InlineKeyboardButton(text="6 КБ", callback_data="clan_boss_6CB")).row(close_keyboard_button)
    await callback.message.edit_text("Клан босс", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="arena_normal")
async def arena_normal_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void"),
             InlineKeyboardButton(text=SACRED, callback_data="sacred")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="arena_return"), close_keyboard_button)
    await callback.message.edit_text("Обычная арена", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="arena_group")
async def arena_group_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void"),
             InlineKeyboardButton(text=SACRED, callback_data="sacred")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="arena_return"), close_keyboard_button)
    await callback.message.edit_text("Групповая арена", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="arena_return")
async def arena_return_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text="Обычная", callback_data="arena_normal"),
             InlineKeyboardButton(text="Групповая", callback_data="arena_group")).row(close_keyboard_button)
    await callback.message.edit_text("Арена", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="events")
async def events_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void"),
             InlineKeyboardButton(text=SACRED, callback_data="sacred")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="events_return"), close_keyboard_button)
    await callback.message.edit_text("События", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="tournaments")
async def tournaments_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void"),
             InlineKeyboardButton(text=SACRED, callback_data="sacred")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="tournaments_return"), close_keyboard_button)
    await callback.message.edit_text("Турниры", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text=["events_return", "tournaments_return"])
async def events_tournaments_return_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text="События", callback_data="events"),
             InlineKeyboardButton(text="Турниры", callback_data="tournaments")).row(close_keyboard_button)
    await callback.message.edit_text("События / Турниры", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="clan_wars")
async def clan_wars_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void"),
             InlineKeyboardButton(text=SACRED, callback_data="sacred")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="clan_return"), close_keyboard_button)
    await callback.message.edit_text("Клановые войны", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="clan_chest")
async def clan_chest_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=1) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="clan_return"), close_keyboard_button)
    await callback.message.edit_text("Клановый сундук", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="clan_shop")
async def clan_shop_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=1) \
        .add(InlineKeyboardButton(text=VOID, callback_data="void")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="clan_return"), close_keyboard_button)
    await callback.message.edit_text("Клановый магазин", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="clan_return")
async def clan_return_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text="Сундук", callback_data="clan_chest"),
             InlineKeyboardButton(text="Магазин", callback_data="clan_shop"),
             InlineKeyboardButton(text="Турнир кланов", callback_data="clan_wars")).row(close_keyboard_button)
    await callback.message.edit_text("Клан", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="other_dungeons")
async def other_dungeons_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=1) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="other_return"), close_keyboard_button)
    await callback.message.edit_text("Подземка", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="other_bazaar")
async def other_bazaar_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=1) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="other_return"), close_keyboard_button)
    await callback.message.edit_text("Базар", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="other_input")
async def other_input_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="other_return"), close_keyboard_button)
    await callback.message.edit_text("Вход", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="other_missions")
async def other_missions_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="other_return"), close_keyboard_button)
    await callback.message.edit_text("Миссии", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="other_tasks")
async def other_tasks_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=1) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient"),
             InlineKeyboardButton(text=VOID, callback_data="void"),
             InlineKeyboardButton(text=SACRED, callback_data="sacred")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="other_return"), close_keyboard_button)
    await callback.message.edit_text("Задания", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="other_shop")
async def other_shop_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=1) \
        .add(InlineKeyboardButton(text=ANCIENT, callback_data="ancient")) \
        .row(InlineKeyboardButton(text=RETURN, callback_data="other_return"), close_keyboard_button)
    await callback.message.edit_text("Магазин", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="other_return")
async def other_return_call(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2) \
        .add(InlineKeyboardButton(text="Подземка", callback_data="other_dungeons"),
             InlineKeyboardButton(text="Рынок", callback_data="other_bazaar"),
             InlineKeyboardButton(text="Вход", callback_data="other_input"),
             InlineKeyboardButton(text="Миссии", callback_data="other_missions"),
             InlineKeyboardButton(text="Задания", callback_data="other_tasks"),
             InlineKeyboardButton(text="Магазин", callback_data="other_shop")).row(close_keyboard_button)
    await callback.message.edit_text("Другие активности", reply_markup=keyboard)
    await callback.answer()


@dispatcher.callback_query_handler(text="ancient")
async def ancient_call(callback: types.CallbackQuery):
    await callback.message.edit_text(f"Добавлен {ANCIENT.lower()} осколок в ")
    await callback.answer()


@dispatcher.callback_query_handler(text="void")
async def ancient_call(callback: types.CallbackQuery):
    await callback.message.edit_text(f"Добавлен {VOID.lower()} осколок в ")
    await callback.answer()


@dispatcher.callback_query_handler(text="sacred")
async def ancient_call(callback: types.CallbackQuery):
    await callback.message.edit_text(f"Добавлен {SACRED.lower()} осколок в ")
    await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
