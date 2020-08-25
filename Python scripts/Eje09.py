"""
Hacer un progrma que pida numeros indefinidamente al usuario
y los muestre por pantalla hasta que ingrese el numero 111

"""

num=0
while num != 111:
    num=float(input("Ingrese un numero:  "))

    if num == 111:
        break
    else:
        continue

"""
Otra forma seria simplemente con el siguiente codigo

num=0
while num != 111:
    num=float(input("Ingrese un numero:  "))

"""

