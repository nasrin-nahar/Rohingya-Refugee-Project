
#author: Nasrin Nahar 
#This code has been used to clip satellite images to the rectangular boundary extent of refugee camp area
import arcpy
from arcpy import env
import os
env.workspace="D:\Rohingya Project-20191106T153319Z-001\Landsat data"
env.overwriteOutput=True

input_dir = "D:\Rohingya Project-20191106T153319Z-001\Landsat data\Input1"
output_dir = "D:\Rohingya Project-20191106T153319Z-001\Landsat data\Clip"

#this list contains all the file name of NDVI folder
input_list = os.listdir(input_dir)

for each_file in input_list:

    print "Generating result for: ", each_file

    #if t = "a.jpg", then print t.split('.') will return ['a','jpg']    
    file_name, extension = each_file.split('.') 

    #input directory + each file in Input1 folder as input
    inp = os.path.join(input_dir, each_file)

    
    #output file is a string = original file name + "_clip." + 'tif'
    output_file = file_name+"_clip."+extension

    #output_directory + output file
    outp = os.path.join(output_dir, output_file) 

    #run arcpy clip management
    arcpy.Clip_management(inp, "402075.686 2311450.636 429645.273 2350370.237", outp, "#", "#", "NONE")

    





