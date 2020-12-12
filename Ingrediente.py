class Ingrediente:

    def __init__(self, ingrediente, cantidad, medida):
        self.Ingrediente = ingrediente
        self.Cantidad = cantidad
        self.Medida = medida

    def imprimeIngrediente(self):
        print("Ingrediente: " + self.Ingrediente + " " + self.Cantidad + " " + self.Medida)

