from events.send_message import send_message

def obtener_mensaje_bienvenida(name):

    return "Hola {usuario}, preciona /{comando} para obtener la lista de precios".format(usuario=name,comando="precios" )

def start(update, context):
    name = str(update.effective_user.first_name)
    send_message(update,context, obtener_mensaje_bienvenida(name))