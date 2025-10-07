
'''EJERCICIO:


Crea ejemplos de funciones básicas que representen las diferentes
posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
Comprueba si puedes crear funciones dentro de funciones.
Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
Pon a prueba el concepto de variable LOCAL y GLOBAL.
Debes hacer print por consola del resultado de todos los ejemplos.
(y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
'''

'''
Funciones definidas por el usuario

'''

#Simple

def greet():
    print("Hola Python")

greet()

#Con retorno

def return_greet():
    return "Hola Python"

print(return_greet())

#Con un argumento

def arg_greet(name):
    print (f"Hola {name}")

arg_greet("Mauris")

#Con argumentos

def args_greet(greet,name):
    print (f"{greet}, {name}")

args_greet("Hi","Mauris")

#Con argumentos predeterminados

def default_greet(name): 
    print (f"hola, {name}")

default_greet("Mauris")

#Con argumentos y return

def args_return_greet(greet,name):  
    return (f"{greet}, {name}")

print(args_return_greet("Hi","Mauris"))

#Con retorno de varios valores

def multiple_return_greet():  
    return "Hola", "Mauris"

greet, name = multiple_return_greet()
print (f"{greet}, {name}")

#Con un numero variable de argumentos

def variable_args_greet(*names):
    for name in names:
        print (f"Hola, {name}")

variable_args_greet("Mauris","Ana","Luis")

#Con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print (f"{value} ({key})")

variable_key_arg_greet(first="Mauris", second="Ana", third="Luis")

'''
Funciones dentro de funciones

'''

def outer_function():
    def inner_function():
        print("Función interna: Hola Python")
    inner_function() 
outer_function()

'''
Funciones del lenguaje

'''

print(len("Hola Python"))  #Función len() para obtener la longitud de una cadena
print(type(123))           #Función type() para obtener el tipo de dato de una variable
print("Hola".upper())  #Método upper() para convertir una cadena a mayúsculas
print("HOLA".lower())  #Método lower() para convertir una cadena a minúsculas

'''
Variables locales y globales

'''
global_var = "Python"
print(global_var)

def hello_python():
    local_var = "Hola"
    print(f'{local_var}, {global_var}') #Accede a variable global

print(global_var) #Accede a variable global
hello_python() #Accede a variable local

'''
EXTRA

'''

def print_numbers(text1, text2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
        count += 1
    return count    

print(print_numbers("Fizz","Buzz"))