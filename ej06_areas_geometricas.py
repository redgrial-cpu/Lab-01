# Ejercicio 6: Calculadora de áreas geométricas
import math

print("A. Triángulo")
print("B. Círculo")
opcion = input("Elija la figura: ").strip().upper()

if opcion == "A":
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    if base <= 0 or altura <= 0:
        print("Las medidas deben ser mayores que cero")
    else:
        area = base * altura / 2
        print(f"El área del triángulo es: {area:.2f}")
elif opcion == "B":
    radio = float(input("Digite el radio: "))
    if radio <= 0:
        print("Las medidas deben ser mayores que cero")
    else:
        area = math.pi * radio ** 2
        print(f"El área del círculo es: {area:.2f}")
else:
    print("Opción no válida")
