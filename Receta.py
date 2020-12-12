import pathlib
import csv
import Ingrediente

class Receta:
# Esta clase es responsable de cargar del disco duro una receta
# cada receta se almacena en un directorio con el nombre de la receta
# en el directorio hay tres ficheros llamados
#   * Ingredientes.csv
#   * Pasos.csv
#   * Temporada.csv
   csvIngredientes = "Ingredientes.csv"
   csvPasos = "Pasos.csv"
   csvTipos = "Tipos.csv"
   csvTemporadas = "Temporada.csv"
   csvRaciones = "Raciones.csv"

   def obtenerTitulo(self, RutaReceta):
       # devuelve la ruta relativa al ultimo directorio de la ruta
       ruta = pathlib.PurePath(RutaReceta)
       return ruta.name

   def obtenerIngredientes(self, RutaReceta):
       RutaIngredientes = '/'.join([RutaReceta, self.csvIngredientes])
       FicheroIngredientes = open(RutaIngredientes)
       ReaderIngredientes = csv.reader(FicheroIngredientes)
       lCsv = list(ReaderIngredientes)
       lIngredientes = []
       for i in range(0, len(lCsv)):
           # El formato de los ingredientes
           # Ingrediente,cantidad,unidad
           # print("Cargando Ingrediente " + lCsv[i][0] + " " + lCsv[i][1] + " " + lCsv[i][2])
           ingrediente = Ingrediente.Ingrediente(lCsv[i][0], lCsv[i][1], lCsv[i][2])
           # ingrediente.imprimeIngrediente()
           lIngredientes.append(Ingrediente)
       FicheroIngredientes.close()
       return lIngredientes

   def obtenerPasos(self, RutaReceta):
       RutaPasos = '/'.join([RutaReceta, self.csvPasos])
       FicheroPasos = open(RutaPasos)
       ReaderPasos = csv.reader(FicheroPasos)
       lCsv = list(ReaderPasos)
       lPasos = []
       for i in range(0, len(lCsv)):
           # El formato de los pasos es
           # una linea por paso
           lPasos.append(lCsv[i][0])
       FicheroPasos.close()
       return lPasos

   def obtenerTemporadas(self, RutaReceta):
       RutaTemporadas = '/'.join([RutaReceta, self.csvTemporadas])
       FicheroTemporadas = open(RutaTemporadas)
       ReaderTemporadas = csv.reader(FicheroTemporadas)
       lCsv = list(ReaderTemporadas)
       lTemporadas = []
       for i in range(0, len(lCsv)):
           lTemporadas.append(lCsv[i][0])
       FicheroTemporadas.close()
       return lTemporadas

   def obtenerTipos(self, RutaReceta):
       RutaTipos = '/'.join([RutaReceta, self.csvTipos])
       FicheroTipos = open(RutaTipos)
       ReaderTipos = csv.reader(FicheroTipos)
       lCsv = list(ReaderTipos)
       lTipos = []
       for i in range(0, len(lCsv)):
           lTipos.append(lCsv[i][0])
       FicheroTipos.close()
       return lTipos

   def obtenerRaciones(self, RutaReceta):
       RutaRaciones = '/'.join([RutaReceta, self.csvRaciones])
       FicheroRaciones = open(RutaRaciones)
       ReaderRaciones = csv.reader(FicheroRaciones)
       lCsv = list(ReaderRaciones)
       FicheroRaciones.close()
       return int(lCsv[0][0])

   def imprimeIngredientes(self):
       for ingrediente in self.Ingredientes:
           # ingrediente.imprimeIngrediente()
           ingrediente.imprimeIngrediente()

   def __init__(self, RutaReceta):
   # Dada una ruta absoluta hacia una receta carga los ficheros desde el disco
   #
   # 1/. Obtenemos el nombre de la receta
   #def obtenerTitulo(self, RutaReceta):
       self.Titulo = self.obtenerTitulo(RutaReceta)
   # 2/. Cargamos los ingredientes
       self.Ingredientes = self.obtenerIngredientes(RutaReceta)
   # 3/. Cargamos los pasos
       self.Pasos = self.obtenerPasos(RutaReceta)
   # 4/. Cargamos la temporada de la receta
       self.Temporadas = self.obtenerTemporadas(RutaReceta)
   # 5/. Cargamos los tipos de la receta
       self.Tipos = self.obtenerTipos(RutaReceta)
   # 6/. Cargamos las raciones de la receta
       self.Raciones = self.obtenerRaciones(RutaReceta)
       self.imprimeIngredientes()
