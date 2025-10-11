'''

 EJERCICIO:
 Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 Utiliza operaciones de inserción, borrado, actualización y ordenación.
 
'''

#Listas

my_list = ['Mauris', 'Alberto', 'Gregorio', 'Marlene']
print(my_list)

my_list.append('Juan') #Insercion
print(my_list)

my_list.remove('Gregorio') #Eliminacion
print(my_list)

my_list[1] = "Ana" #Modificacion
print(my_list)

my_list.sort() #Ordenamiento
print(my_list)

#Tuplas

my_tuple = ('Mauris', 'Alberto', 'Gregorio', 'Marlene')
print(my_tuple[1]) #Acceso a elementos
print(my_tuple[3])
print(type(my_tuple))
my_tuple = sorted(my_tuple) #Ordenamiento
print(my_tuple)

#Sets

my_set = {'Mauris', 'Alberto', 'Gregorio', 'Marlene'}
print(my_set)
my_set.add('Juan') #Insercion
print(my_set)
print(type(my_set))
my_set.remove('Gregorio') #Eliminacion
print(my_set)
my_set = set(sorted(my_set)) #No se puede ordenar
print(my_set)
print(type(my_set))

#Diccionarios

my_dict: dict = {
    'nombre': 'Mauris',
    'apellido': 'Salazar',
    'edad': 39,
    'ciudad': 'Caracas'
}
my_dict["Email"] = "mauris.salazar105@gmail.com" #Insercion
print(my_dict)
print(my_dict['nombre']) #Acceso a elementos
my_dict['edad'] = 40 #Actualizacion
print(type(my_dict))
del my_dict['ciudad'] #Eliminacion
sorted_dict = sorted(my_dict.items()) #Ordenamiento
print(my_dict)
print (type(my_dict))

'''
EXTRA

'''

'''
DIFICULTAD EXTRA (opcional):

 Crea una agenda de contactos por terminal.
 Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 Cada contacto debe tener un nombre y un número de teléfono.
 El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 los datos necesarios para llevarla a cabo.
 El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 (o el número de dígitos que quieras)
 También se debe proponer una operación de finalización del programa.

'''

def my_agenda():
    
    agenda = {}

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar un contacto")
        print("3. Actualizar un contacto")
        print("4. Eliminar un contacto")
        print("5. Salir")

        option = input("Selecciona una opcion: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El numero de telefono de {name} es {agenda[name]}")
                else:
                    print(f"El contacto {name} no se encuentra en la agenda")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                phone = input("Introduce el numero de telefono: ")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone
                else:
                    print("Debes introducir un numero de telefono un maximo de 11 digitos y solo numeros")
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    phone = input("Introduce el nuevo numero de telefono: ")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                        print(f"El contacto {name} ha sido actualizado")
                    else:
                        print("Debes introducir un numero de telefono un maximo de 11 digitos y solo numeros")
                else:
                    print(f"El contacto {name} no se encuentra en la agenda")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print(f"El contacto {name} ha sido eliminado")
                else:
                    print(f"El contacto {name} no se encuentra en la agenda")
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opcion no valida, Elige una opcion del 1 al 5")

my_agenda()