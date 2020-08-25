#Ingresar dos numero y mostrar por pantalla los numeros contenido entre los dos numero ingresados
num1=int(input("Ingrese el primer numero  "))
num2=int(input("Ingrese el segundo numero  "))

if num1<num2:
    for i in range(num1,(num2+1)):
        print(i)
else:
    print("El primer numero debe ser menor que el segundo")