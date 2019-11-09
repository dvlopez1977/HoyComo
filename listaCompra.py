import PlanDeComidas

class listaCompra:
	Ingredientes = []
	lCompra = []
	
	def __init__(self, PlanDeComidas):
		# Recorremos el plan de comidas anadiendo los ingredientes de cada receta
		for i in range(0,len(PlanDeComidas.Plan)-1):
			self.Ingredientes = ingredientes
