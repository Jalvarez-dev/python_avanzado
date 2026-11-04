## crear una funcion que resiva 5 numeros enteros y que retorne solo una listaa de numeros pares, tener en cuenta las anotaciones
def num_pares(a:int,b:int,c:int,d:int,e:int)->list[int]:
    numeros:list[int]=[a,b,c,d,e]
    numeros_pares:list[int]=[]
    for i in numeros:
        if i%2==0:
            numeros_pares.append(i)
    return numeros_pares


def suma(a:int,b:int)->int:
    return a+b

def login(user="",passw=""):
    return "bienvenido al sistema"
print(login(passw="11111",user="hola"))