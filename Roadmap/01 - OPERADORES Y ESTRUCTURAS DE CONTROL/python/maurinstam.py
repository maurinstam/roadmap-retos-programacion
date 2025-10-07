'''

 EJERCICIO:

 Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 que representen todos los tipos de estructuras de control que existan
 en tu lenguaje:
 Condicionales, iterativas, excepciones...
 Debes hacer print por consola del resultado de todos los ejemplos.
 

'''

'''
Operadores

'''

#Operadores aritmeticos

print(f'suma: 10 + 3 = {10 + 3}') # interpolacion
print(f'resta: 10 - 3 = {10 - 3}') # interpolacion
print(f'multiplicacion: 10 * 3 = {10 * 3}') # interpolacion
print(f'division: 10 / 3 = {10 / 3}') # interpolacion
print(f'modulo: 10 % 3 = {10 % 3}') # interpolacion
print(f'exponente: 10 ** 3 = {10 ** 3}') # interpolacion
print(f'division entera: 10 // 3 = {10 // 3}') # interpolacion

#Operadores logicos

print(f'AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}')
print(f'OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4}')
print(f'NO !: not 10 + 3 == 14 es {not 10 + 3 == 14}' )

#Operadores de comparacion

print (f'Igualdad: 10 == 3 {10 == 3}')
print (f'desigualdad: 10 != 3 {10 != 3}')
print (f'mayor que: 10 != 3 {10 > 3}')
print (f'menor que: 10 != 3 {10 < 3}')
print (f'mayor o igual que: 10 >= 10 {10 >= 10}')
print (f'menor o igual que: 10 <= 3 {10 <= 3}')

#Operadores de asignacion

miNumero = 15
print(miNumero) #asignacion 

miNumero += 1 #suma  y asignacion
print(miNumero)

miNumero -= 1 #resta  y asignacion
print(miNumero)

miNumero *= 2 #multiplicacion  y asignacion
print(miNumero)

miNumero /= 2 #division  y asignacion
print(miNumero)

miNumero %= 2 #modulo  y asignacion
print(miNumero)

miNumero **= 1 #exponente  y asignacion
print(miNumero)

miNumero //= 1 #division entera  y asignacion
print(miNumero)

#Operadores de identidad

minuevoNumero = miNumero
print(f'mi numero is mi nuevo numero es {miNumero is minuevoNumero}')
print(f'mi numero is not mi nuevo numero es {miNumero is not minuevoNumero}')

#Operadores de pertenencia

print(f"'u' in 'mauris' = '{'u' in 'mauris'}'")
print(f"'b' not in 'mauris' = '{'b' in 'mauris'}'")

#Operadores bits

a = 10 #1010
b = 3 #0011

print(f'AND: 10 & 3 = {10 & 3}') #0010
print(f'OR: 10 & 3 = {10 & 3}') #1011
print(f'XOR: 10 & 3 = {10 & 3}') #1001
print(f'NOT: 10 & 3 = {10 & 3}') #0010
print(f'Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}') #0010
print(f'Desplazamiento a la izquierda: 10 << 2 = {10 << 2}') #101000 

'''

Estructuras de control

'''

#Condicionales

mi_nombre = "Mauris"

if mi_nombre == "Mauris":
    print("Hola, Mauris")
elif mi_nombre == "Juan":
    print("Hola, Juan")
else:
    print("Hola, extraño")

#Iterativas

#Bucle for
for i in range(11):
    print(i)

#Bucle while
contador = 0
while contador < 11:   
    print(contador)
    contador += 1

#Excepciones

try:
     print (10 / 0)   
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")



'''
Extra

'''

for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
