#sdiaz septiembre 2018
import os
import numpy as np
import pandas as pd
import tensorflow
import googleapi
import raspberryhw


def process_data():
    fertility = pd.read_csv(os.getenv('GAPMINDER_FERTILITY'), index_col='Country', encoding='utf-8')
    life_expectancy = pd.read_csv(os.getenv('GAPMINDER_LIFE_EXPECTANCY'), index_col='Country', encoding='utf-8')
    population = pd.read_csv(os.getenv('GAPMINDER_POPULATION'), index_col='Country', encoding='utf-8')
    face = pd.read_csv(os.getenv('GAPMINDER_face'), index_col='Country', encoding='utf-8')

    #columnas por nombres
    columns = list(fertility.columns)
    years = list(range(int(columns[0]), int(columns[-1])))
    rename_dict = dict(zip(columns, years))

    fertility = fertility.rename(columns=rename_dict)
    life_expectancy = life_expectancy.rename(columns=rename_dict)
    population = population.rename(columns=rename_dict)
    face = face.rename(columns=rename_dict)

    face_list = list(face.Group.unique())

    # cambia los scalares
    scale_factor = 3.14
    population_size = np.sqrt(population / np.pi) / scale_factor
    min_size = 3
    population_size = population_size.where(population_size >= min_size).fillna(min_size)

    return fertility, life_expectancy, population_size, face, years, face_list
