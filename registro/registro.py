def registrar_usuario(nombre, correo):
    return {"nombre": nombre, "correo": correo}

def validar_correo(correo):
    return "@" in correo and "." in correo
