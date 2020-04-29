"""This script describes the landcover.tiff raster dataset resolution"""
#Output of the script: The raster resolution is 30.0 by 30.0 Meter
import arcpy   #imports arcpy library
from arcpy import env
env.workspace="C:\Users\MMasitha\Downloads\Lab_5_Working_with_Rasters\Lab_5_Working_with_Rasters\Data Lab_5_Working_with_Rasters"   #Sets up workspace environment
raster="landcover.tif"    #Specifies landcover.tif as the variable of interest or raster data
desc=arcpy.Describe(raster)    #Summons a description for the landcover.tif
x=desc.meanCellHeight           #Specifies grid cell height
y=desc.meanCellWidth             #Specifies grid cell width
spatialref=desc.spatialReference     #Specifies spatial reference system for the dataset
units = spatialref.linearUnitName      #Specifies the unit for the dataset
print "The raster resolution is " + str(x) + " by " + str(y) + " " + units + "."  #Prints the resolution of the dataset
