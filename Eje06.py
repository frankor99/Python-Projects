""" 
Mostrar todas las tablas de multiplicar del 1 al 10 
mostrando el titulo de las tablas y las multiplicaciones

"""

for i in range(0,11):
    print(f"####### Tabla del {i}######")
    for a in range(0,11):
        print(f"{a} x {i} = {a*i}")
    print('\n')