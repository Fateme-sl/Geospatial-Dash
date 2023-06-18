##Data Base
###read excel files of data###
import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine, text
import psycopg2
import geoalchemy2


data=pd.read_excel(r"D:\E\Polimi\SE4GE\Project\data_Copy\Data.xls")
sensor=pd.read_excel(r"D:\E\Polimi\SE4GE\Project\data_Copy\Sensors.xls")



###create a connection to DataBase in SQL###


engine = create_engine('postgresql://postgres:9110460311@localhost:5432/se4g') 
con = engine.connect()
#save data to sql
sensor.to_sql('sensor', engine, if_exists = 'replace', index=False)
data.to_sql('data', engine, if_exists = 'replace', index=False)
# Read tables to join
sensor_df = pd.read_sql_table('sensor', con)
data_df = pd.read_sql_table('data', con)
# Merge the DataFrames based on the "SensorID" column
all_data_df = pd.merge(sensor_df, data_df, on='SensorID')
all_data_df.to_sql('all_data2', engine, if_exists = 'replace' , index=False)

print("Code execution finished.")
