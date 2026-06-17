def validar_texto_saludo(texto):
    if not isinstance(texto, str):
        return False
    if len(texto) == 0 or len(texto) > 50:
        return False
    if texto == "Hola Mundo":
        return True
    return False
