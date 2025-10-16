# -*- coding: utf-8 -*-

"""This module defines constants which are used package-wide."""

DEFAULT_VARS = ['lake_surface_water_temperature', 
                'lswt_quality_level', 
                'lake_ice_cover_class']

LSWT_FLAGS = {0: 'unprocessed', 1: 'bad', 2: 'suspect/marginal',
              3: 'intermediate', 4: 'good', 5: 'best'}

DEFAULT_START = '1992-09-26'
DEFAULT_END = '2020-12-31'

VERSION = '2.1.0'
CCI_DATA_NAME = data_id = 'esacci.LAKES.day.L3S.LK_PRODUCTS.multi-sensor.multi-platform.MERGED.v2-1-0.r1'

PATH_RAW = 'data/raw'
PATH_EXTRACTED = 'data/extracted'
PATH_INTERP = 'data/interpolated'
PATH_AUXILIARY = 'data/auxiliary'
PATH_OUTPUT = 'data/output'
PATH_DINEOF = 'data/output/DINEOF'
PATH_ABBREV = PATH_AUXILIARY+'/abbreviations.json'

FN_MASK = f'lakescci_v{VERSION}_data-availability.shp'
FN_SHP = f'lakescci_v{VERSION}_data-availability.shp'
FN_TABLE = f'lakescci_v{VERSION}_metadata.csv'
URL_TABLE = f'https://climate.esa.int/documents/2607/lakescci_v{VERSION}_metadata.csv'

FN_TABLE_KWARGS = {'delimiter':';'}