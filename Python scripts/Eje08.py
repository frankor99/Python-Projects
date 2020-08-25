"""
¿cuanto es el x% de y-numero?

"""
Num1=int(input("Ingrese el numero a operar:  "))
Num2=float(input("Ingrese el porcentaje que desea extraer de ese numero en una escala del 1 al 100:  "))
print("\n")
operacion=Num1*(Num2/100)
print(f"El {Num2}% de  {Num1} es {operacion}")