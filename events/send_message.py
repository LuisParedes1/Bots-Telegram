def send_message(update, context,message):
    chat_id = update.effective_chat.id

    context.bot.send_message(chat_id=chat_id, text=message)