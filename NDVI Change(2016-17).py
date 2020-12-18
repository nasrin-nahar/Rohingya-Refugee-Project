#!/usr/bin/env python
# coding: utf-8

# In[6]:


#author: Nasrin Nahar
#version: 1.0
#last access: 2:26 AM 4/30/20
#library imports

from osgeo import ogr, gdal, osr
import numpy as np
import os
import matplotlib.pyplot as plt


# In[2]:


#Image-2017
path_B5_2017="./Image2017clip/2017B5.TIF"
path_B4_2017="./Image2017clip/2017B4.TIF"

#Image-2016
path_B5_2016="./Image2016clip/2016B5.TIF"
path_B4_2016="./Image2016clip/2016B4.TIF"


# In[4]:


#Output Files

#Output NDVI Rasters 
path_NDVI_2017 = './Output/NDVI2017.tif'
path_NDVI_2016 = './Output/NDVI2016.tif'
path_NDVIChange ='./Output/NDVIChange.tif'
#NDVI Contours
contours_NDVIChange ='./Output/NDVIChange.shp'


# In[8]:


#Open raster bands
B5_2017 = gdal.Open(path_B5_2017)
B4_2017 = gdal.Open(path_B4_2017)
B5_2016 = gdal.Open(path_B5_2016)
B4_2016 = gdal.Open(path_B4_2016)


# In[10]:


#Read bands as matrix arrays
B52017_Data = B5_2017.GetRasterBand(1).ReadAsArray().astype(np.float32)
B42017_Data = B4_2017.GetRasterBand(1).ReadAsArray().astype(np.float32)
B52016_Data = B5_2016.GetRasterBand(1).ReadAsArray().astype(np.float32)
B42016_Data = B4_2016.GetRasterBand(1).ReadAsArray().astype(np.float32)


# In[11]:


print(B5_2017.GetProjection()[:80])
print(B5_2016.GetProjection()[:80])
if B5_2017.GetProjection()[:80]==B5_2016.GetProjection()[:80]: print('SRC OK')


# In[12]:


print(B52017_Data.shape)
print(B52016_Data.shape)
if B52017_Data.shape==B52016_Data.shape: print('Array Size OK')


# In[13]:


print(B5_2017.GetGeoTransform())
print(B5_2016.GetGeoTransform())
if B5_2017.GetGeoTransform()==B5_2016.GetGeoTransform(): print('Geotransformation OK')


# In[15]:


geotransform = B5_2017.GetGeoTransform()

originX,pixelWidth,empty,finalY,empty2,pixelHeight=geotransform
cols =  B5_2017.RasterXSize
rows =  B5_2017.RasterYSize


# In[16]:


projection = B5_2017.GetProjection()

finalX = originX + pixelWidth * cols
originY = finalY + pixelHeight * rows


# In[22]:


#Calculate_NDVI_2016
ndvi2016 = np.divide(B52016_Data - B42016_Data, B52016_Data+ B42016_Data,where=(B52016_Data - B42016_Data)!=0)
ndvi2016[ndvi2016 == 0] = -999


# In[23]:


#Calculate_NDVI_2017
ndvi2017 = np.divide(B52017_Data - B42017_Data, B52017_Data+ B42017_Data,where=(B52017_Data - B42017_Data)!=0)
ndvi2017[ndvi2017 == 0] = -999


# In[24]:


def saveRaster(dataset,datasetPath,cols,rows,projection):
    rasterSet = gdal.GetDriverByName('GTiff').Create(datasetPath, cols, rows,1,gdal.GDT_Float32)
    rasterSet.SetProjection(projection)
    rasterSet.SetGeoTransform(geotransform)
    rasterSet.GetRasterBand(1).WriteArray(dataset)
    rasterSet.GetRasterBand(1).SetNoDataValue(-999)
    rasterSet = None


# In[26]:


saveRaster(ndvi2016,path_NDVI_2016,cols,rows,projection)

saveRaster(ndvi2017,path_NDVI_2017,cols,rows,projection)


# In[31]:


#Plot_NDVI
extentArray = [originX,finalX,originY,finalY]
def plotNDVI(ndviImage,extentArray,vmin,cmap):
    ndvi = gdal.Open(ndviImage)
    ds2019 = ndvi.ReadAsArray()
    plt.figure(figsize=(20,15))
    im = plt.imshow(ds2019, vmin=vmin, cmap=cmap, extent=extentArray)#
    plt.colorbar(im, fraction=0.015)
    plt.xlabel('Este')
    plt.ylabel('Norte')
    plt.show()
plotNDVI(path_NDVI_2016,extentArray,0,'YlGn')


# In[32]:


plotNDVI(path_NDVI_2017,extentArray,0,'YlGn')


# In[36]:


#NDVI_Change
ndviChange = ndvi2017-ndvi2016
ndviChange = np.where((ndvi2016>-999) & (ndvi2017>-999),ndviChange,-999)
ndviChange


# In[40]:


#Save_NDVI_Change
saveRaster(ndviChange,path_NDVIChange,cols,rows,projection)


# In[41]:


#Plot_NDVI_Change
plotNDVI(path_NDVIChange,extentArray,-0.5,'Spectral')


# In[43]:


#Create Contourlines
Dataset_ndvi = gdal.Open(path_NDVIChange)#path_NDVI_2014
ndvi_raster = Dataset_ndvi.GetRasterBand(1)

ogr_ds = ogr.GetDriverByName("ESRI Shapefile").CreateDataSource(contours_NDVIChange)

prj=Dataset_ndvi.GetProjectionRef()#GetProjection()

srs = osr.SpatialReference(wkt=prj)#
#srs.ImportFromProj4(prj)

contour_shp = ogr_ds.CreateLayer('contour', srs)
field_defn = ogr.FieldDefn("ID", ogr.OFTInteger)
contour_shp.CreateField(field_defn)
field_defn = ogr.FieldDefn("ndviChange", ogr.OFTReal)
contour_shp.CreateField(field_defn)
#Generate Contourlines
gdal.ContourGenerate(ndvi_raster, 0.1, 0, [], 1, -999, contour_shp, 0, 1)
ogr_ds = None

