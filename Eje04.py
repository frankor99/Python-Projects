#Pedir dos numero al usuario y hacer todas las operaciones basicas de una calculadora

num1=float(input("Ingrese el primer valor:"))
num2=float(input("Ingrese el segundo valor:"))

print(f"La multiplicacion del primer valor con el segundo es {num1} x {num2}={num1*num2}")
print(f"La suma del primer valor con el segundo es {num1} + {num2}={num1+num2}")
print(f"La resta del primer valor con el segundo es {num1} - {num2}={num1-num2}")
print(f"La division del primer valor con el segundo es {num1} / {num2}={num1/num2}")

#Otra forma 
print("suma =" + str(num1+num2))
print("Resta = " + str(num1-num2))
print("Multiplicacion =" + str(num1*num2))
print("Division =" + str(num1/num2))