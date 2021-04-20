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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

class file_proc:
    def __init__(self, filepath: str, *args):
        self.filepath = filepath
        self.index_types = lt.newList(datastructure='ARRAY_LIST')
        for itype in args:
            lt.addLast(self.index_types, itype)

class catalog:
    def array_line(self, line, index_types):
        if line:
            array = lt.newList(datastructure='ARRAY_LIST')
            i = 1
            for element in line.items():
                element_obj = element[1].replace('"', '')
                if lt.getElement(index_types, i) == 'f':
                    lt.addLast(categories, float(element_obj))
                elif lt.getElement(index_types, i) == 'i':
                    lt.addLast(categories, int(element_obj))
                else:
                    lt.addLast(categories, element_obj)
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



# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
