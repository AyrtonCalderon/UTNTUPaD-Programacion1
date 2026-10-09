from alumno import Alumno
from nota import Nota

class CargaNotas:
    @staticmethod
    def main():
        alumnos = []

        # Bucle principal para cargar alumnos
        while True:
            print("\n --- INGRESE LOS DATOS DEL ALUMNO ---")
            
            # Validación Nombre: No permite texto vacío
            while True:
                nombre = input("Ingrese el nombre del alumno: ").strip()
                if nombre:
                    break
                print("Error: El nombre no puede estar vacío.")

            # Validación Legajo: Debe ser un número entero positivo
            while True:
                try:
                    legajo = int(input("Ingrese el numero de legajo: "))
                    if legajo > 0:
                        break
                    print("Error: El legajo debe ser un número entero positivo.")
                except ValueError:
                    print("Error: Ingrese un número entero válido.")

            alumno = Alumno(nombre, legajo)

            # Bucle secundario para cargar notas
            while True:
                print("\n-- CARGA DE DATOS --")
                
                # Validación Cátedra: No permite texto vacío
                while True:
                    catedra = input("Ingrese el nombre de la catedra: ").strip()
                    if catedra:
                        break
                    print("Error: La cátedra no puede estar vacía.")

                # Validación Nota Examen: Debe ser un número entre 1 y 10
                while True:
                    try:
                        nota_examen = float(input("Nota (1-10): "))
                        if 1.0 <= nota_examen <= 10.0:
                            break
                        print("Error: La nota debe estar entre 1 y 10.")
                    except ValueError:
                        print("Error: Ingrese un número decimal o entero válido.")

                nueva_nota = Nota(catedra, nota_examen)
                alumno.agregar_nota(nueva_nota)

                # Confirmación para salir de la carga de notas
                salir_notas = input("Desea salir de la carga de notas? (S/N): ").strip().lower()

                if salir_notas == "s":
                    # Regla del negocio: al menos 1 nota ingresada
                    if len(alumno.notas) >= 1:
                        break
                    else:
                        print("Debe ingresar al menos 1 nota para este alumno.")

            alumnos.append(alumno)

            # Confirmación para salir de la carga de alumnos
            salir_alumno = input("\nDesea salir de la carga de alumnos? (S/N): ").strip().lower()
            if salir_alumno == "s":
                break

        # --- MOSTRAR RESULTADOS FINALES ---
        print("\n" + "=" * 40)
        print("RESUMEN DE ALUMNOS Y NOTAS")
        print("=" * 40)

        for a in alumnos:
            print(f"\nDatos Alumno: {a.nombreCompleto} (Legajo: {a.legajo})")
            print("Notas:")
            for n in a.notas:
                print(f"  - Cátedra: {n.catedra} | Nota: {n.nota_examen}")
            
            print(f"El promedio del alumno es: {a.calcular_promedio():.2f}")


if __name__ == "__main__":
    CargaNotas.main()