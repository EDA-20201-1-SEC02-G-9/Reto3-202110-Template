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

def max_rep(ans_list):
    iterator = ll_it.newIterator(ans_list)
    maximo = ('',0)
    while ll_it.hasNext(iterator):
        valor = ll_it.next(iterator)
        if maximo[1] < valor[1]:
            maximo = valor
    return maximo

def setup_genres():
    genre_map = mp.newMap()
    mp.put(genre_map, "Reggae", (60, 90))
    mp.put(genre_map, "Down-tempo", (70, 100))
    mp.put(genre_map, "Chill-out", (90, 120))
    mp.put(genre_map, "Hip-Hop", (85, 115))
    mp.put(genre_map, "Jazz and Funk", (120, 125))
    mp.put(genre_map, "Pop", (100, 130))
    mp.put(genre_map, "R&B", (60, 80))
    mp.put(genre_map, "Rock", (110, 140))
    mp.put(genre_map, "Metal", (100, 160))
    return genre_map

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

def req_2_cmpfunc(list1, list2):
    en_1 = lt.getElement(list1, 9)
    en_2 = lt.getElement(list2, 9)
    id_1 = lt.getElement(list1, 14)
    id_2 = lt.getElement(list2, 14)
    if en_1 < en_2:
        return -1
    elif en_1 > en_2:
        return 1
    elif id_1 < id_2:
        return -1
    elif id_1 > id_2:
        return 1
    else:
        return 0

def req_3_cmpfunc(list1, list2):
    inst_1 = lt.getElement(list1, 1)
    inst_2 = lt.getElement(list2, 1)
    id_1 = lt.getElement(list1, 14)
    id_2 = lt.getElement(list2, 14)
    if inst_1 < inst_2:
        return -1
    elif inst_1 > inst_2:
        return 1
    elif id_1 < id_2:
        return -1
    elif id_1 > id_2:
        return 1
    else:
        return 0

def req_4_cmpfunc(list1, list2):
    temp_1 = lt.getElement(list1, 7)
    temp_2 = lt.getElement(list2, 7)
    id_1 = lt.getElement(list1, 14)
    id_2 = lt.getElement(list2, 14)
    if temp_1 < temp_2:
        return -1
    elif temp_1 > temp_2:
        return 1
    elif id_1 < id_2:
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

