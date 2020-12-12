import Receta

class PlanComidaDia:
    tipos = ['Entrante', 'PrincipalComida', 'GuarnicionComida', 'PrincipalCena', 'GuarnicionCena']
    def __init__(self):
        self.plan_dia = {}
        for tipo in self.tipos:
            self.plan_dia[tipo] = []

    def dameIngredientes(self):
        lIngredientes = []
        for key in self.plan_dia.keys():
            print("El " + key + " tiene " + str(len(self.plan_dia[key])) + " ingredientes")
            for ingrediente in self.plan_dia[key]:
                print("tratando ingrediente " + ingrediente.Ingrediente )
                lIngredientes.append(ingrediente)
        return lIngredientes
