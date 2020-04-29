# -*- coding: cp1252 -*-
"""The script calculates the inclination of a slope using the “elevation” raster"""
import arcpy          #imports arcpy module
from arcpy import env
from arcpy.sa import *    #imports Spatial Analyst extension 
env.workspace = "C:\Users\MMasitha\Downloads\Lab_5_Working_with_Rasters\Lab_5_Working_with_Rasters\Data Lab_5_Working_with_Rasters"  #Sets up workspace environment
if arcpy.CheckExtension("spatial") == "Available":      #Indicates whether extension is active
    arcpy.CheckOutExtension("spatial")
    outraster = arcpy.sa.Slope("elevation", "PERCENT_RISE")    
    outraster.save("slope_per")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."    #If the extension is not available, prints this statement.
