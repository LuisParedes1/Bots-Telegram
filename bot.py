from telegram.ext import Updater
from telegram.ext import CommandHandler

from events.start import start


telegram_bot_token = 'TOKEN'

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()