# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# liberias
import os
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# lectura de datos
gnss_data = pd.read_csv(r"D:\vehicle-testing\PVE-GNSS\data\interim\Location_Test_GPS_GPRMC_(2021-Jul-30__12_44_45)(1).csv")

# correccion formato de latitud y longitud
gnss_data['lat'] = gnss_data.loc[:,'latitude']/100
gnss_data['lon']  = (gnss_data.loc[:,'longitude']* -1)/100


# formateado de fecha

fecha_formateada = []

for i in gnss_data.index:
    date_time_string = str(gnss_data['date_stamp'][i])[:2] + str(gnss_data['date_stamp'][i])[2:4] +'20' + str(gnss_data['date_stamp'][i])[4:6] + str(gnss_data['time_stamp'][i])[:2]+ str(gnss_data['time_stamp'][i])[2:4]+ str(gnss_data['time_stamp'][i])[4:6]
    date_time = datetime.datetime.strptime(date_time_string, '%d%m%Y%H%M%S')
    fecha_formateada.append(date_time)
    
gnss_data['date'] =  fecha_formateada



# grafico

plt.plot(gnss_data['date'][6:],gnss_data['speed_kmh'][6:])
plt.title("Comportamiento de la velocidad en el Tiempo")
plt.xticks(rotation=90)
plt.ylabel("Velocidad en km/h")
plt.xlabel("Tiempo")
plt.savefig(r"D:\vehicle-testing\PVE-GNSS\reports\figures\velocity_vs_time.png")


#gnss_data.to_csv(r"D:\vehicle-testing\PVE-GNSS\data\interim\Location_Test_GPS_GPRMC_(2021-Jul-30__12_44_45)(1)_corregido.csv")