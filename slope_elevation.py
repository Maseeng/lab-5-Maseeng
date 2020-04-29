"""Started by importing the Spatial Analyst module to access its functionality of the extension: tools, operators, functions, and classes"""
"""The script descibed the permanent state of the raster"""
"""We used map algebra operators"""
from arcpy import env
env.workspace="C:\Users\MMasitha\Downloads\Lab_5_Working_with_Rasters\Lab_5_Working_with_Rasters\Data Lab_5_Working_with_Rasters" #Sets up workspace environment
outraster=arcpy.sa.Slope("elevation")   #Accessing "Slope" toolbox to identify the gradient of each grid cell of raster data
desc=arcpy.Describe(outraster)    #Description of the outraster argument is "elevation"
print desc.permanent             #Description of the state is printed
outraster.save("slope")         #Gradient result is saved
from arcpy.sa import *            #Imports functionality of Spatial Analyst in a more elegant way
outraster2=Aspect("elevation")    
outraster2.save("aspect")        #Adds compass directionality to the downhill slope for each grid cell in the raster
elevraster = arcpy.Raster("elevation") #Map algebra operators will be applied until the final output is saved
outraster3 = elevraster * 3.281
outraster3.save("elev_ft")
slope = Slope(elevraster)
goodslope = slope < 20
goodelev = elevraster < 2000
goodfinal = goodslope & goodelev
goodfinal.save("final")

