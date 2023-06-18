
###get data from sql###
import pandas as pd
from flask import Flask,jsonify,request
from sqlalchemy import create_engine, text




engine = create_engine('postgresql://postgres:9110460311@localhost:5432/se4g') 
con = engine.connect()
app=Flask("se4g")

#get sensor information
@app.route("/api/Allsensors_data")
def AllSensors_data():
    get_sensors = pd.read_sql_table(table_name = 'sensor', con = con)
    sensors_json = get_sensors.to_json(orient="records")
    return(sensors_json)

#get sensor airquality observations data
@app.route("/api/AllAQ_data")
def AllAQdata():
    get_data = pd.read_sql_table(table_name = 'data', con = con)
    data_json = get_data.to_json(orient="records")
    return(data_json)


#get merged together(tables merged)
@app.route("/api/all_data")
def AllData():
    get_all = pd.read_sql_table(table_name = 'all_data2', con = con)
    Alldata_json = get_all.to_json(orient="records")
    return(Alldata_json)



@app.route('/api/date_filtered', methods=['POST'])
def station_filter():
    query = 'SELECT "StationName", "Average Value" FROM "all_data2"'
    data = pd.read_sql_query(sql=text(query), con=con)
    
    station_name = request.json['station_name']
    
    pollution_data = data[data['StationName'] == station_name].to_dict(orient='records')
    
    return jsonify(pollution_data)


@app.route('/api/sensor_type_filtered', methods=['POST'])
def sensor_type_filter():
    query = 'SELECT "SensorType", "SensorID" FROM "sensor"'
    data = pd.read_sql_query(sql=text(query), con=con)
    
    sensor_type = request.json['sensor_type']
    
    pollution_data = data[data['SensorType'] == sensor_type].to_dict(orient='records')
    
    return jsonify(pollution_data)


@app.route('/api/comune_filtered', methods=['POST'])
def comune_filter():
    query = 'SELECT "Comune", "SensorID" ,"SensorType"   FROM "sensor"'
    data = pd.read_sql_query(sql=text(query), con=con)
    
    comune = request.json['comune']
    
    pollution_data = data[data['Comune'] == comune].to_dict(orient='records')
    
    return jsonify(pollution_data)
    
@app.route('/api/province_filtered', methods=['POST'])
def province_filter():
    query = 'SELECT "Province", "SensorID" ,"Comune", "SensorType"   FROM "sensor"'
    data = pd.read_sql_query(sql=text(query), con=con)
    
    province = request.json['Province']

    pollution_data = data[data['Province'] == province].to_dict(orient='records')
    
    return jsonify(pollution_data)


    

print("Code execution finished.")

app.run(port=5005)
