import Recetario
import Receta
import Ingrediente
import csv


class InterfazRecetario:


	
	def __init__(self, ruta):
		self.cRuta = ruta
		FicheroRecetario = open(self.cRuta)
		ReaderRecetario = csv.reader(FicheroRecetario)
		lCsv = list(ReaderRecetario)		
		lRecetas = []
		for i in range(0, len(lCsv)-1):
			#El formato del csv de recetas es:
			#	Titulo,temporadas,rutaIngredientes,rutaPasos,tipo,raciones
			ingredientes = self.CargaIngredientes(lCsv[i][2])
			receta = Receta.Receta(lCsv[i][0], lCsv[i][1].split(";"), ingredientes, lCsv[i][3].split(";"), lCsv[i][4].split(";"), int(lCsv[i][5]))
			lRecetas.append(receta)
		self.lasRecetas = Recetario.Recetario(lRecetas)
	
	def CargaIngredientes(self,rutaIngredientes):
		FicheroIngredientes = open(rutaIngredientes)
		ReaderIngredientes = csv.reader(FicheroIngredientes)
		lcsvIngredientes = list(ReaderIngredientes)
		lIngredientes = []
		for i in range(0, len(lcsvIngredientes)-1):
			ingrediente = Ingrediente.Ingrediente(lcsvIngredientes[i][0],float(lcsvIngredientes[i][1]),lcsvIngredientes[i][2])
			lIngredientes.append(ingrediente)
		return lIngredientes
			
	def DameRecetario(self):
		self.lasRecetas.imprime
		return self.lasRecetas
