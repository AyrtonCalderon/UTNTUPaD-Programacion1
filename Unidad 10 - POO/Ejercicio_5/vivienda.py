#Esta clase tiene los atributos basicos, una lista para guardar habitaciones y el metodo para calcular la superficie cubierta validando que no supere el terreno.
#Python
from habitacion import Habitacion


class Vivienda:

  def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
    self.calle = calle
    self.numero = numero
    self.manzana = manzana
    self.nroCasa = nroCasa
    self.superficieTerreno = superficieTerreno
    self.listaHabitaciones = []

  def agregar_habitacion(self, habitacion):
    self.listaHabitaciones.append(habitacion)

  def getMetrosCuadradosCubiertos(self):
    total_cubiertos = sum(h.metrosCuadrados for h in self.listaHabitaciones)

    if total_cubiertos > self.superficieTerreno:
      raise ValueError(
          "La superficie cubierta no puede ser mayor a la superficie del terreno"
      )

    return total_cubiertos