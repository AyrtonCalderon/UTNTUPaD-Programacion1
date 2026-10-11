from vivienda import Vivienda


class Barrio:

  def __init__(self, nombre, empresaConstructora):
    self.nombre = nombre
    self.empresaConstructora = empresaConstructora
    self.listaViviendas = []

  def agregar_vivienda(self, vivienda):
    self.listaViviendas.append(vivienda)

  def getSuperficieTotalTerreno(self):
    return sum(v.superficieTerreno for v in self.listaViviendas)

  def getSuperficieTotalTerrenoXManzana(self, manzana):
    return sum(
        v.superficieTerreno
        for v in self.listaViviendas
        if v.manzana == manzana
    )

  def getSuperficieTotalCubierta(self):
    return sum(v.getMetrosCuadradosCubiertos() for v in self.listaViviendas)