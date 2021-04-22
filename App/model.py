"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import rbt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.DataStructures import arraylistiterator as al_it
from DISClib.DataStructures import linkedlistiterator as ll_it 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def req_1_cmpfunc(characteristic: int, list1, list2):
    char_1 = lt.getElement(list1, characteristic)
    char_2 = lt.getElement(list2, characteristic)
    id_1 = lt.getElement(list1, 19)
    id_2 = lt.getElement(list2, 19)
    if char_1 < char_2:
        return -1
    elif char_1 > char_2:
        return 1
    else:
        if id_1 < id_2:
            return -1
        elif id_1 > id_2:
            return 1
        else:
            return 0

def count_artists(rango, reproducciones) -> int:
    artists_ids = mp.newMap(numelements=reproducciones)
    rango_it = ll_it.newIterator(rango)
    while ll_it.hasNext(rango_it):
        mp.put(artists_ids, ll_it.next(rango_it), 1)
    return mp.size(artists_ids)

def type_var(var):
    if var.isnumeric():
        return 'i'
    elif var.replace('.','').isnumeric():
        return 'f'
    else:
        return 's'

class file_proc:
    def indexes(self):
        f = open(self.filepath, 'r')
        f.readline()
        line = f.readline()
        f.close()
        params = line.replace('"','').split(',')
        indexes = lt.newList(datastructure='ARRAY_LIST')
        for par in params:
            lt.addLast(indexes, type_var(par))
        self.index_types = indexes
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.indexes()

class catalog:
    def array_line(self, line, index_types):
        if line:
            array = lt.newList(datastructure='ARRAY_LIST')
            i = 1
            for element in line.items():
                element_obj = element[1].replace('"', '')
                if lt.getElement(index_types, i) == 'f':
                    if element_obj:
                        lt.addLast(array, float(element_obj))
                    else:
                        lt.addLast(array, 0.0)
                elif lt.getElement(index_types, i) == 'i':
                    if element_obj:
                        lt.addLast(array, int(element_obj))
                    else:
                        lt.addLast(array, 0)
                else:
                    lt.addLast(array, element_obj)
                i += 1
            return array
        else:
            return None

    def create_matrix(self, file: file_proc):
        filepath = file.filepath
        index_types = file.index_types
        if filepath is not None:
            input_file = csv.DictReader(open(filepath, encoding="utf-8"), delimiter=',')
            matrix = lt.newList(datastructure='ARRAY_LIST')
            for line in input_file:
                array = self.array_line(line, index_types)
                if array:
                    lt.addLast(matrix, array)
            return matrix

    def __init__(self, file_basic: file_proc, file_characteristics: file_proc, file_sentiments: file_proc):
        self.basic_catalog = self.create_matrix(file_basic)
        self.characteristics_catalog = self.create_matrix(file_characteristics)
        self.sentiments_catalog = self.create_matrix(file_sentiments)

    def req_1(self, characteristic: int, minimo, maximo):
        cmpfunc = lambda a,b: req_1_cmpfunc(characteristic,a,b)
        char_rbt = rbt.newMap(cmpfunc)
        for music in catalog_iterator(self, 1):
            rbt.put(char_rbt, music, lt.getElement(music, 12))
        rango = rbt.values(char_rbt, minimo, maximo)
        reproducciones = lt.size(rango)
        artistas = count_artists(rango, reproducciones)
        return (reproducciones, artistas)

class catalog_iterator:
    def __init__(self, music_catalog: catalog, index:int):
        this_catalog = None
        if index == 0:
            this_catalog = music_catalog.basic_catalog
        elif index == 1:
            this_catalog = music_catalog.characteristics_catalog
        elif index == 2:
            this_catalog = music_catalog.sentiments_catalog
        self.m_it = al_it.newIterator(this_catalog)

    def __next__(self):
        if al_it.hasNext(self.m_it):
            return al_it.next(self.m_it)
        else:
            raise StopIteration
    
    def __iter__(self):
        return self



# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
