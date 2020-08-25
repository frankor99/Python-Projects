"""
Mostrar los numeros impares que esten entre dos numeros
ingresados por el usuario.

"""
num1=int(input("Ingrese el primer numero:  "))
num2=int(input("Ingrese el segundo numero:  "))

if num1 < num2:
    for i in range(num1,(num2+1)):
        if i%2!=0:
            print(i)
else: print("El primer numero debe ser menor que el segundo")