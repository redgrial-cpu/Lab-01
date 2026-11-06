# Ejercicio 2: División segura
dividendo = input("Digite el dividendo: ").strip()
divisor = input("Digite el divisor: ").strip()

dividendo_valido = dividendo.removeprefix("-").replace(".", "", 1).isdigit()
divisor_valido = divisor.removeprefix("-").replace(".", "", 1).isdigit()

if not dividendo_valido or not divisor_valido:
    print("Entrada inválida")
elif float(divisor) == 0:
    print("No se puede dividir por cero")
else:
    resultado = float(dividendo) / float(divisor)
    print(f"Resultado: {resultado}")
