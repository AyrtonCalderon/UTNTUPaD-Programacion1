import re
from barrio import Barrio
from habitacion import Habitacion
from vivienda import Vivienda


def validar_texto(mensaje):
  """Función para pedir texto asegurando que no tenga caracteres especiales raros."""
  while True:
    texto = input(mensaje).strip()
    # Permitimos letras (con acentos y ñ), números y espacios.
    if re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]+$", texto):
      return texto
    print(
        "Error: No se permiten simbolos o caracteres especiales."
        " Reintentemos."
    )


def main():
  print("=== CONFIGURACIÓN DEL BARRIO ===")
  nombre_barrio = validar_texto("Ingrese el nombre del barrio: ")
  empresa = validar_texto("Ingrese la empresa constructora: ")
  mi_barrio = Barrio(nombre_barrio, empresa)

  while True:
    print("\n--- AGREGAR NUEVA VIVIENDA ---")
    calle = validar_texto("Calle: ")

    try:
      numero = int(input("Número: "))
    except ValueError:
      numero = 0

    manzana = validar_texto("Manzana (ej. A, B): ")

    try:
      nroCasa = int(input("Número de casa: "))
    except ValueError:
      nroCasa = 1

    try:
      sup_terreno = float(input("Superficie total del terreno (m2): "))
    except ValueError:
      sup_terreno = 100.0

    vivienda = Vivienda(calle, numero, manzana, nroCasa, sup_terreno)

    # Carga de habitaciones
    while True:
      nombre_hab = validar_texto(
          "Nombre de la habitación (escriba 'fin' para terminar con esta"
          " vivienda): "
      )
      if nombre_hab.lower() == "fin":
        break

      try:
        metros_hab = float(input(f"Metros cuadrados de '{nombre_hab}': "))
        vivienda.agregar_habitacion(Habitacion(nombre_hab, metros_hab))
      except ValueError:
        print("⚠️ Por favor, ingrese un número válido para los metros.")

    # Validamos y agregamos la vivienda al barrio
    try:
      vivienda.getMetrosCuadradosCubiertos()
      mi_barrio.agregar_vivienda(vivienda)
      print("Vivienda agregada con exito al barrio!")
    except ValueError as e:
      print(f"No se pudo agregar la vivienda: {e}")

    continuar = input(
        "\nDesea agregar otra vivienda al barrio? (s/n): "
    ).lower()
    if continuar != "s":
      break

  print(f"\n==========================================")
  print(f"--- INFORMACION DEL BARRIO: {mi_barrio.nombre} ---")
  print(f"Empresa Constructora: {mi_barrio.empresaConstructora}")
  print(f"=============================================")

  sup_total = mi_barrio.getSuperficieTotalTerreno()
  print(f"a) Superficie total de terreno del barrio: {sup_total} m2")

  manzana_consulta = validar_texto(
      "\nIngrese la letra de la manzana a consultar (ej. A): "
  )
  sup_manzana = mi_barrio.getSuperficieTotalTerrenoXManzana(manzana_consulta)
  print(
      f"b) Superficie total de terreno (Manzana {manzana_consulta}):"
      f" {sup_manzana} m2"
  )

  try:
    sup_cubierta_total = mi_barrio.getSuperficieTotalCubierta()
    print(f"d) Superficie total cubierta del barrio: {sup_cubierta_total} m2")
  except ValueError as e:
    print(f"Advertencia en superficie cubierta: {e}")


if __name__ == "__main__":
  main()