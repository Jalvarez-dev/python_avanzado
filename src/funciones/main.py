# crear un programa que me permita mostar mensajes personalizados, crear un funcion similar a la funcion print de python
def mi_print(mensaje:str):
    texto=f"""
    --------------------------------
    {mensaje}
    --------------------------------
    """
    
    print(texto)

mi_print("hola como estas es es un nuevo mensaje")
mi_print("este es otro texto")