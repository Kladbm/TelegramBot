import json
import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

with open('config.json') as file:
    token = json.load(file)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

    await context.bot.send_message(chat_id=update.effective_chat.id, text="It's /start command",
                                   reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("It's /help command")


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    update_message_text = update.message.text

    default_parameter = [
        InlineKeyboardButton("Ок", callback_data="1"),
        InlineKeyboardButton("Заново", callback_data="1"),
        InlineKeyboardButton("Закрыть", callback_data="1")
    ]

    if update_message_text == "Роковая башня":
        keyboard = [
            [
                InlineKeyboardButton("Легкая", callback_data="1"),
                InlineKeyboardButton("Сложная", callback_data="1")
            ],
            default_parameter
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Роковая башня", reply_markup=reply_markup)
        return

    if update_message_text == "Клан босс":
        keyboard = [
            [
                InlineKeyboardButton("4 КБ", callback_data="1"),
                InlineKeyboardButton("5 КБ", callback_data="1"),
                InlineKeyboardButton("6 КБ", callback_data="1")
            ],
            default_parameter
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Клан босс", reply_markup=reply_markup)
        return

    if update_message_text == "Арена":
        keyboard = [
            [
                InlineKeyboardButton("Обычная", callback_data="1"),
                InlineKeyboardButton("Групповая", callback_data="1")
            ],
            default_parameter
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Арена", reply_markup=reply_markup)
        return

    if update_message_text == "События / Турниры":
        keyboard = [
            [
                InlineKeyboardButton("События", callback_data="1"),
                InlineKeyboardButton("Турниры", callback_data="1")
            ],
            default_parameter
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("События / Турниры", reply_markup=reply_markup)
        return

    if update_message_text == "Клан":
        keyboard = [
            [
                InlineKeyboardButton("Турнир кланов", callback_data="1")
            ],
            [
                InlineKeyboardButton("Сундук", callback_data="1"),
                InlineKeyboardButton("Магазин", callback_data="1")
            ],
            default_parameter
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Клан", reply_markup=reply_markup)
        return

    if update_message_text == "Другое":
        keyboard = [
            [
                InlineKeyboardButton("Подземка", callback_data="1"),
                InlineKeyboardButton("Рынок", callback_data="1")
            ],
            [
                InlineKeyboardButton("Вход", callback_data="1"),
                InlineKeyboardButton("Миссии", callback_data="1")
            ],
            [
                InlineKeyboardButton("Задания", callback_data="1"),
                InlineKeyboardButton("Магазин", callback_data="1")
            ],
            default_parameter
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Другое", reply_markup=reply_markup)
        return

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Неизвестная команда")


if __name__ == '__main__':
    application = ApplicationBuilder().token(token['bot.token']).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), message)
    application.add_handler(message_handler)

    application.run_polling()
