"""
Solicitar la calificacion de 15 alunmnos e indicar cuantos aprobaron y cuantos
reprobaron

"""
cont=int(input("Ingrese la cantidad de alumnos a calificar:  "))
apro1=0
repro1=0
apro2=0
repro2=0
for i in range(1,(cont+1)):
    nota=int(input(f"Ingrese la calificacion del alumno numero {i}:  "))

    if  nota<0:
        print("La calificacion no puede ser vacia o negativa, intentelo de nuevo")
        nota=int(input(f"Ingrese la calificacion del alumno numero {i}:  "))
        print(nota)
        if nota>5:
            apro1+=1
        else:
            repro1+=1

    else:
        print(nota)
        if nota>5:
            apro2+=1
        else:
            repro2+=1
            

print(f"Aprobaron {apro1+apro2} alumnos y reprobaron {repro1+repro2}")
