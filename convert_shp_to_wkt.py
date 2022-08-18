#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 20:50:42 2022

@author: satyukt
"""

import os,glob
import geopandas as gpd
from shapely import wkt

in_shps = glob.glob("/media/edrive1/Shashank/Shashank_Projects/UP_classification/village_shp/Sitapur/*.shp")
out_shps = "/home/satyukt/Downloads/out/"

for in_shp in in_shps :
#    print(in_shp)
    shp_filename = os.path.splitext(os.path.basename(in_shp))[0]
    print(shp_filename)
    in_shp = gpd.read_file(in_shp).to_crs(4326)
    out_wkt = (in_shp.geometry)
    
f = open(out_shps + shp_filename + ' .csv', 'w')
f.write(out_wkt.wkt)
f.close()