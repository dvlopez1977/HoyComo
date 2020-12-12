import Receta
import pathlib
import os
import random

class Recetario:
    tipos = ["Entrante", "Guarnicion", "PrincipalComida", "PrincipalCena"]
    temporadas = ["Primavera", "Verano", "Otoño", "Invierno"]

# un recetario es una coleccion de recetas. F'isicamente es un directorio en el que
# hay una receta en cada uno de los subdirectorios
    def cargarRecetas(self, ruta):
        #en cada uno de los subdirectorios de ruta hay una receta
        #debemos recorrer el directorio ruta y cargar las recetas
        lrecetas= {}
        for tipo in self.tipos:
            lrecetas[tipo]={}
            for temporada in self.temporadas:
                lrecetas[tipo][temporada]=[]
        for ruta,dirs,archs in os.walk(ruta.encode('utf-8', 'surrogateescape').decode('utf-8')):
            for d in dirs:
                receta = Receta.Receta('/'.join([ruta, d]))
                for tipo_receta in receta.Tipos:
                    for temporada_receta in receta.Temporadas:
                        lrecetas[tipo_receta][temporada_receta].append(receta)
        return lrecetas

    def dameReceta(self, temporada='todas', tipo='ninguno'):
        # dado un filtro devuelve una receta
        # de momento el filtro solo incluye  el tipo de receta
        if temporada == 'todas':
            temporada = random.choice(self.temporadas)
        if tipo == 'ninguno':
            tipo = random.choice(self.tipos)
        return random.choice(self.lRecetas[tipo][temporada])

    def __init__ (self, ruta_recetario):
        self.ruta = ruta_recetario
        self.lRecetas = self.cargarRecetas(self.ruta)
