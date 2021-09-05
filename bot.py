from telegram.ext import Updater
from telegram.ext import CommandHandler

from events.start import start
from events import eventos


telegram_bot_token = '1960999315:AAGU2_X3aMXAyH0GPuzsx7hzxdWBckVdrXA'

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("precios", eventos.obtener_precios))


updater.start_polling()