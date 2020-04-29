"""Output of the script:
aspect
Elevation
elev_ft
final
landcover.tif
slope
slope_per
tm.img
""""
import arcpy     #imports arcpy library
from arcpy import env
env.workspace="C:\Users\MMasitha\Downloads\Lab_5_Working_with_Rasters\Lab_5_Working_with_Rasters\Data Lab_5_Working_with_Rasters"    #Sets up workspace environment
rasterlist = arcpy.ListRasters()    #Summons a list of raster datasets
for raster in rasterlist:           #"For" loop reiterates in the raster list to find rasters to print
   print raster

