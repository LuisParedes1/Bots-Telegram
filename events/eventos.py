from events.send_message import send_message

def obtener_precios(update, context):
    send_message(update,context, "10 Pesos")