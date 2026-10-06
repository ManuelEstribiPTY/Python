estudiante = str(input("Ingrese su nombre: "))
count = 0
notas = 0
while True:
    notas += float(input("Ingrese su nota:"))
    count += 1
    if count == 3:
        division= float(notas/(count))
        nota = print("Su nota final es: ", division)
        break

if division >= 3:
    print(estudiante, "Aprobado")
else:
    print(estudiante, "No aprobado")