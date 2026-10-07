# crear un programa que me permita desarrollar las 4 opoeraciones basica (suma, resta, division, multiplicacion)
def operaciones(n:list,o:str):
    if o=="+":
        return sum(n)
print(operaciones([4,8,20,78],"+"))    