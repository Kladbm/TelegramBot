import json
import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, ConversationHandler, \
    CallbackQueryHandler

DOOM_TOWER, CLAN_BOSS, ARENA, EVENTS_TOURNAMENTS, CLAN, OTHER = range(6)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

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


async def message_doom_tower(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == "Роковая башня":
        keyboard = [
            [
                InlineKeyboardButton("Легкая", callback_data=1),
                InlineKeyboardButton("Сложная", callback_data=1)
            ],
            [
                InlineKeyboardButton("Закрыть", callback_data=1)
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Роковая башня", reply_markup=reply_markup)
        return DOOM_TOWER


async def message_clan_boss(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == "Клан босс":
        keyboard = [
            [
                InlineKeyboardButton("4 КБ", callback_data=1),
                InlineKeyboardButton("5 КБ", callback_data=1),
                InlineKeyboardButton("6 КБ", callback_data=1)
            ],
            [
                InlineKeyboardButton("Закрыть", callback_data=1)
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Клан босс", reply_markup=reply_markup)
        return CLAN_BOSS


async def message_arena(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == "Арена":
        keyboard = [
            [
                InlineKeyboardButton("Обычная", callback_data=1),
                InlineKeyboardButton("Групповая", callback_data=1)
            ],
            [
                InlineKeyboardButton("Закрыть", callback_data=1)
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Арена", reply_markup=reply_markup)
        return ARENA


async def message_events_tournaments(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == "События / Турниры":
        keyboard = [
            [
                InlineKeyboardButton("События", callback_data=1),
                InlineKeyboardButton("Турниры", callback_data=1)
            ],
            [
                InlineKeyboardButton("Закрыть", callback_data=1)
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("События / Турниры", reply_markup=reply_markup)
        return EVENTS_TOURNAMENTS


async def message_clan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == "Клан":
        keyboard = [
            [
                InlineKeyboardButton("Турнир кланов", callback_data=1)
            ],
            [
                InlineKeyboardButton("Сундук", callback_data=1),
                InlineKeyboardButton("Магазин", callback_data=1)
            ],
            [
                InlineKeyboardButton("Закрыть", callback_data=1)
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Клан", reply_markup=reply_markup)
        return CLAN


async def message_other(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == "Другое":
        keyboard = [
            [
                InlineKeyboardButton("Подземка", callback_data=1),
                InlineKeyboardButton("Рынок", callback_data=1)
            ],
            [
                InlineKeyboardButton("Вход", callback_data=1),
                InlineKeyboardButton("Миссии", callback_data=1)
            ],
            [
                InlineKeyboardButton("Задания", callback_data=1),
                InlineKeyboardButton("Магазин", callback_data=1)
            ],
            [
                InlineKeyboardButton("Закрыть", callback_data=1)
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Другое", reply_markup=reply_markup)
        return OTHER


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="До встречи")
    return ConversationHandler.END


if __name__ == '__main__':
    application = ApplicationBuilder().token(token['bot.token']).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    # message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), message)
    # application.add_handler(message_handler)

    conversation_handler = ConversationHandler(
        entry_points=[
            MessageHandler(filters.TEXT & (~filters.COMMAND), message_clan_boss),
            MessageHandler(filters.TEXT & (~filters.COMMAND), message_doom_tower),
            MessageHandler(filters.TEXT & (~filters.COMMAND), message_arena),
            MessageHandler(filters.TEXT & (~filters.COMMAND), message_events_tournaments),
            MessageHandler(filters.TEXT & (~filters.COMMAND), message_clan),
            MessageHandler(filters.TEXT & (~filters.COMMAND), message_other)
        ],
        states={
            DOOM_TOWER: [
                CallbackQueryHandler(end, pattern="^" + "1" + "$")
            ],
            CLAN_BOSS: [
                CallbackQueryHandler(end, pattern="^" + "1" + "$")
            ],
            ARENA: [
                CallbackQueryHandler(end, pattern="^" + "1" + "$")
            ],
            EVENTS_TOURNAMENTS: [
                CallbackQueryHandler(end, pattern="^" + "1" + "$")
            ],
            CLAN: [
                CallbackQueryHandler(end, pattern="^" + "1" + "$")
            ],
            OTHER: [
                CallbackQueryHandler(end, pattern="^" + "1" + "$")
            ]
        },
        fallbacks=[CommandHandler("start", start)]
    )
    application.add_handler(conversation_handler)

    application.run_polling()
