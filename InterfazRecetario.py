import Recetario
import Receta
import csv


class InterfazRecetario:
	cRuta = ""
	lasRecetas = Recetario.Recetario([])
	
	def __init__(self, ruta):
		self.cRuta = ruta
		FicheroRecetario = open(self.cRuta)
		ReaderRecetario = csv.reader(FicheroRecetario)
		lCsv = list(ReaderRecetario)		
		lRecetas = []
		for i in range(0, len(lCsv)-1):
			receta = Receta.Receta(lCsv[i][0], lCsv[i][1].split(";"), lCsv[i][2].split(";"), lCsv[i][3].split(";"), lCsv[i][4].split(";"), int(lCsv[i][5]))
			lRecetas.append(receta)
		self.lasRecetas = Recetario.Recetario(lRecetas)
		
	def DameRecetario(self):
		self.lasRecetas.imprime
		return self.lasRecetas
