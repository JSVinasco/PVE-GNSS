# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import os
import pandas as pd

gnss_data = pd.read_csv(r"D:\vehicle-testing\Location_Test_GPS_GPRMC_(2021-Jul-30__12_44_45)(1).csv")

gnss_data['lat'] = gnss_data.loc[:,'latitude']/100

gnss_data['lon']  = (gnss_data.loc[:,'longitude']* -1)/100

gnss_data.to_csv(r"D:\vehicle-testing\Location_Test_GPS_GPRMC_(2021-Jul-30__12_44_45)(1)_corregido.csv")