from barrio import Barrio
from habitacion import Habitacion
from vivienda import Vivienda


def main():
  mi_barrio = Barrio("Bº Los Olivos", "Construcciones del Sur S.A.")

  v1 = Vivienda("San Martín", 120, "A", 1, 300.0)
  v2 = Vivienda("Belgrano", 450, "A", 2, 250.0)
  v3 = Vivienda("Rivadavia", 89, "B", 1, 400.0)

  v1.agregar_habitacion(Habitacion("Living", 45.0))
  v1.agregar_habitacion(Habitacion("Cocina", 20.0))
  v1.agregar_habitacion(Habitacion("Dormitorio", 30.0))

  v2.agregar_habitacion(Habitacion("Monoambiente", 50.0))
  v2.agregar_habitacion(Habitacion("Baño", 10.0))

  v3.agregar_habitacion(Habitacion("Living-Comedor", 60.0))
  v3.agregar_habitacion(Habitacion("Dormitorio Principal", 40.0))

  mi_barrio.agregar_vivienda(v1)
  mi_barrio.agregar_vivienda(v2)
  mi_barrio.agregar_vivienda(v3)

  print(f"--- INFORMACIÓN DEL BARRIO: {mi_barrio.nombre} ---")
  print(f"Empresa Constructora: {mi_barrio.empresaConstructora}")

  sup_total = mi_barrio.getSuperficieTotalTerreno()
  print(f"a) Superficie total de terreno del barrio: {sup_total} m2")

  sup_manzana_a = mi_barrio.getSuperficieTotalTerrenoXManzana("A")
  print(f"b) Superficie total de terreno (Manzana A): {sup_manzana_a} m2")

  sup_cubierta_total = mi_barrio.getSuperficieTotalCubierta()
  print(f"d) Superficie total cubierta del barrio: {sup_cubierta_total} m2")

  print("\n--- Probando Validación de Excepción ---")
  try:
    v_erronea = Vivienda("Mitre", 999, "C", 1, 50.0)
    v_erronea.agregar_habitacion(Habitacion("Salón gigante", 80.0))
    v_erronea.getMetrosCuadradosCubiertos()
  except ValueError as e:
    print(f"Excepción atrapada con éxito: {e}")


if __name__ == "__main__":
  main()