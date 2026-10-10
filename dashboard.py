import streamlit as st
import pandas as pd
import sqlite3
import time

st.set_page_config(page_title='Smart City Municipal Center', layout="wide")

st.title('🏙️ IoT Municipal gateway')
st.caption('Real-Time Telemetry & Fault Detection pipeline')

conn = sqlite3.connect('telemetry.db')

def load_data():
    df = pd.read_sql_query(sql="SELECT * FROM telemetry ORDER BY id DESC LIMIT 100", con=conn)
    conn.close()
    return df

df  = load_data()

if not df.empty:
    alerts = df[df['status'] == "CRITICAL ALERT"]

    col1, col2, col3 = st.columns(3)

    col1.metric('Total telemetry log,', len(df))
    col2.metric('Active subsystems', df['node_id'].nunique())
    col3.metric('Detected anomalis', len(alerts),delta_color='orange')


    if not alerts.empty:
        st.error(f"⚠️ Active Faults Detected in {len(alerts)} telemetry packets!")
        st.dataframe(alerts[['timestamp', "node_id", "sensor_type", "value", "status"]].head(5), use_container_width=True)
    else:
        st.success('All municipal nodes operating within nominal thresholds')

    st.subheader("Raw data stream from sql database")
    selected_node = st.selectbox("Select Municipal Node to Inspect", df["node_id"].unique())
    node_data = df[df['node_id'] == selected_node].sort_values('id')

    st.line_chart(data=node_data,x="timestamp", y='value')

    st.subheader('Raw data stream from sql database')
    st.dataframe(df.head(15), use_container_width=True)

else:
    st.warning("Database empty. Start running `iot_node_simulator.py` first to generate data.")

time.sleep(1)
st.rerun()