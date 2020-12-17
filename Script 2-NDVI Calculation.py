
#author: Nasrin Nahar
#This code has been used to calculate NDVI from each scene and create a cloud free composite of NDVI

import osgeo
from osgeo import ogr, gdal, osr
import numpy as np
import os
import matplotlib.pyplot as plt

def run(img1, img2, out):
    
    #img path
    in_path_1 = img1
    in_path_2 = img2 
    
    #output path
    NDVI_out_path = out
    
    #open raster bands
    raster_1 = gdal.Open(in_path_1)
    raster_2 = gdal.Open(in_path_2)
    
    #read bands as matrix arrays
    raster_1_data = raster_1.GetRasterBand(1).ReadAsArray().astype(float)
    raster_2_data = raster_2.GetRasterBand(1).ReadAsArray().astype(float)
    
    print(raster_1.GetProjection()[:80])
    print(raster_2.GetProjection()[:80])
    if raster_1.GetProjection()[:80]==raster_2.GetProjection()[:80]: 
        print('SRC OK')
        
    print(raster_1_data.shape)
    print(raster_2_data.shape)
    if raster_1_data.shape==raster_2_data.shape: 
        print('Array Size OK')
        
    print(raster_1.GetGeoTransform())
    print(raster_2.GetGeoTransform())
    if raster_1.GetGeoTransform()==raster_2.GetGeoTransform(): 
        print('Geotransformation OK')
        
    #geotransform = raster_2.GetGeoTransform()
    
    originX,pixelWidth,empty,finalY,empty2,pixelHeight=geotransform
    cols =  raster_2.RasterXSize
    rows =  raster_2.RasterYSize
    
    projection = raster_2.GetProjection()
    finalX = originX + pixelWidth * cols
    originY = finalY + pixelHeight * rows
    
    print(raster_1_data.shape, raster_2_data.shape)
    
    NDVI = np.divide(raster_2_data - raster_1_data, raster_2_data + raster_1_data, where=(raster_2_data - raster_1_data)!=0)
    NDVI[NDVI == 0] = -999
    
    print(NDVI)
    
    saveRaster(NDVI, NDVI_out_path, cols, rows, projection)
    
    return NDVI

def saveRaster(dataset,datasetPath,cols,rows,projection):
    rasterSet = gdal.GetDriverByName('GTiff').Create(datasetPath, cols, rows,1,gdal.GDT_Float32)
    rasterSet.SetProjection(projection)
    rasterSet.SetGeoTransform(geotransform)
    rasterSet.GetRasterBand(1).WriteArray(dataset)
    rasterSet.GetRasterBand(1).SetNoDataValue(-999)
    rasterSet = None

def get_geotransform(img_path):
    raster = gdal.Open(img_path)
    geotransform = raster.GetGeoTransform()
    return geotransform

geotransform = get_geotransform(img_path="./Clip/2018_1_B4_clip.TIF")

NDVI_2018_1 = run(img1="./Clip/2018_1_B4_clip.TIF", img2="./Clip/2018_1_B5_clip.TIF", out="./NDVI/NDVI2018_1.tif")

NDVI_2018_2 = run(img1="./Clip/2018_2_B4_clip.TIF", img2="./Clip/2018_2_B5_clip.TIF", out="./NDVI/NDVI2018_2.tif")

NDVI_2018_3 = run(img1="./Clip/2018_3_B4_clip.TIF", img2="./Clip/2018_3_B5_clip.TIF", out="./NDVI/NDVI2018_3.tif")

NDVI_2018_4 = run(img1="./Clip/2018_4_B4_clip.TIF", img2="./Clip/2018_4_B5_clip.TIF", out="./NDVI/NDVI2018_4.tif")

NDVI_2018_5 = run(img1="./Clip/2018_5_B4_clip.TIF", img2="./Clip/2018_5_B5_clip.TIF", out="./NDVI/NDVI2018_5.tif")

NDVI_2019_1 = run(img1="./Clip/2019_1_B4_clip.TIF", img2="./Clip/2019_1_B5_clip.TIF", out="./NDVI/NDVI2019_1.tif")

NDVI_2019_2 = run(img1="./Clip/2019_2_B4_clip.TIF", img2="./Clip/2019_2_B5_clip.TIF", out="./NDVI/NDVI2019_2.tif")

NDVI_2019_3 = run(img1="./Clip/2019_3_B4_clip.TIF", img2="./Clip/2019_3_B5_clip.TIF", out="./NDVI/NDVI2019_3.tif")

NDVI_2019_4 = run(img1="./Clip/2019_4_B4_clip.TIF", img2="./Clip/2019_4_B5_clip.TIF", out="./NDVI/NDVI2019_4.tif")

NDVI_2020_1 = run(img1="./Clip/2020_1_B4_clip.TIF", img2="./Clip/2020_1_B5_clip.TIF", out="./NDVI/NDVI2020_1.tif")

