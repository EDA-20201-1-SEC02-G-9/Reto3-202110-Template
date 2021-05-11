"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import linkedlistiterator as ll_it 
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Reproducciones por rango de característica")
    print("3- Música para festejar")
    print("4- Música para estudiar")
    print("5- Estudiar género")
    print("6- Género Musical más escuchado")

catalog = None

def print_req_2(resultado):
    iterator = ll_it.newIterator(resultado)
    while ll_it.hasNext(iterator):
        res = tuple(ll_it.next(iterator))
        print("{} tiene {} de energía y {} de danceabilidad".format(*res))

def print_req_3(resultado):
    iterator = ll_it.newIterator(resultado)
    while ll_it.hasNext(iterator):
        res = tuple(ll_it.next(iterator))
        print("{} tiene {} de instrumentalidad y {} de tempo".format(*res))

def aux_print_4(resultado):
    iterator = ll_it.newIterator(resultado)
    while ll_it.hasNext(iterator):
        res = ll_it.next(iterator)
        print(res)

def print_req_4(resultado):
    iterator = ll_it.newIterator(resultado)
    while ll_it.hasNext(iterator):
        res = tuple(ll_it.next(iterator))
        print("{} tiene {} y {} artistas".format(*res[0:3]))
        print("Artistas de {}".format(res[0]))
        aux_print_4(res[3])
        print("\n\n")


def print_req_5(resultado):
    iterator = ll_it.newIterator(resultado)
    while ll_it.hasNext(iterator):
        res = tuple(ll_it.next(iterator))
        print("{} tiene {} reproducciones".format(*res))

"""
Menu principal
"""
catalog = None
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.create_catalog()
    elif int(inputs[0]) == 2:
        char_i = input("Introduzca la característica: ")
        minimo = input("Introduzca el mínimo: ")
        maximo = input("Introduzca el máximo: ")
        resultado = controller.req_1(catalog, char_i, minimo, maximo)
        print("{} reproducciones y {} artistas".format(*resultado))
    elif int(inputs[0]) == 3:
        en_min = float(input("Introduzca el mínimo de energía: "))
        en_max = float(input("Introduzca el máximo de energía: "))
        dan_min = float(input("Introduzca el mínimo de danceabilidad: "))
        dan_max = float(input("Introduzca el máximo de danceabilidad: "))
        resultado = controller.req_2(catalog, en_min, en_max, dan_min, dan_max)
        print("{} canciones".format(resultado[0]))
        print_req_2(resultado[1])
    elif int(inputs[0]) == 4:
        inst_min = float(input("Introduzca el mínimo de instrumentalidad: "))
        inst_max = float(input("Introduzca el máximo de instrumentalidad: "))
        temp_min = float(input("Introduzca el mínimo de tempo: "))
        temp_max = float(input("Introduzca el máximo de tempo: "))
        resultado = controller.req_3(catalog, inst_min, inst_max, temp_min, temp_max)
        print("{} canciones".format(resultado[0]))
        print_req_3(resultado[1])
    elif int(inputs[0]) == 5:
        genero = "t"
        generos = lt.newList()
        while True:
            genero = input("Introduzca el género o deje vacío para terminar: ")
            if not genero:
                break
            lt.addLast(generos, genero)
        resultado =controller.req_4(catalog, generos)
        print_req_4(resultado)
    elif int(inputs[0]) == 6:
        resultado = controller.req_5(catalog)
        print_req_5(resultado[0])
        print("{} es el máximo con {} reproducciones".format(*resultado[1]))
    else:
        sys.exit(0)
sys.exit(0)
