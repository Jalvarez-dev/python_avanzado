# Funciones en python
las funciones no permiten ordenar mejor el codigo y reutilizarlo cuando sea necesario.
```python
# ejemplo deseamos crear un programa en python que nos permite sumar dos numeros
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)
```
como hacemos reutilizable el ejercicio anterior y mas lejible.
para eso utilizaremos funciones.
la caracteristica de una funcion en python es la siguiente:
1. debe comenzar con la palabra reservada `def`.
2. debe tener un nombre que de a entender que realizara la funcion.
3. debera tener parametros y estos estaran encerrados en parentesistes `()`. no todas las funciones resibiran parametros aun asi debera tener los `()`
4. las funciones deberan retornar datos a travez de la palabra reservada `return`

```python
# crear un programa que me permita sumar dos numeros
def sumar(a:int,b:int):
    return a+b

print(sumar(78,56))
print(sumar(45,5))
```
## funciones avanzadas
existen tres grandes conceptos para poder entender el uso avanzada de las funciones:
1. argumentos, parametros posicionles y nominales, *args y +kargs.
2. anotaciones en la salida de una funcion.
3. recursividad.

```python
# anotacion en una funcion
def suma(a:int,b:float)->int:
    return a+b
# crear solo las notaciones de una funcion que resiva cutro numeros enteros y como salida que me muestre os 4 numeros enters en una lista
def numeros_lista(a:int,b:int,c:int,d:int)->list[int]:
    return [a,b,c,d]
```
**Argumentos Parametros**
- **Parametros** - los parametros son las variables que se declaran en la definicion de la funcion
- **Argumentos** - es el dato concreto enviado en el llamado de la funcion
**Nota:** en ambos casos tenemos los posicionales/nominales
```python
# parametros
def suma(a,b): # en este caso tenemos una funcion suma que recibe dos parametros a,b
suma(34,45) # en este caso estoy llamndo a la funcion pasandole como argumento los datos.
# en este caso en concreto podemos decir que estamos frente a una funcion que tiene parametros posicionales, eso siginifica que cada valor reemplaza en el orden que le pasemos a las vaariables, 34->a , 45->b

def login(usuario="",password=""):
    return "acceso correcto"
login(password="12345678",usuario="tupapi")
# esta funcion es una funcion nominal por que para pasar los valores tengo que indicar la variable a la que se le va asociar en el parametro de la funcion.
```
## conociendo mas sobre funciones parametros y argumentos
sobre los parametros/argumentos nominales es ampliamente usado para distintas configuraciones y que se puede pasar solo los argumentos que se usaran y dejar los parametros por defecto si no se van a modificar.
```python
# tenemos un program que me permite accede a internet que tiene parmetrs por defecto, sin embargo si se actualiza uno de los accesos se podra modificar el valor.
## primer caso accesos por defecto
def config(user="admin",pass="1234",port="8080",BSSID="wifi"):
    return "conectado a la red"
config()
## segundo caso l BSSID cambi por el de "laboratorio1"
def config(user="admin",pass="1234",port="8080",BSSID="wifi"):
    return "conectado a la red"

config(BSSID="laboratorio1")

## reyner desea conectarse al wifi de ana luz, pregunta cmo se llama tu wifi y cual es la contraseña. respuesta le dice el wifi es A56 y su contraseña es 12345678
def config(user="admin",pass="1234",port="8080",BSSID="wifi"):
    return "conectado a la red"

config(BSSID="A56",pass="12345678")
```

### conociendo *args y **kargs (empaquetado y desempaquetado de argumentos posicionales)
### desempaquetando argumentos posicionales
esta tecnica nos permite empaquetas nuestros argumentos cuando no sabemos la cantidad de datos que vamos a pasar. imaginemos que nos piden una funcion para suma n cantidad de numeros la solucion seria empaquetar los arguments y luego desempaquetarlos para ello en la definicion de la funcion dentro de los paarametrs debemos usar el operador `*` delante del nombre del parametro posicional esto hara que todos los argumentos se almacenen en una tupla`()` (lista`[]`) esto nos permite recorer dentro de sus elementos para poder desempaquetarlo y realizar las operaciones necesarias.
```python
# deseamos crear un funcion que nos permita sumar n cantidad de numeros
# n es un numero varible puede ser 3, 7, 8 .....n
def suma(*args):
    #*args = (2,5,7,8,9)
    acumulado=0
    for i in args:
        acumulado += i
    return acumulado
print(suma(2,5,7,8,9))
```
#### desempaquetando argumentos nominales
en es caso como en el anterior utilizaremos el operador `*` la casuistic es el mismo sin embargo paraa desempaaquetar aargumento nominales usaremos `**` delante del nombre del parametro nominal ,  diferenciaa del anterior esto se empaquetar en un diccionario(`{clave:valor}`).
```python
# debemos crear una funcion que me permita saber  encontrar la perosna con mayor calificacion.
def mejor_alumno(**kwargs):
    # **kwargs={'noemi':20,'eduardo':18,'david':19}
    nota_maxima=-1
    for alumno,nota in kwargs.items():
        if nota > nota_maxima:
            nota_maxima = nota
            mejor_alumno = alumno
    return mejor_alumno
mejor_alumno(noemi=20,eduardo=18,david=19)
```
## Funciones Anonimas
las funciones anonimas en python son llamadas `lambda`, estas funciones tienen las siguientes propiedades:
1. se escribe en una unica sentencia`(linea)`.
2. no tiene nombre`(anonima)`.
3. su cuerpo conlleva un `return` implicito.
4. puede recibir cualquier numero de parametros.

la estructura para definir una funcion `lambda` es la siguiente:
1. escribir la palabra reservada `lambda`.
2. especificar la cantidad de parametros.
3. indicar los datos de retorno
```python
lambda a,b: a+b
```
> [!TIP] Puesto que esta funcion es anonima para ejecurtarla debemos almacenar la funcion en una variable.

```python
suma=lambda a,b: a+b
suma(3,6)
```
## Documentacion
python nos permite documentar un funcion con el objetivo de explicar mejor determinadas zonas de nuestro codigo, para eso usamos una cadena de texto despues de la definicion de una funcion, a esta cadena de texto se le conoce como `docstring` y esta delimitado por triples `""" aqui el texto """`.
```python
def suma(a,b):
    """
    funcion paar realizar la suma de dos numeros
    """
## los docstring tambien nos permite explicar los parametros que recibe y los datos de salida
def resta(a,b):
    """
    a= un numero entero.
    b= un numer entero.
    en ambos casos a,b no deben recibir vaalores menores  0.
    retornara un dato entero <int> positivo
    """
    return a-b
```
> [!WARNING] en el proceso de documentacion tener encuenta de incluir a lo menos lo siguiente: 1. breve explicacion sbre que hace la funcion 2. especificaciones y caracteristicas de los parametros incluyendo sus tipos. 3. restriccines de la funcion. 4. el valor que retorna y sus caracteristicas