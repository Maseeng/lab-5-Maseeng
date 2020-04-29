#Outputs: This script provides a description of the raster dataset
"""Outputs:
Raster base name is: tm
Raster data type is: RasterDataset
Raster file extension is: img
desc.spatialReference.name: GCS_North_American_1983
desc.format: IMAGINE Image
desc.compressionType: RLE
desc.bandCount: 3
"""
import arcpy         #imports arcpy library
from arcpy import env
env.workspace="C:\Users\MMasitha\Downloads\Lab_5_Working_with_Rasters\Lab_5_Working_with_Rasters\Data Lab_5_Working_with_Rasters" #Sets workspace environment
raster="tm.img"   #Specifies tm.img as the variable of interest
desc=arcpy.Describe(raster)     #Summons a description for the raster listed in above
print "Raster base name is: " + desc.basename     #Prints basename of the raster data
print "Raster data type is: " + desc.dataType       #Prints the datatype
print "Raster file extension is: " + desc.extension    #Prints the datatype extension of the file
print "Raster spatial reference type is: " + desc.spatialReference.name    #Prints spatial reference of the raster
print"Raster format is: " + desc.format                   #Prints format of the raster data type
print "Raster compression type is: " + desc.compressionType          #Prints compression type of the raster data
print "Raster band numbers: " + str (desc.bandCount)                #Prints number of bands of the raster 
