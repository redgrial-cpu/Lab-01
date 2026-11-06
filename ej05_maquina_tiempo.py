# Ejercicio 5: La máquina del tiempo
anio_1 = int(input("Digite el primer año: "))
anio_2 = int(input("Digite el segundo año: "))

diferencia = abs(anio_1 - anio_2)

if anio_1 > anio_2:
    print(f"Desde el año {anio_2} han pasado {diferencia} años.")
elif anio_1 < anio_2:
    print(f"Para llegar al año {anio_2} faltan aún {diferencia} años.")
else:
    print("Ambos años son iguales, no hay diferencia de tiempo.")
