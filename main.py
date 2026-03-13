
estudiantes = []

def registrar_estudiante():
    nombre = input("Nombre del estudiante: ")
    estudiante = {
        "nombre": nombre,
        "materias": []
    }
    estudiantes.append(estudiante)
    print(f"✓ {nombre} registrado correctamente.\n")


def registrar_materia():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    mostrar_estudiantes()
    numero = int(input("¿A qué estudiante? (número): ")) - 1

    if numero < 0 or numero >= len(estudiantes):
        print("Número inválido.\n")
        return

    materia = input("Nombre de la materia: ")
    nota    = float(input("Nota (0 a 10): "))

    estudiantes[numero]["materias"].append({
        "materia": materia,
        "nota": nota
    })
    print(f"✓ Materia '{materia}' con nota {nota} agregada.\n")


def mostrar_info_estudiante():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    mostrar_estudiantes()
    numero = int(input("¿Qué estudiante quieres ver? (número): ")) - 1

    if numero < 0 or numero >= len(estudiantes):
        print("Número inválido.\n")
        return

    est = estudiantes[numero]
    print(f"\n--- {est['nombre']} ---")

    if not est["materias"]:
        print("  Sin materias registradas.")
    else:
        for m in est["materias"]:
            print(f"  {m['materia']}: {m['nota']}")
    print()

def calcular_promedio(estudiante):
    materias = estudiante["materias"]
    if not materias:
        return None
    total = sum(m["nota"] for m in materias)
    return total / len(materias)

def mostrar_promedio():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    mostrar_estudiantes()
    numero = int(input("¿De qué estudiante? (número): ")) - 1

    if numero < 0 or numero >= len(estudiantes):
        print("Número inválido.\n")
        return

    est     = estudiantes[numero]
    promedio = calcular_promedio(est)

    if promedio is None:
        print(f"{est['nombre']} no tiene materias registradas.\n")
    else:
        print(f"Promedio de {est['nombre']}: {promedio:.2f}\n")


def mejor_estudiante():
    con_notas = [e for e in estudiantes if e["materias"]]

    if not con_notas:
        print("No hay notas registradas aún.\n")
        return

    mejor = max(con_notas, key=calcular_promedio)
    print(f"★ Mejor estudiante: {mejor['nombre']} "
          f"con promedio {calcular_promedio(mejor):.2f}\n")


def mostrar_estudiantes():
    print("\nEstudiantes registrados:")
    for i, est in enumerate(estudiantes, 1):
        print(f"  {i}. {est['nombre']}")
    print()


def menu():
    while True:
        print("================================")
        print("      SISTEMA ACADÉMICO")
        print("================================")
        print("1. Registrar estudiante")
        print("2. Registrar materia y nota")
        print("3. Ver info de un estudiante")
        print("4. Ver promedio de un estudiante")
        print("5. Ver el mejor estudiante")
        print("0. Salir")
        print("--------------------------------")

        opcion = input("Elige una opción: ")

        if   opcion == "1": registrar_estudiante()
        elif opcion == "2": registrar_materia()
        elif opcion == "3": mostrar_info_estudiante()
        elif opcion == "4": mostrar_promedio()
        elif opcion == "5": mejor_estudiante()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.\n")


menu()