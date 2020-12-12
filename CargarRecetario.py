import Receta
import Recetario
import PlanDeComidas

def imprime_plan_diario(plan_dia):
    print("El entrante es: " + plan_dia.Entrante.Titulo)
    print("El principal es: " + plan_dia.PrincipalComida.Titulo + " acompa;ado de " + plan_dia.GuarnicionComida.Titulo)
    print("Para cenar tenemos: " + plan_dia.PrincipalCena.Titulo + " acompa;ado de " + plan_dia.GuarnicionCena.Titulo)

def imprime_plan_mes(plan):
    i = 0
    for plan_dia in plan.Plan:
        print("-------------------")
        print("El menu para el dia " + str(i))
        imprime_plan_diario(plan_dia)
        print("-------------------")
        i = i + 1

def imprime_ingrediente(ingrediente):
    print("Ingrediente " + ingrediente.Ingrediente + " Cantidad: " + ingrediente.Cantidad +" " + ingrediente.Medida)

def imprime_lista_compra(plan):
    print ("")
    print ("Imprimiendo la lista de la compra")
    print ("---------------------------------")
    for ingrediente in plan.listaCompra:
        imprime_ingrediente(ingrediente)

def main():
    # 1/. cargamos el recetario
    ruta_recetario = "/home/dvlopez/HoyComo/Recetario/"
    print("La ruta al recetario es:" + ruta_recetario)
    recetario = Recetario.Recetario(ruta_recetario)
    for tipo in recetario.tipos:
        print("Estos son los " + tipo + " del recetario")
        for temporada in recetario.temporadas:
            print("Estos son los " + tipo + " que comemos en " + temporada)
            for receta in recetario.lRecetas[tipo][temporada]:
                print (receta.Titulo)
    # 2/. creamos el plan de comidas
    plan = PlanDeComidas.PlanDeComidas(recetario)
    plan.CrearPlanDeComidas("Diciembre", 5)
    imprime_plan_mes(plan)

    # 3/. creamos la lista de la compra
    plan.CrearListaDeCompra()
    imprime_lista_compra(plan)

if __name__ == "__main__":
    main()