def count_artists_2(rango, reproducciones) -> int:
    artists_ids = mp.newMap(numelements=reproducciones)
    rango_it = ll_it.newIterator(rango)
    while ll_it.hasNext(rango_it):
        mp.put(artists_ids, ll_it.next(rango_it), 1)
    artist_list = lt.newList()
    artist_full_list = mp.keySet(artists_ids)
    iterator = ll_it.newIterator(artist_full_list)
    for i in range(0,10):
        if not ll_it.hasNext(iterator):
            break
        lt.addLast(artist_list, ll_it.next(iterator))
    return mp.size(artists_ids), artist_list

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
        self.req_1_rbt = mp.newMap()
        self.genres = setup_genres()

    def req_1(self, characteristic: int, minimo, maximo):
        char_rbt = None
        if mp.get(self.req_1_rbt, characteristic):
            char_rbt = mp.get(self.req_1_rbt, characteristic)
        else:
            cmpfunc = lambda a,b: req_1_cmpfunc(characteristic,a,b)
            char_rbt = rbt.newMap(cmpfunc)
            for music in catalog_iterator(self, 1):
                rbt.put(char_rbt, music, lt.getElement(music, 12))
            mp.put(self.req_1_rbt, characteristic, char_rbt)
        rango = rbt.values(char_rbt, minimo, maximo)
        reproducciones = lt.size(rango)
        artistas = count_artists(rango, reproducciones)
        return (reproducciones, artistas)
    
    def req_2(self, en_min, en_max, dan_min:float, dan_max:float):
        char_rbt = None
        if mp.get(self.req_1_rbt, 20):
            char_rbt = mp.get(self.req_1_rbt, 20)['value']
        else:
            char_rbt = rbt.newMap(req_2_cmpfunc)
            for music in catalog_iterator(self, 1):
                rbt.put(char_rbt, music, [lt.getElement(music, 14),lt.getElement(music,9),lt.getElement(music, 4)])
            mp.put(self.req_1_rbt, 20, char_rbt)
        rango = rbt.values(char_rbt, en_min, en_max)
        itera = ll_it.newIterator(rango)
        count = 0
        res_list = lt.newList()
        while ll_it.hasNext(itera):
            danceability = ll_it.next(itera)
            if danceability[2] >= dan_min and danceability[2] <= dan_max:
                count += 1
                if count <= 5:
                    lt.addLast(res_list, danceability)
        return count, res_list
    
    def req_3(self, inst_min, inst_max, temp_min:float, temp_max:float):
        char_rbt = None
        if mp.get(self.req_1_rbt, 21):
            char_rbt = mp.get(self.req_1_rbt, 21)['value']
        else:
            char_rbt = rbt.newMap(req_3_cmpfunc)
            for music in catalog_iterator(self, 1):
                rbt.put(char_rbt, music, [lt.getElement(music, 14),lt.getElement(music, 1),lt.getElement(music, 7)])
            mp.put(self.req_1_rbt, 21, char_rbt)
        rango = rbt.values(char_rbt, inst_min, inst_max)
        itera = ll_it.newIterator(rango)
        count = 0
        res_list = lt.newList()
        while ll_it.hasNext(itera):
            tempo = ll_it.next(itera)
            if tempo[2] >= temp_min and tempo[2] <= temp_max:
                count += 1
                if count <= 5:
                    lt.addLast(res_list, tempo)
        return count, res_list
    
    def req_4_aux(self, min_temp, max_temp):
        char_rbt = None
        if mp.get(self.req_1_rbt, 22):
            char_rbt = mp.get(self.req_1_rbt, 22)['value']
        else:
            char_rbt = rbt.newMap(req_4_cmpfunc)
            for music in catalog_iterator(self, 1):
                rbt.put(char_rbt, music, lt.getElement(music, 12))
            mp.put(self.req_1_rbt, 22, char_rbt)
        rango = rbt.values(char_rbt, min_temp, max_temp)
        reproducciones = lt.size(rango)
        artistas = count_artists_2(rango, reproducciones)
        return (reproducciones, *artistas)
    
    def req_5_aux(self, temp_min, temp_max):
        char_rbt = None
        if mp.get(self.req_1_rbt, 7):
            char_rbt = mp.get(self.req_1_rbt, 7)['value']
        else:
            cmpfunc = lambda a,b: req_1_cmpfunc(7,a,b)
            char_rbt = rbt.newMap(cmpfunc)
            for music in catalog_iterator(self, 1):
                rbt.put(char_rbt, music, lt.getElement(music, 12))
            mp.put(self.req_1_rbt, 7, char_rbt)
        rango = rbt.values(char_rbt, temp_min, temp_max)
        reproducciones = lt.size(rango)
        return reproducciones
    
    def req_5_aux_2(self, temp_min, temp_max):
        real_minimo = lt.newList(datastructure='ARRAY_LIST')
        real_maximo = lt.newList(datastructure='ARRAY_LIST')
        for i in range(1, 20):
            if i == 7:
                lt.addLast(real_minimo, temp_min)
                lt.addLast(real_maximo, temp_max)
            else:
                lt.addLast(real_minimo, '')
                lt.addLast(real_maximo, '')
        return real_minimo, real_maximo

    def req_4(self, genre_list):
        genre_it = ll_it.newIterator(genre_list)
        ans_list = lt.newList()
        while ll_it.hasNext(genre_it):
            genre = ll_it.next(genre_it)
            temp_min, temp_max = mp.get(self.genres, genre)['value']
            temp_min, temp_max = self.req_5_aux_2(temp_min, temp_max)
            lt.addLast(ans_list, (genre, *self.req_4_aux(temp_min, temp_max)))
        return ans_list

    def req_5(self):
        genre_list = mp.keySet(self.genres)
        genre_it = ll_it.newIterator(genre_list)
        ans_list = lt.newList()
        while ll_it.hasNext(genre_it):
            genre = ll_it.next(genre_it)
            temp_min, temp_max = mp.get(self.genres, genre)['value']
            temp_min, temp_max = self.req_5_aux_2(temp_min, temp_max)
            reproducciones = self.req_5_aux(temp_min, temp_max)
            lt.addLast(ans_list, (genre, reproducciones))
        maximo = max_rep(ans_list)
        return ans_list, maximo


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
