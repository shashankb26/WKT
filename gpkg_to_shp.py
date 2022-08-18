#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:41:25 2022

@author: satyukt
"""

from osgeo import ogr
import os,glob
import geopandas as gpd

path = "/home/satyukt/Downloads/new_data/*.gpkg"
files = glob.glob(path)
out_gpkg = "/home/satyukt/Downloads/new_data/shp1/"
#
#for file in files :
#    drv = ogr.GetDriverByName( 'ESRI Shapefile' )
#    village = file.split("/")[-1].split(".")[0]
#    file = (gpd.read_file(file)).to_crs(4326)
#    out_wkt = (file.geometry)
#    
#    
#    
#f = open(out_gpkg + village + '.shp', 'w')
#f.write(out_wkt.to_shp)
#f.close()
#    
    


source = ogr.Open('/home/satyukt/Downloads/12409_part.gpkg',update=False)
drv = ogr.GetDriverByName( 'ESRI Shapefile' )
for i in source:
    LayerName = i.GetName() 
    inlyr = source.GetLayer( LayerName )
    outds = drv.CreateDataSource( '/home/satyukt/Downloads/new_data_2/shp/' + LayerName + '.shp')
    outlyr = outds.CopyLayer(inlyr,LayerName)
del inlyr,outlyr,outds    
        
        
        
  





      
        
 