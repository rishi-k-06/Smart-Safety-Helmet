import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="Worker Safety HQ", page_icon="⛑️", layout="wide")

st.title("⛑️ Industrial Safety Monitoring Dashboard")

if 'safety_events' not in st.session_state:
    st.session_state.safety_events = pd.DataFrame(columns=['Time', 'G_Force', 'Status'])

placeholder = st.empty()

for _ in range(100):
    # Simulating G-Force data from Nano 33 IoT
    g_force = round(np.random.uniform(0.9, 1.1), 2)
    status = "Active"
    
    # Simulate a Fall Event
    if _ == 40:
        g_force = 4.5
        status = "FALL DETECTED"

    new_event = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), g_force, status]], 
                             columns=st.session_state.safety_events.columns)
    st.session_state.safety_events = pd.concat([st.session_state.safety_events, new_event]).tail(10)

    with placeholder.container():
        c1, c2 = st.columns([1, 2])
        
        with c1:
            if status == "FALL DETECTED":
                st.error("🚨 EMERGENCY: MAN DOWN DETECTED!")
                st.button("Dispatch Medical Aid")
            else:
                st.success("✅ Worker Status: Normal")
            
            st.metric("Live Impact Force", f"{g_force} G")

        with c2:
            fig = go.Figure(go.Scatter(x=st.session_state.safety_events['Time'], 
                                       y=st.session_state.safety_events['G_Force'],
                                       mode='lines+markers', line_color='red'))
            fig.update_layout(title="Impact Force Timeline (G)", yaxis_range=[0, 6])
            st.plotly_chart(fig, use_container_width=True)

    time.sleep(1)
