class Receta:
	Titulo = ""
	Temporadas = []
	Ingredientes = []
	Pasos = []
	Tipos = []
	Raciones = 0
	
	def __init__(self, titulo, temporadas, ingredientes, pasos, tipos, raciones):
		self.Titulo = titulo
		self.Temporadas = temporadas
		self.Ingredientes = ingredientes
		self.Pasos = pasos
		self.Tipos = tipos
		self.Raciones = raciones
	
	def imprime(self):
		print (self.Titulo + " " + self.Temporadas + " " + self.Ingredientes + " " + self.Pasos + " " + self.Tipos + " " + self.Raciones)
