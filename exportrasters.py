"""Creating a png file for goodslope, goodlev and goodfinal raster layers"""
import arcpy     #imports arcpy library
mxd=arcpy.mapping.MapDocument("CURRENT")   #Generating png file in ArcMap 
df=arcpy.mapping.ListDataFrames(mxd)[0]
layers=['goodslope','goodelev','goodfinal']

for lyr in arcpy.mapping.ListLayers(mxd):    #Creates "for" loop for reiterating in the mxd file of the map
    if lyr.name in layers:      
        lyr.visible = True       #Summons Boolean result for the name of layer
        ext = lyr.getExtent()     #Summons extent of the layer of interest
        df.extent = ext            #Specifies data frame extent
        arcpy.RefreshTOC()           #Table contents are refreshed
        arcpy.RefreshActiveView()      #Active view in ArcMap is refreshed
        arcpy.mapping.ExportToPNG(mxd,lyr.name + ".png")   #Map layer is exported to png
        lyr.visible = False                 #Layer will remain unseen
 
        