NDVI_2020_2 = run(img1="./Clip/2020_2_B4_clip.TIF", img2="./Clip/2020_2_B5_clip.TIF", out="./NDVI/NDVI2020_2.tif")

NDVI_2020_3 = run(img1="./Clip/2020_3_B4_clip.TIF", img2="./Clip/2020_3_B5_clip.TIF", out="./NDVI/NDVI2020_3.tif")

NDVI_2020_4 = run(img1="./Clip/2020_4_B4_clip.TIF", img2="./Clip/2020_4_B5_clip.TIF", out="./NDVI/NDVI2020_4.tif")

from osgeo import ogr, gdal, osr
import numpy as np
import os
import matplotlib.pyplot as plt

path_NDVI_2018_1 = './NDVI/NDVI2018_1.tif'
path_NDVI_2018_2 = './NDVI/NDVI2018_2.tif'
path_NDVI_2018_3 = './NDVI/NDVI2018_3.tif'
path_NDVI_2018_4 = './NDVI/NDVI2018_4.tif'
path_NDVI_2018_5 = './NDVI/NDVI2018_5.tif'
path_NDVI_2019_1 = './NDVI/NDVI2019_1.tif'
path_NDVI_2019_2 = './NDVI/NDVI2019_2.tif'
path_NDVI_2019_3 = './NDVI/NDVI2019_3.tif'
path_NDVI_2019_4 = './NDVI/NDVI2019_4.tif'
path_NDVI_2020_1 = './NDVI/NDVI2020_1.tif'
path_NDVI_2020_2 = './NDVI/NDVI2020_2.tif'
path_NDVI_2020_3 = './NDVI/NDVI2020_3.tif'
path_NDVI_2020_4 = './NDVI/NDVI2020_4.tif'

NDVI_2018_1 = gdal.Open(path_NDVI_2018_1)
NDVI_2018_2 = gdal.Open(path_NDVI_2018_2)
NDVI_2018_3 = gdal.Open(path_NDVI_2018_3)
NDVI_2018_4 = gdal.Open(path_NDVI_2018_4)
NDVI_2018_5 = gdal.Open(path_NDVI_2018_5)
NDVI_2019_1 = gdal.Open(path_NDVI_2019_1)
NDVI_2019_2 = gdal.Open(path_NDVI_2019_2)
NDVI_2019_3 = gdal.Open(path_NDVI_2019_3)
NDVI_2019_4 = gdal.Open(path_NDVI_2019_4)
NDVI_2020_1 = gdal.Open(path_NDVI_2020_1)
NDVI_2020_2 = gdal.Open(path_NDVI_2020_2)
NDVI_2020_3 = gdal.Open(path_NDVI_2020_3)
NDVI_2020_4 = gdal.Open(path_NDVI_2020_4)

NDVI_2018_1_Data = NDVI_2018_1.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2018_2_Data = NDVI_2018_2.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2018_3_Data = NDVI_2018_3.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2018_4_Data = NDVI_2018_4.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2018_5_Data = NDVI_2018_5.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2019_1_Data = NDVI_2019_1.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2019_2_Data = NDVI_2019_2.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2019_3_Data = NDVI_2019_3.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2019_4_Data = NDVI_2019_4.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2020_1_Data = NDVI_2020_1.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2020_2_Data = NDVI_2020_2.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2020_3_Data = NDVI_2020_3.GetRasterBand(1).ReadAsArray().astype(float)
NDVI_2020_4_Data = NDVI_2020_4.GetRasterBand(1).ReadAsArray().astype(float)

#Creating cloud free composite
cloud_free_composite = np.maximum.reduce([NDVI_2018_1_Data,NDVI_2018_2_Data,NDVI_2018_3_Data,NDVI_2018_4_Data,NDVI_2018_5_Data,NDVI_2019_1_Data,NDVI_2019_2_Data,NDVI_2019_3_Data,NDVI_2019_4_Data,NDVI_2020_1_Data,NDVI_2020_2_Data,NDVI_2020_3_Data,NDVI_2020_4_Data])

cloud_free_composite

def saveRaster(dataset,datasetPath,cols,rows,projection):
    rasterSet = gdal.GetDriverByName('GTiff').Create(datasetPath, cols, rows,1,gdal.GDT_Float32)
    rasterSet.SetProjection(projection)
    rasterSet.SetGeoTransform(geotransform)
    rasterSet.GetRasterBand(1).WriteArray(dataset)
    rasterSet.GetRasterBand(1).SetNoDataValue(-999)
    rasterSet = None

#Save_Cloud_Free_Composite
cols = NDVI_2018_1.RasterXSize
rows = NDVI_2018_1.RasterYSize
projection = NDVI_2018_1.GetProjection()
geotransform = NDVI_2018_1.GetGeoTransform()
datasetPath = './Output/cloud_free_composite.tif'
saveRaster(cloud_free_composite, datasetPath, cols, rows, projection)