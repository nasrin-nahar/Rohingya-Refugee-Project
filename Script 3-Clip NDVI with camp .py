#Author: Nasrin Nahar
#This code has been used clip the cloud free composite of NDVI to refugee camp boundary through 
import arcpy
from arcpy import env
env.workspace="D:\Rohingya Project-20191106T153319Z-001\Landsat data"
env.overwriteOutput=True
input = "D:\Rohingya Project-20191106T153319Z-001\Landsat data\Output\cloud_free_composite.tif"
clipfc = "D:\Rohingya Project-20191106T153319Z-001\Landsat data\Camp_R1\CampR1.shp"
arcpy.Clip_management(input,"402075.686 2311450.636 429645.273 2350370.237","Output\Camp_NDVI.tif",clipfc, "0", "ClippingGeometry","MAINTAIN_EXTENT")


