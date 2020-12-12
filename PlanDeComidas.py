import Receta
import Recetario
import PlanComidaDia
import Ingrediente
import random

class Sobrante:

    def __init__(self, receta, raciones):
        self.receta = receta
        self.raciones = raciones

class PlanDeComidas:


    def __init__(self, recetas, comensales = 4):
        self.Recetas = recetas
        self.Plan = []
        self.ListaCompra = []
        self.Comensales = comensales
        self.completo = False

    def SeleccionaPlato(self, temporada, tipo):
    # def dameReceta(self, temporada='todas', tipo='ninguno'):
        return self.Recetas.dameReceta(temporada, tipo)
        # return lPlatos[random.randint(0, len(lPlatos)-1)]

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
            temporada = "Otoño"
        return temporada

    def aniadeReceta(plato, tipo):
    # calculamos cuantos dias tenemos para rellenar con la receta
        nRaciones = plato.Raciones
        nDias = plato.Raciones / self.Comensales
    # buscamos dias libres para rellenar los huecos
        while (nDias > 0 ):
            # buscamos el primer hueco en el que colocar el plato
            colocado = False
            i = 0
            while (colocado == False):
                if tipo == "Entrante" and self.Recetas[i].Entrante == []:
                    self.Recetas[i].Entrante = plato
                    colocado = True
                i = i + 1
            nDias = nDias - 1

    def dame_sobrante(self, sobrantes, tipo, dia):
        sobrante = None
        if dia > 2:
            atras = 2
            while (atras > 0) and not(isinstance(sobrante, Receta.Receta)):
                s = 0
                while ( s < len(sobrantes[dia - atras]) and not(tipo in sobrantes[dia - atras][s].receta.Tipos)):
                    s = s + 1
                if ( s < len(sobrantes[dia - atras]) and (tipo in sobrantes[dia - atras][s].receta.Tipos)):
                    #Hemos encontrado un plato sobrante ya cocinado del tipo que buscamos
                    sobrante = sobrantes[dia - atras][s].receta
                    # calculamos el numero de raciones que quedan
                    sobrantes[dia - atras][s].raciones = sobrantes[dia - atras][s].raciones - self.Comensales
                    if sobrantes[dia - atras][s].raciones <= 0 :
                        sobrantes[dia - atras].remove(sobrantes[dia -atras][s])
                atras = atras - 1
        return sobrante

    def dame_plato(self, sobrantes, temporada, tipo, dia):
        plato = None
        # primero miramos si hay algun plato cocinado que no hayamos comido
        plato = self.dame_sobrante(sobrantes, tipo, dia)
        if plato is None: # no habia sobrantes, tengo que cocinar un plato nuevo
            plato = self.Recetas.dameReceta(temporada, tipo)
        # aqui debemos calcular si hay sobrantes y, si los hay, aniadirlos a la lista de sobrantes
            if plato.Raciones > self.Comensales:
                sobrantes[dia].append(Sobrante(plato, plato.Raciones - self.Comensales))
        return plato

    def rellena_platos(self, temporada, nDias):
        # iniciamos la lista de sobrantes
        sobrantes = []
        for dia in range(0, nDias):
            sobrantes.append([])
        for dia in range(0, nDias):
            # conseguir un entrante
            self.Plan[dia].Entrante = self.dame_plato(sobrantes, temporada, "Entrante", dia)
            # conseguir un principal comida
            self.Plan[dia].PrincipalComida = self.dame_plato(sobrantes, temporada, "PrincipalComida", dia)
            # conseguir una guarnicion comida
            self.Plan[dia].GuarnicionComida = self.dame_plato(sobrantes, temporada, "Guarnicion", dia)
            # conseguir un principal cena
            self.Plan[dia].PrincipalCena = self.dame_plato(sobrantes, temporada, "PrincipalCena", dia)
            # conseguir una guarnicion cena
            self.Plan[dia].GuarnicionCena = self.dame_plato(sobrantes, temporada, "Guarnicion", dia)

    def CrearPlanDeComidas(self, Mes, dias=None):
        # iniciamos el plan de comidas creando un plan de comida diario por cada dia del mes
        # calculamos cuantos platos de cada tipo vamos a necesitar
        # Solicitamos tantos platos de cada tipo como vayamos a necesitar
        self.completo = False
        self.Plan = []
        temporada = self.CalculaTemporadaMes(Mes)
        if dias is None or dias < 0:
            nDias = self.CalculaDiasMes(Mes)
        else:
            nDias = dias
        for dia in range(0, nDias):
            self.Plan.append(PlanComidaDia.PlanComidaDia())
        # calculamos cuantas raciones de cada tipo de plato hacen falta
        self.rellena_platos(temporada, nDias)

    def anadeIngredientes(self, lista):
	# para cada ingrediente de la lista
        for i in range(len(lista)):
        	#busco si el ingrediente esta en la lista
            j =0
            nIngredientes = len(self.ListaCompra)
            while j < nIngredientes and lista[i].Ingrediente != self.ListaCompra[j].Ingrediente :
                j += 1
            if j < nIngredientes and lista[i].Ingrediente == self.ListaCompra[j].Ingrediente :
                # si el ingrediente ya esta en la lista de la compra anadimos la cantidad
                # print (lista[i].Ingrediente, "==", self.ListaCompra[j].Ingrediente )
                # print ("Ahora en la lista hay ", self.ListaCompra[j].Cantidad)
                # print ("Y voy a anadir ", lista[i].Cantidad)
                self.ListaCompra[j].Cantidad = self.ListaCompra[j].Cantidad + lista[i].Cantidad
                # print ("Al final en la lista quedan: ", self.ListaCompra[j].Cantidad )
            else:
                # si el ingrediente no esta en la lista lo anadimos al final
                nuevoIngrediente = Ingrediente.Ingrediente(lista[i].Ingrediente, lista[i].Cantidad, lista[i].Medida)
                self.ListaCompra.append(nuevoIngrediente)

    def CrearListaDeCompra(self):
        print ("Voy a crear la lista de la compra")
        nIngredientes = 0
        self.listaCompra = []
        for plan_dia in self.Plan: # we get the number of days in the plan, i is a PlanComidaDia
            lIngredientes = plan_dia.dameIngredientes()
            print(lIngredientes)
            self.anadeIngredientes(lIngredientes)
        print ("He terminado de crear la lista de la compra")
