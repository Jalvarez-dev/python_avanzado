# ejercicio usando la tecnica *args crear una funcion que me permita identificar numeros pares de n cantidad de numeros pasados por argumento la funcion debera retornar una lista con los numeros pares identificados
def num_pares(*args)->list[int]:
    pares:list[int]=[]
    for i in args:
        if i % 2 == 0:
            pares.append(i)
    return pares
print(num_pares(2,5,8,6,5,3,5,6,8,2))
print(num_pares(10,50,20,4,8,100,300))
