import sqlite3
import time
import random
from datetime import datetime



def init_conn():
    conn = sqlite3.connect('telemetry.db')

    command = """ create table if not exists telemetry(
        id integer primary key autoincrement,
        timestamp text not null,
        node_id text not null,
        sensor_type text not null,
        value real not null,
        status text not null
    )

"""
    cursor = conn.cursor()
    cursor.execute(command)
    conn.commit()
    conn.close()


def generate_telemetry_data():
    nodes = [
        {'id':"STREET1_power", 'type':"VOLTAGE_VAC", 'normal_range': (218, 232), 'unit': 'V'},
        {'id': 'MAIN_WATER_LINE', 'type': 'Water_Pressure_Bar', 'normal_range': (3.5, 5), 'unit':'bar'},
        {'id': 'SMART_LIGHT', 'type':"Power_Consumption_kw", 'normal_range': (10, 45), 'unit':'kw'},
        {'id': 'CENTRAL_PARK_AIR', "type": "PM2_5_PPM", "normal_range": (12,35), 'unit': 'ppm'}
    ]

    print('Start simulation of data flow')
    conn = sqlite3.connect('telemetry.db')
    cursor = conn.cursor()

    while True:
        for node in nodes:
            is_anomaly = random.random() < 0.05

            if is_anomaly:
                val = node['normal_range'][1] * random.uniform(1.3, 1.8)
                status = "CRITICAL ALERT"
            else: 
                val = random.uniform(node['normal_range'][0], node['normal_range'][1])
                status = "OPTIMAL"

            now  = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
            
            cursor.execute("""
                insert into telemetry(timestamp, node_id, sensor_type, value, status)
                values(?, ?, ?, ?, ?)""", (now, node['id'], node['type'], round(val, 2), status))

            conn.commit()

            print(now, node['id'], node['type'], round(val, 2), status)
        time.sleep(2)



init_conn()
generate_telemetry_data()
# if __name__ == "__main__":
#     init_conn()
#     generate_telemetry_data()
