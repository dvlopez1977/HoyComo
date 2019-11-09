import Receta

class PlanComidaDia:
	Entrante = Receta.Receta("", [], [], [], [], 0)
	PrincipalComida = Receta.Receta("", [], [], [], [], 0)
	GuarnicionComida = Receta.Receta("", [], [], [], [], 0)
	PrincipalCena = Receta.Receta("", [], [], [], [], 0)
	GuarnicionCena = Receta.Receta("", [], [], [], [], 0)
	
	def __init__(self):
		self.Entrante = Receta.Receta("", [], [], [], [], 0)
		self.PrincipalComida = Receta.Receta("", [], [], [], [], 0)
		self.GuarnicionComida = Receta.Receta("", [], [], [], [], 0)
		self.PrincipalCena = Receta.Receta("", [], [], [], [], 0)
		self.GuarnicionCena = Receta.Receta("", [], [], [], [], 0)
	
	def dameIngredientes(self):
		lIngredientes = self.Entrante.Ingredientes + self.PrincipalComida.Ingredientes + self.GuarnicionComida.Ingredientes + self.PrincipalCena.Ingredientes + self.GuarnicionCena.Ingredientes
		return lIngredientes
		
	
	
	
