N = int(input("Ingrese el promedio de infracciones en un mes: "))
matutino = 0.20 * N / 30
vespertino = 0.35 * N / 30
nocturno = 0.45 * N / 30
print("El promedio diario de infracciones en la mañana es de:", matutino)
print("El promedio diario de infracciones en la tarde es de:", vespertino)
print("El promedio diario de infracciones en la noche es de:", nocturno)