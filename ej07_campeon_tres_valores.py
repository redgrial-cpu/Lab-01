# Ejercicio 7: El campeón de tres valores
numero_1 = float(input("Digite el primer número: "))
numero_2 = float(input("Digite el segundo número: "))
numero_3 = float(input("Digite el tercer número: "))

if numero_1 >= numero_2 and numero_1 >= numero_3:
    mayor = numero_1
elif numero_2 >= numero_3:
    mayor = numero_2
else:
    mayor = numero_3

print(f"El número mayor es: {mayor}")
