import re  # Importa re para validación de contraseña y poder usar el re.search

# Lista global de usuarios
usuarios = []

# Función para registrar un usuario
def registrar_usuarios():
    global usuarios

    # Validar nombre de usuario único
    while True:
        nombre = input("Escriba su nombre de usuario: ")
        if any(user['nombre'] == nombre for user in usuarios):
            print("Ese nombre de usuario ya existe. Intente con otro.")
        else:
            break

    # Validar sexo
    while True:
        sexo = input("Escriba su sexo (F o M): ").upper()
        if sexo in ['F', 'M']:
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")

    # Validar contraseña
    def validar_contraseña(contra):
        if len(contra) < 8:
            return False
        if " " in contra:
            return False
        if not re.search(r"[A-Za-z]", contra):
            return False
        if not re.search(r"[0-9]", contra):
            return False
        return True

    while True:
        contra = input("Ingrese contraseña: ")
        if validar_contraseña(contra):
            print("Contraseña válida.")
            break
        print("Contraseña no valida. Intente otra.")

    # Agrega el usuario
    usuarios.append({'nombre': nombre, 'sexo': sexo, 'contraseña': contra})
    print("Usuario ingresado con éxito!!")

# Función para buscar usuario
def buscar_usuarios():
    nombre = input("Ingrese usuario a buscar: ")
    for user in usuarios:
        if user['nombre'] == nombre:
            print(f"Nombre: {user['nombre']}, Sexo: {user['sexo']}, Contraseña: {user['contraseña']}")
            return
    print("El usuario no se encuentra.")

# Función para eliminar usuario
def eliminar_usuarios():
    nombre = input("Ingrese el nombre de usuario que quiere eliminar: ")
    for i, user in enumerate(usuarios):
        if user['nombre'] == nombre:
            del usuarios[i]
            print("Usuario eliminado con éxito!")
            return
    print("El usuario no se encuentra.")

# Menú principal (fuera de función)
menu = 0

while menu != 4:
    try:
        menu = int(input("MENU PRINCIPAL\n1.- Ingresar usuario.\n2.- Buscar usuario.\n3.- Eliminar usuario.\n4.- Salir.\nIngrese opción: "))
    except ValueError:
        print("Debe ingresar una opción válida!!")
        continue

    if menu == 1:
        registrar_usuarios()
    elif menu == 2:
        buscar_usuarios()
    elif menu == 3:
        eliminar_usuarios()
    elif menu == 4:
        print("Programa terminado...")
    else:
        print("Debe ingresar una opción válida!!")
