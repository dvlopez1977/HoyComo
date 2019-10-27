import Receta
import Recetario
import PlanComidaDia
import random

class PlanDeComidas:
	Recetas = Recetario.Recetario([])
	Plan = []
	Comensales = 4
	
	def __init__(self, recetas):
		self.Recetas = recetas
		
	def SeleccionaPlato(self, lPlatos):
		return lPlatos[random.randint(0, len(lPlatos)-1)]
	
	def CalculaDiasMes(self, Mes):
		lMeses31 = ["Enero", "Marzo", "Mayo", "Julio", "Agosto", "Octubre", "Diciembre"]
		nDias = 30
		if Mes == "Febrero":
			nDias = 28
		elif Mes in lMeses31:
			nDias = 31
		return nDias
		
	def CalculaTemporadaMes(self, Mes):
		Primavera = ["Abril", "Mayo", "Junio"]
		Verano = ["Julio", "Agosto", "Septiembre"]
		Otono = ["Octubre", "Noviembre", "Diciembre"]
		
		temporada = "Invierno"
		if Mes in Primavera:
			temporada = "Primavera"
		elif Mes in Verano:
			temporada = "Verano"
		elif Mes in Otono:
			temporada = "Otono"
		return temporada
			
	def CrearPlanDeComidas(self, Mes):
		self.Plan = []
		temporada = self.CalculaTemporadaMes(Mes)
		lPrincipales = self.Recetas.DameRecetas("Principal", temporada)
		lEntrantes = self.Recetas.DameRecetas("Entrante", temporada)
		lGuarniciones = self.Recetas.DameRecetas("Guarnicion", temporada)
		nDia = 0
		nDias = self.CalculaDiasMes(Mes)
		while ( nDia < nDias ):
			# creamos el plan diario
			planDia = PlanComidaDia.PlanComidaDia()
			# seleccionamos recetas al azar
			planDia.Entrante = self.SeleccionaPlato(lEntrantes)
			planDia.PrincipalComida = self.SeleccionaPlato(lPrincipales)
			planDia.GuarnicionComida = self.SeleccionaPlato(lGuarniciones)
			planDia.PrincipalCena = self.SeleccionaPlato(lPrincipales)
			planDia.GuarnicionCena = self.SeleccionaPlato(lGuarniciones)
			# anhadimos la receta al plan
			self.Plan.append(planDia)
			nDia = nDia + 1
