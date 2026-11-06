# Ejercicio 4: Clasificador de magnitudes (mayor, menor o igual)
numero_1 = float(input("Digite el primer número: "))
numero_2 = float(input("Digite el segundo número: "))

if numero_1 > numero_2:
    print(f"El número mayor es {numero_1} y el menor es {numero_2}")
elif numero_1 < numero_2:
    print(f"El número mayor es {numero_2} y el menor es {numero_1}")
else:
    print("Ambos números son exactamente iguales")
