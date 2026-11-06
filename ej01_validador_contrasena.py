# Ejercicio 1: Validador de contraseñas (insensible a mayúsculas)
contrasena_guardada = "Sena2026"

contrasena_ingresada = input("Digite la contraseña: ")

if contrasena_ingresada.lower() == contrasena_guardada.lower():
    print("Acceso Concedido")
else:
    print("Acceso Denegado")
