# CREACION DE UNA AGENDA TELEFONCIA

def mostrar_menu():
    print("\n--- AGENDA TELEFÓNICA ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Modificar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")

def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    agenda[nombre] = telefono
    print(" Contacto agregado.")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre a buscar: ")
    if nombre in agenda:
        print(f" {nombre}: {agenda[nombre]}")
    else:
        print(" Contacto no encontrado.")

def modificar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a modificar: ")
    if nombre in agenda:
        nuevo = input("Ingrese el nuevo teléfono: ")
        agenda[nombre] = nuevo
        print("✏️ Contacto actualizado.")
    else:
        print(" Contacto no encontrado.")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(" Contacto eliminado.")
    else:
        print(" Contacto no encontrado.")

def mostrar_todos(agenda):
    if agenda:
        print("\n--- Lista de Contactos ---")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    else:
        print(" La agenda está vacía.")

# Programa principal
def agenda_telefonica():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            modificar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            mostrar_todos(agenda)
        elif opcion == "6":
            print(" Saliendo de la agenda...")
            break
        else:
            print(" Opción no válida. Intente de nuevo.")

agenda_telefonica()