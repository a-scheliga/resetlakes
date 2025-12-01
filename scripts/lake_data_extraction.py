# -*- coding: utf-8 -*-

from multiprocessing import Pool
from codebase.lakecci_functions import data_extraction, find_lakeid

# Define lakes of interest
# Extract specific lakes by lakeids
# lakeids = [6, 2, 8, 9, 10, 12]

# (OR) Extract all lakes
#import pandas as pd
#lakescci_lut = pd.read_csv('data/auxiliary/lakescci_v2.0.2_data-availability.csv')
#lakeids = list(lakescci_lut.id)

# # Common sets of variables
lswt_vars = ["lake_surface_water_temperature","lswt_uncertainty","lswt_quality_level"]
wq_vars = ["chla_mean", "chla_uncertainty", "turbidity_mean", "turbidity_uncertainty"] 
lic_vars = ["lake_ice_cover_class", "lake_ice_cover_flag", "lake_ice_cover_uncertainty"]
lwl_vars = ["water_surface_height_above_reference_datum", "lwl_uncertainty", "lwl_quality_flag"] 
lswe_vars = ["lake_surface_water_extent", "lwe_uncertainty", "lwe_quality_flag"]

# (OR) Extract specific lakes by names
lakenames = ['Great Bear']
lakeids = [find_lakeid(lakename) for lakename in lakenames]

# Set extraction settings
settings = {'variables':lswt_vars, # (list) Variables to extract
            'use_opendap': False,      # (boolean) Download data using oPeNDAP (slow, up to 2sec per day)
            'startdate': '2018-08-25', # (string) Startdate of the timeseries in the form (YYYY-MM-DD)
            'enddate': '2020-09-01',   # (string) Enddate of the timeseries in the form (YYYY-MM-DD)
            'compress': True,          # (boolean) Apply z-lib compression
            'complevel': 4,            # (int) Compression level to use
            'verbose': True,           # (boolean) Print additional status updates
            'use_esacci':True,         # (boolean) Download data using esa_climate toolbox
            }

data_extraction((lakeids[0], settings))

# Multiprocessing settings
n_processes = 1

# # Main (run extraction)
# if __name__ == '__main__':

#     if settings['use_opendap']:
#         print(f'Start extracting {len(lakeids)} lakes using oPeNDAP (slow)..')
#     elif settings['use_esacci']:
#         print(f'Start extracting {len(lakeids)} lakes from ESA CCI Data Store..')
#     else:
#         print(f'Start extracting {len(lakeids)} lakes from local dataset..')
    
#     # Run extraction in multiprocessing pool
#     with Pool(processes=n_processes) as p:
#         outputs = p.map(data_extraction, map(lambda id: (id, settings), lakeids))
