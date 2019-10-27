import Receta

class Recetario:
	lRecetas = []

	def __init__ (self, recetas):
		self.lRecetas = recetas
	
	def DameRecetas(self, tipo, temporada):
	# Recorremos la lista de recetas sacando aquellas del tipo que nos han pedido 
		recetas = []
		nRecetas = range(len(self.lRecetas))
		for i in nRecetas:
			if tipo in self.lRecetas[i].Tipos and temporada in self.lRecetas[i].Temporadas:
				recetas.append(self.lRecetas[i])
		return recetas
		
	def AnadeReceta(self, receta):
		self.lRecetas.append(receta)
		
	def imprime(self):
		print("Imprimiendo las recetas")
		for i in range(0, len(self.lRecetas)-1):
			self.lRecetas[i].imprime
		
