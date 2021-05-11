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
 """

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp

import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def create_index_map(first_line):
    first_line = first_line.replace('"','')
    cate_list = first_line.split(',')
    index_map = mp.newMap()
    for i, category in enumerate(cate_list, 1):
        mp.put(index_map, category, i)
    return index_map

index_map = None

# Inicialización del Catálogo de libros    
def create_catalog():
    global index_map
    index_map = create_index_map('"instrumentalness","liveness","speechiness","danceability","valence","loudness","tempo","acousticness","energy","mode","key","artist_id","tweet_lang","track_id","created_at","lang","time_zone","user_id","id"')
    file_1 = model.file_proc("Data/user_track_hashtag_timestamp-small.csv")
    file_2 = model.file_proc("Data/context_content_features-small.csv")
    file_3 = model.file_proc("Data/sentiment_values.csv")
    return model.catalog(file_1, file_2, file_3)
# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def req_1(catalog: model.catalog, characteristic_name: str, minimo, maximo):
    global index_map
    characteristic_index = mp.get(index_map, characteristic_name)['value']
    t_min = model.type_var(minimo)
    if t_min == 'i':
        minimo = int(minimo)
        maximo = int(maximo)
    elif t_min == 'f':
        minimo = float(minimo)
        maximo = float(maximo)
    real_minimo = lt.newList()
    real_maximo = lt.newList()
    for i in range(1, 20):
        if i == characteristic_index:
            lt.addLast(real_minimo, minimo)
            lt.addLast(real_maximo, maximo)
        else:
            lt.addLast(real_minimo, '')
            lt.addLast(real_maximo, '')
    return catalog.req_1(characteristic_index, real_minimo, real_maximo)

def req_2(catalog: model.catalog, en_min: float, en_max: float, dan_min: float, dan_max: float):
    real_minimo = lt.newList()
    real_maximo = lt.newList()
    for i in range(1, 20):
        if i == 9:
            lt.addLast(real_minimo, en_min)
            lt.addLast(real_maximo, en_max)
        else:
            lt.addLast(real_minimo, '')
            lt.addLast(real_maximo, '')
    return catalog.req_2(real_minimo, real_maximo, dan_min, dan_max)

def req_3(catalog: model.catalog, inst_min: float, inst_max: float, temp_min: float, temp_max: float):
    real_minimo = lt.newList()
    real_maximo = lt.newList()
    for i in range(1, 20):
        if i == 1:
            lt.addLast(real_minimo, inst_min)
            lt.addLast(real_maximo, inst_max)
        else:
            lt.addLast(real_minimo, '')
            lt.addLast(real_maximo, '')
    return catalog.req_3(real_minimo, real_maximo, temp_min, temp_max)

def req_4(catalog: model.catalog, generos):
    return catalog.req_4(generos)

def req_5(catalog: model.catalog):
    return catalog.req_5()