import Receta

class PlanComidaDia:
	
	def __init__(self):
		self.Entrante = Receta.Receta("", [], [], [], [], 0)
		self.PrincipalComida = Receta.Receta("", [], [], [], [], 0)
		self.GuarnicionComida = Receta.Receta("", [], [], [], [], 0)
		self.PrincipalCena = Receta.Receta("", [], [], [], [], 0)
		self.GuarnicionCena = Receta.Receta("", [], [], [], [], 0)
	
	def dameIngredientes(self):
		lIngredientes = []
		lIngredientes = self.Entrante.Ingredientes + self.PrincipalComida.Ingredientes + self.GuarnicionComida.Ingredientes + self.PrincipalCena.Ingredientes + self.GuarnicionCena.Ingredientes
#		for i in range(len(lIngredientes)):
#			print (lIngredientes[i].Ingrediente)
#			print (lIngredientes[i].Cantidad)
#			print (lIngredientes[i].Medida)
		return lIngredientes
		
	
	
	
