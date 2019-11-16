import Recetario
import Receta
import PlanDeComidas
import InterfazRecetario
import random
import csv
#
# Programa principal
#

# 1 leemos algunas recetas de un fichero csv:
#
LectorRecetas = InterfazRecetario.InterfazRecetario("./recetario.csv")

# imprimimos las recetas
print("Estas son las recetas")
recetitas = LectorRecetas.DameRecetario()
recetitas.imprime()
print("----")

# 2 creamos el plan de comidas
planazo = PlanDeComidas.PlanDeComidas(recetitas)
#planazo = PlanDeComidas.PlanDeComidas(LectorRecetas.DameRecetario())
print("Intento crear el plan de comidas")

planazo.CrearPlanDeComidas("Junio")
#for i in range(len(planazo.Plan)):
#   print(i+1, "Entrante: ", planazo.Plan[i].Entrante.Titulo)
#   print(i+1, "Principal: ", planazo.Plan[i].PrincipalComida.Titulo)
#   print(i+1, "Guarnicion: ", planazo.Plan[i].GuarnicionComida.Titulo)
#   print(i+1, "Cena: ", planazo.Plan[i].PrincipalCena.Titulo)
#   print(i+1, "Guarnicion cena: ", planazo.Plan[i].GuarnicionCena.Titulo)

planazo.CrearListaDeCompra()
nIngredientes = range(len(planazo.listaCompra))
print ("Hay un total de ", nIngredientes, " ingredientes en la lista de la compra")
for i in range(len(planazo.ListaCompra)):
   print(i, "Ingrediente: ", planazo.ListaCompra[i].Ingrediente)
   print(i, "Cantidad: ", planazo.ListaCompra[i].Cantidad)
   print(i, "Medida: ", planazo.ListaCompra[i].Medida)

