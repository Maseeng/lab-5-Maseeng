"""The script describes the resolution of the raster band"""
#Output: The raster resolution of band one is 0.000277778 by 0.000277778 Degree.
import arcpy    #Imports arcpy library
from arcpy import env
env.workspace="C:\Users\MMasitha\Downloads\Lab_5_Working_with_Rasters\Lab_5_Working_with_Rasters\Data Lab_5_Working_with_Rasters"   #Sets up workspace environment
rasterband="tm.img/Layer_1"      #Specifies tm.img/Layer_ as the variable of interest or band
desc=arcpy.Describe(rasterband)    #Provides a description for the raster band, tm.img/Layer_1
x=desc.meanCellHeight               #Specifies grid cell height
y=desc.meanCellWidth                 #Specifies grid cell width
spatialref=desc.spatialReference      #Specifies spatial reference system of the band
units=spatialref.angularUnitName       #Specifies unit of the spatial reference
print "The raster resolution of band one is " + str(x) + " by " + str(y) + " " + units + "."   #The resolution is given in print

