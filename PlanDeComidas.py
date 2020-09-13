import Receta
import Recetario
import PlanComidaDia
import Ingrediente
import random

class PlanDeComidas:

    def __init__(self, recetas):
        self.Recetas = recetas
        self.Plan = []
        self.ListaCompra = []
        self.Comensales = 4
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

    def anadeIngredientes(self, lista):
		# para cada ingrediente de la lista
        for i in range(len(lista)):
			#busco si el ingrediente esta en la lista
            j =0
            nIngredientes = len(self.ListaCompra)
#            print ("Busco ingrediente:", lista[i].Ingrediente,",",lista[i].Cantidad)
            while j < nIngredientes and lista[i].Ingrediente != self.ListaCompra[j].Ingrediente :
#				print (lista[i].Ingrediente," != ", self.ListaCompra[j].Ingrediente)
                j += 1
            if j < nIngredientes and lista[i].Ingrediente == self.ListaCompra[j].Ingrediente :
                # si el ingrediente ya esta en la lista de la compra anadimos la cantidad
                print (lista[i].Ingrediente, "==", self.ListaCompra[j].Ingrediente )
                print ("Ahora en la lista hay ", self.ListaCompra[j].Cantidad)
                print ("Y voy a anadir ", lista[i].Cantidad)
                self.ListaCompra[j].Cantidad = self.ListaCompra[j].Cantidad + lista[i].Cantidad
                print ("Al final en la lista quedan: ", self.ListaCompra[j].Cantidad )
            else:
                # si el ingrediente no esta en la lista lo anadimos al final
                nuevoIngrediente = Ingrediente.Ingrediente(lista[i].Ingrediente, lista[i].Cantidad, lista[i].Medida)
                self.ListaCompra.append(nuevoIngrediente)


    def CrearListaDeCompra(self):
        print ("Voy a crear la lista de la compra")
        nIngredientes = 0
        self.listaCompra = []
        for i in range(len(self.Plan)):
            lIngredientes = self.Plan[i].dameIngredientes()
            print ("Estoy trabajando con el plan diario numero: " , i)
            nIgredientes = len(lIngredientes)
            for j in range(len(lIngredientes)):
                print (lIngredientes[j].Ingrediente, "," , lIngredientes[j].Cantidad, ",", lIngredientes[j].Medida)
            self.anadeIngredientes(lIngredientes)
        print ("He terminado de crear la lista de la compra")
