library(sf)
library(sp)
library(raster)
library(dplyr)
library(spData)
library(rnaturalearth)
library(tmap)  
library(osmdata)

setwd("D:/vehicle-testing/PVE-GNSS/")

#data <- read.csv('D:/vehicle-testing/PVE-GNSS/data/interim/Location_Test_GPS_GPRMC_(2021-Jul-30__12_44_45)(1)_corregido.csv')


gnss_track = st_read("D:/vehicle-testing/PVE-GNSS/data/interim/Location_Test_GPS_GPRMC_(2021-Jul-30__12_44_45)_corregido.shp")

tm_shape(gnss_track) 

plot(gnss_track[["speed_kmh"]][6:321],type="l",col="blue",lwd=3)
