library(sf)
library(sp)
library(raster)
library(dplyr)
library(spData)
library(rnaturalearth)
library(tmap)  
library(osmdata)


setwd("D:/vehicle-testing/PVE-GNSS")

colombia = ne_countries(country = "Colombia")

class(colombia)

colombia_sf = st_as_sf(colombia)


tm_shape(colombia_sf) + tm_fill()

gnss_track = st_read("D:/vehicle-testing/PVE-GNSS/data/interim/Location_Test_GPS_GPRMC_(2021-Jul-30__12_44_45)_corregido.shp")

tm_shape(gnss_track) 

plot(gnss_track["speed_kmh"])


















city_polygon <- getbb("Cali",
                      featuretype = "settlement",
                      format_out = "polygon")

# Get the rectangular bounding box
city_rect <- getbb("Cali", featuretype = "settlement")


# Get the data from OSM (might take a few seconds)
greensp_osm <-
  opq(bbox = city_polygon) %>%  # start query, input bounding box
  add_osm_feature(key = "leisure",
                  value = c("park", "nature_reserve", "golf_course")) %>%
  # we want to extract "leisure" features that are park, nature reserve or a golf course
  osmdata_sf() %>%
  # query OSM and return as simple features (sf)
  trim_osmdata(city_polygon)
# limit data to the Edinburgh polygon instead of the rectangular bounding box

greensp_osm




greensp_sf <- bind_rows(st_cast(greensp_osm$osm_polygons, "MULTIPOLYGON"),
                        greensp_osm$osm_multipolygons) %>%
  select(name, osm_id, leisure)



plot(greensp_sf["leisure"])
