# en la siguiente funcion deberan escribir la documentacion segun la convencion para el docstring de funciones. 
def area_rectangulo(b,h):
    """calcula el area del rectangulo

    Args:
        b (int|float): este argumento sera la base del rectangulo
        h (int|float): este argumento sera la altura del rectangulo

    Raises:
        los argumentos no podran ser igual o menores a 0
        
    Returns:
        int|float: el resultado de la operacion b*h (base*altura)
    """
    return b*h


# funcion para hallar la potencia de un numero
def potencia(n:int,p:int)->int:
    """_summary_

    Args:
        n (int): _description_
        p (int): _description_

    Returns:
        int: _description_
    """
    resultado:int=1
    for _ in range(p):
        resultado *= n
    return resultado