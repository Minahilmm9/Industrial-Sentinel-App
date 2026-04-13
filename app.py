import streamlit as st
import time
import joblib
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

st.set_page_config(
    page_title="Industrial Sentinel",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "current_page" not in st.session_state:
    st.session_state.current_page = "login"

def render_login():
    
    # Set up page config
    
    # Custom Styling to match Tailwind 'Industrial Sentinel' theme
    st.markdown("""
        <style>
            /* Base surface */
            .stApp {
                background-color: #060e20;
                background-image: radial-gradient(circle at 2px 2px, rgba(58, 223, 250, 0.05) 1px, transparent 0);
                background-size: 40px 40px;
                color: #dee5ff;
                font-family: 'Inter', sans-serif;
            }
    
            /* Hide Streamlit Header */
            header { visibility: hidden; }
    
            /* Hide Sidebar Toggle */
            [data-testid="collapsedControl"] { display: none; }
    
            /* Glass Panel Container */
            .main [data-testid="block-container"] {
                padding: 2rem 1rem;
                max-width: 500px;
                margin: auto;
            }
    
            /* Forms / Inputs */
            div[data-baseweb="input"] {
                background-color: transparent !important;
                border: none !important;
                border-bottom: 1px solid rgba(109, 117, 140, 0.4) !important;
                border-radius: 0 !important;
                color: #dee5ff !important;
            }
            div[data-baseweb="input"] input {
                color: #dee5ff !important;
                font-family: 'Inter', sans-serif;
                font-size: 16px;
            }
            div[data-baseweb="input"]:focus-within {
                border-bottom: 1px solid #3adffa !important;
            }
            
            /* Labels */
            .stTextInput label p {
                font-family: 'Space Grotesk', sans-serif;
                font-size: 10px;
                text-transform: uppercase;
                letter-spacing: 0.1em;
                color: #a3aac4;
            }
    
            /* Button */
            button[data-testid="baseButton-secondary"] {
                background: linear-gradient(to bottom right, #3adffa, #00cbe6) !important;
                color: #003d46 !important;
                border: none;
                border-radius: 4px;
                font-family: 'Space Grotesk', sans-serif;
                font-weight: 700;
                padding: 1rem;
                width: 100%;
                height: 50px;
                margin-top: 2rem;
                letter-spacing: 0.05em;
                transition: all 0.2s ease-in-out;
                box-shadow: 0 0 20px rgba(58,223,250,0.3);
            }
            button[data-testid="baseButton-secondary"]:hover {
                transform: scale(0.98);
                filter: brightness(1.2);
            }
    
            /* Titles and Headers */
            h1, h2, h3 {
                font-family: 'Space Grotesk', sans-serif !important;
                text-align: center;
            }
            
            .header-title {
                color: #dee5ff;
                font-size: 24px;
                font-weight: 700;
                margin-bottom: 5px;
                text-align: center;
            }
            
            .header-subtitle {
                color: #a3aac4;
                font-size: 10px;
                text-transform: uppercase;
                letter-spacing: 0.2em;
                text-align: center;
                margin-bottom: 40px;
            }
            
            .glass-card {
                background-color: rgba(25, 37, 64, 0.6);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(64, 72, 93, 0.2);
                border-radius: 8px;
                padding: 30px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.3);
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Main UI
    st.markdown("""
    <div class="header-title">Industrial Sentinel</div>
    <div class="header-subtitle">Node Authorization Protocol</div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2>Machine Failure Prediction System</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#a3aac4; font-size:14px;'>Enter secure credentials to access system telemetry.</p>", unsafe_allow_html=True)
    
    # Fake Login Form
    email = st.text_input("Operator Email", placeholder="operator@sentinel.ai")
    password = st.text_input("Access Code", placeholder="••••••••", type="password")
    
    if st.button("INITIALIZE SESSION"):
        if email == "" or password == "":
            st.error("Please enter credentials.")
        else:
            with st.spinner("Authenticating Node..."):
                time.sleep(1)
                st.session_state.current_page = "dashboard"; st.rerun()
    
    st.markdown("""
    <div style="margin-top:20px; text-align:center; font-size:10px; color:#6dfe9c; letter-spacing:0.1em;">
        <span style="display:inline-block; width:6px; height:6px; background-color:#6dfe9c; border-radius:50%; margin-right:5px; box-shadow:0 0 8px #6dfe9c;"></span>
        GLOBAL STATUS: ALL NODES ACTIVE
    </div>
    """, unsafe_allow_html=True)
    
    

def render_dashboard():
    
    
    # Custom Styling
    st.markdown("""
        <style>
            .stApp {
                background-color: #060e20;
                color: #dee5ff;
                font-family: 'Inter', sans-serif;
            }
            [data-testid="collapsedControl"] { display: none; }
            header { visibility: hidden; }
            
            /* Glass effect cards */
            div[data-testid="stVerticalBlock"] > div > div[data-testid="stVerticalBlock"] {
                background-color: rgba(25, 37, 64, 0.6);
                border: 1px solid rgba(109, 117, 140, 0.2);
                border-radius: 8px;
                padding: 1.5rem;
                backdrop-filter: blur(10px);
            }
            
            .metric-label {
                font-family: 'Space Grotesk', sans-serif;
                font-size: 12px;
                color: #a3aac4;
                text-transform: uppercase;
                letter-spacing: 0.1em;
                margin-bottom: -10px;
            }
            .metric-value {
                font-family: 'Space Grotesk', sans-serif;
                font-size: 36px;
                font-weight: bold;
                color: #dee5ff;
            }
            .metric-value.critical { color: #ff716c; text-shadow: 0 0 10px rgba(255,113,108,0.3); }
            .metric-value.nominal { color: #6dfe9c; text-shadow: 0 0 10px rgba(109,254,156,0.3); }
            
            h1, h2, h3 { font-family: 'Space Grotesk', sans-serif; }
        </style>
    """, unsafe_allow_html=True)
    
    # Load Models
    @st.cache_resource
    def load_models():
        try:
            knn = joblib.load('knn_model.pkl')
            scaler = joblib.load('scaler.pkl')
            le = joblib.load('label_encoder.pkl')
            feature_names = joblib.load('feature_names.pkl')
            return knn, scaler, le, feature_names
        except Exception as e:
            return None, None, None, None
    
    knn, scaler, le, feature_names = load_models()
    
    # Top Bar
    st.markdown("""
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(109,117,140,0.2); padding-bottom:1rem; margin-bottom:2rem;">
        <h2 style="color:#3adffa; margin:0; font-size:24px; text-transform:uppercase;">Industrial Sentinel // Dashboard</h2>
        <div style="color:#6dfe9c; font-size:12px; font-family:'Space Grotesk'; letter-spacing:0.1em;">
            <span style="display:inline-block; width:8px; height:8px; background-color:#6dfe9c; border-radius:50%; margin-right:5px; box-shadow:0 0 8px #6dfe9c;"></span>
            SYSTEM ONLINE
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if not knn:
        st.error("Models not found. Please wait for the initial training to complete.")
        st.stop()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Primary Diagnostics")
        
        # We create inputs that look like sensor readings
        cols = st.columns(3)
        with cols[0]:
            air_temp = st.slider("Air Temp [K]", min_value=290.0, max_value=310.0, value=298.1)
            proc_temp = st.slider("Process Temp [K]", min_value=300.0, max_value=320.0, value=308.6)
        with cols[1]:
            rot_speed = st.slider("Rot speed [rpm]", min_value=1100, max_value=3000, value=1500)
            torque = st.slider("Torque [Nm]", min_value=0.0, max_value=80.0, value=40.0)
        with cols[2]:
            tool_wear = st.slider("Tool wear [min]", min_value=0, max_value=300, value=10)
            m_type = st.selectbox("Machine Type", ["L", "M", "H"])
    
        # Hidden failure flags (we assume 0 for manual prediction testing to see baseline failure)
        twf = 0; hdf = 0; pwf = 0; osf = 0; rnf = 0
        
        # If the user slides values out of bounds, we might simulate TWF, HDF, etc.
        if tool_wear > 200: twf = 1
        if rot_speed < 1300 and torque > 60: pwf = 1
        if (proc_temp - air_temp) > 10 and rot_speed < 1300: hdf = 1
        if torque * rot_speed > 100000 and tool_wear > 200: osf = 1
    
        # Prepare input
        type_encoded = le.transform([m_type])[0]
        input_df = pd.DataFrame([{
            'Type': type_encoded,
            'Air temperature [K]': air_temp,
            'Process temperature [K]': proc_temp,
            'Rotational speed [rpm]': rot_speed,
            'Torque [Nm]': torque,
            'Tool wear [min]': tool_wear,
            'TWF': twf, 'HDF': hdf, 'PWF': pwf, 'OSF': osf, 'RNF': rnf
        }])
        
        # Ensure column order matches training
        input_df = input_df[feature_names]
        
        # Predict
        input_scaled = scaler.transform(input_df)
        pred = knn.predict(input_scaled)[0]
        prob = knn.predict_proba(input_scaled)[0]
        
        # Calculate a responsive risk score so the UI feels alive
        base_risk = (tool_wear / 300.0) * 15 + (torque / 80.0) * 10 
        fail_prob = prob[1] * 100 + base_risk
        if pred == 1 and fail_prob < 50:
            fail_prob += 50
        if fail_prob > 99.9: fail_prob = 99.9
    
    with col2:
        st.markdown("### Machine State")
        state_str = "CRITICAL" if pred == 1 else "NOMINAL"
        state_class = "critical" if pred == 1 else "nominal"
        prob_color = "critical" if fail_prob > 50 else "nominal"
        
        st.markdown(f"""
        <div style="background-color:rgba(0,0,0,0.2); padding:2rem; border-radius:8px; text-align:center; border: 1px solid {'#ff716c' if pred==1 else '#6dfe9c'}">
            <div class="metric-label">Failure Probability</div>
            <div class="metric-value {prob_color}">{fail_prob:.1f}%</div>
            <div style="margin-top:1rem; font-family:'Space Grotesk'; color:{'#ff716c' if pred==1 else '#6dfe9c'}; font-weight:bold; letter-spacing:2px;">
                STATUS: {state_str}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
            <div>
                <div class="metric-label">Remaining Life</div>
                <div class="metric-value" style="font-size:20px;">14.2 HRS</div>
            </div>
            <div>
                <div class="metric-label">AI Confidence</div>
                <div class="metric-value" style="font-size:20px;">99.2%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Navigation Footer
    st.markdown("""
    <div style="position:fixed; bottom:0; left:0; width:100%; height:50px; background:#060e20; border-top:1px solid rgba(109,117,140,0.2); display:flex; padding:0 2rem; align-items:center;">
        <span style="color:#a3aac4; font-size:10px; font-family:'Space Grotesk'; letter-spacing:0.1em;">v2.4.0-Stable</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Add navigation buttons at the bottom
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        if st.button("Go to Live Sensors"):
            st.session_state.current_page = "sensors"; st.rerun()
    with col_nav2:
        if st.button("Go to Alerts"):
            st.session_state.current_page = "alerts"; st.rerun()
    

def render_sensors():
    
    
    st.markdown("""
        <style>
            .stApp {
                background-color: #060e20;
                background-image: radial-gradient(circle at 10% 20%, rgba(58, 223, 250, 0.03) 0%, transparent 40%);
                color: #dee5ff;
                font-family: 'Inter', sans-serif;
            }
            [data-testid="collapsedControl"] { display: none; }
            header { visibility: hidden; }
            
            .metric-title {
                color: #3adffa;
                font-size: 10px;
                font-family: 'Space Grotesk';
                letter-spacing: 0.15em;
                text-transform: uppercase;
            }
            .metric-value {
                font-size: 32px;
                font-weight: bold;
                font-family: 'Space Grotesk';
                color: #dee5ff;
            }
            
            /* Layout overrides */
            .glass-panel {
                background: rgba(16, 25, 46, 0.7);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(58, 223, 250, 0.1);
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 20px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
            }
            
            .log-table {
                width:100%; 
                text-align:left; 
                border-collapse:collapse; 
                font-size:13px;
            }
            .log-table th {
                padding:12px;
                color:#a3aac4;
                font-family:'Space Grotesk', sans-serif;
                letter-spacing: 0.1em;
                font-weight: 600;
                border-bottom:1px solid rgba(58,223,250,0.2);
            }
            .log-table td {
                padding: 14px 12px;
                transition: all 0.2s ease;
            }
            .log-table tr {
                border-bottom: 1px solid rgba(109,117,140,0.1);
            }
            .log-table tr:hover td {
                background: rgba(58,223,250,0.05);
            }
            
            div[data-testid="stButton"] button {
                background: transparent !important;
                color: #3adffa !important;
                border: 1px solid rgba(58,223,250,0.4) !important;
                border-radius: 6px !important;
                font-family: 'Space Grotesk', sans-serif !important;
                font-weight: 600 !important;
                letter-spacing: 0.05em !important;
                transition: all 0.3s ease !important;
            }
            div[data-testid="stButton"] button:hover {
                background: rgba(58,223,250,0.1) !important;
                border-color: #3adffa !important;
                color: #fff !important;
                box-shadow: 0 0 15px rgba(58,223,250,0.3) !important;
                transform: translateY(-2px) !important;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="border-bottom:1px solid rgba(58,223,250,0.2); padding-bottom:10px; margin-bottom:20px; display:flex; align-items:flex-end;">
        <div>
            <span style="color:#3adffa; font-size:10px; letter-spacing:0.3em; font-family:'Space Grotesk'; font-weight:700;">REAL-TIME TELEMETRY</span>
            <h2 style="margin:0; font-family:'Space Grotesk'; font-size:32px; font-weight:700; background:linear-gradient(90deg, #fff, #a3aac4); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Live Sensor Monitoring</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<div class="metric-title">Thermal Load</div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-value">78.4° <span style="font-size:12px; color:#6dfe9c; font-family:Inter; font-weight:normal;">+2.4% vs baseline</span></div>', unsafe_allow_html=True)
        
        # Generate some sine wave data for thermal load
        x = np.linspace(0, 100, 100)
        y = np.sin(x/5) * 5 + 75 + np.random.normal(0, 1, 100)
        df_temp = pd.DataFrame(y, columns=["Temperature"])
        st.line_chart(df_temp, color="#3adffa", height=200)
        st.markdown('</div>', unsafe_allow_html=True)
        
        col1a, col1b = st.columns(2)
        with col1a:
            st.markdown('<div class="glass-panel"><div class="metric-title" style="color:#6dfe9c;">Hydrostatic Pressure</div><div class="metric-value">412.8 <span style="font-size:12px; color:#a3aac4;">PSI</span></div>', unsafe_allow_html=True)
            y_pres = np.random.normal(410, 5, 50)
            st.line_chart(pd.DataFrame(y_pres, columns=["Pressure"]), color="#6dfe9c", height=150)
            st.markdown('</div>', unsafe_allow_html=True)
        with col1b:
            st.markdown('<div class="glass-panel"><div class="metric-title" style="color:#ffe083;">Acoustic Vibration</div><div class="metric-value">0.024 <span style="font-size:12px; color:#a3aac4;">G-RMS</span></div>', unsafe_allow_html=True)
            y_vib = np.random.normal(0.02, 0.005, 50)
            st.line_chart(pd.DataFrame(y_vib, columns=["Vibration"]), color="#ffe083", height=150)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-panel" style="height:100%;">', unsafe_allow_html=True)
        st.markdown('<div class="metric-title" style="color:#ffe083; margin-bottom:20px;">AI Prediction Engine</div>', unsafe_allow_html=True)
        
        st.markdown("""
            <div style="margin-bottom:24px;">
                <div style="display:flex; justify-content:space-between; font-size:11px; color:#a3aac4; font-family:'Space Grotesk'; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">
                    <span>Failure Probability</span><span style="color:#6dfe9c;">Low</span>
                </div>
                <div style="height:6px; background:rgba(25,37,64,0.8); border-radius:3px; overflow:hidden;">
                    <div style="height:100%; width:12%; background:linear-gradient(90deg, #3adffa, #6dfe9c); box-shadow:0 0 10px rgba(109,254,156,0.5);"></div>
                </div>
            </div>
            
            <div style="margin-bottom:32px;">
                <div style="display:flex; justify-content:space-between; font-size:11px; color:#a3aac4; font-family:'Space Grotesk'; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">
                    <span>Engine Confidence</span><span style="color:#dee5ff;">98.2%</span>
                </div>
                <div style="height:6px; background:rgba(25,37,64,0.8); border-radius:3px; overflow:hidden;">
                    <div style="height:100%; width:98%; background:linear-gradient(90deg, #3adffa, #00cbe6); box-shadow:0 0 10px rgba(58,223,250,0.5);"></div>
                </div>
            </div>
            
            <div style="background:rgba(58,223,250,0.05); padding:18px; border-left:3px solid #3adffa; border-radius:0 8px 8px 0; font-size:11px; color:#a3aac4; font-family:'Space Grotesk'; letter-spacing:0.15em; line-height:1.6;">
                CURRENT TREND INDICATES STABLE OPERATION. NEXT PREDICTIVE MAINTENANCE WINDOW: <span style="color:#dee5ff; font-weight:bold;">420 HOURS</span>.
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Generate dynamic times for logs
    now = datetime.now()
    t1 = (now - timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
    t2 = (now - timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
    t3 = (now - timedelta(minutes=12)).strftime("%Y-%m-%d %H:%M:%S")
    
    # Fake Logs Table
    st.markdown(f"""
    <div class="glass-panel" style="margin-top:0;">
    <div style="color:#dee5ff; font-family:'Space Grotesk'; font-size:14px; font-weight:700; letter-spacing:0.1em; margin-bottom:15px; text-transform:uppercase;">System Event Logs</div>
    <table class="log-table">
    <tr>
    <th>TIMESTAMP</th>
    <th>COMPONENT</th>
    <th>EVENT</th>
    <th>STATUS</th>
    </tr>
    <tr>
    <td style="color:#8b99ad; font-family:'Space Grotesk', monospace;">{t1}</td>
    <td style="color:#dee5ff;">Turbine Alpha-4</td>
    <td style="color:#dee5ff;">Periodic Sync Check</td>
    <td style="color:#6dfe9c; font-family:'Space Grotesk'; font-weight:700; font-size:11px; letter-spacing:0.1em;">NOMINAL</td>
    </tr>
    <tr>
    <td style="color:#8b99ad; font-family:'Space Grotesk', monospace;">{t2}</td>
    <td style="color:#dee5ff;">Coolant Loop 2</td>
    <td style="color:#dee5ff;">Pressure Fluctuation</td>
    <td style="color:#ffe083; font-family:'Space Grotesk'; font-weight:700; font-size:11px; letter-spacing:0.1em;">ADVISORY</td>
    </tr>
    <tr>
    <td style="color:#8b99ad; font-family:'Space Grotesk', monospace;">{t3}</td>
    <td style="color:#dee5ff;">Bearing S-82</td>
    <td style="color:#dee5ff;">Thermal Spike Detected</td>
    <td style="color:#ff716c; font-family:'Space Grotesk'; font-weight:700; font-size:11px; letter-spacing:0.1em;">WARNING</td>
    </tr>
    </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        if st.button("← Back to Dashboard"):
            st.session_state.current_page = "dashboard"; st.rerun()
    with col_nav2:
        if st.button("Go to Alerts →"):
            st.session_state.current_page = "alerts"; st.rerun()
    
    

def render_alerts():
    
    
    # Generate dynamic recent timestamps
    now = datetime.now()
    times = [
        (now - timedelta(minutes=random.randint(1, 10))).strftime("%Y-%m-%d %H:%M:%S"),
        (now - timedelta(minutes=random.randint(15, 30))).strftime("%Y-%m-%d %H:%M:%S"),
        (now - timedelta(hours=1, minutes=random.randint(0, 30))).strftime("%Y-%m-%d %H:%M:%S"),
        (now - timedelta(hours=2, minutes=random.randint(0, 45))).strftime("%Y-%m-%d %H:%M:%S"),
    ]
    
    st.markdown("""
        <style>
            .stApp {
                background-color: #060e20;
                background-image: 
                    radial-gradient(circle at 15% 50%, rgba(58, 223, 250, 0.04) 0%, transparent 50%),
                    radial-gradient(circle at 85% 30%, rgba(255, 113, 108, 0.04) 0%, transparent 50%);
                color: #dee5ff;
                font-family: 'Inter', sans-serif;
            }
            [data-testid="collapsedControl"] { display: none; }
            header { visibility: hidden; }
            
            .alert-card {
                background: rgba(16, 25, 46, 0.7);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(58, 223, 250, 0.1);
                border-radius: 12px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
            }
            
            .alert-row {
                display: flex;
                align-items: center;
                padding: 18px 24px;
                border-left: 4px solid transparent;
                border-bottom: 1px solid rgba(109,117,140,0.1);
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                cursor: pointer;
                background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0) 100%);
            }
            .alert-row:last-child {
                border-bottom: none;
            }
            .alert-row:hover { 
                transform: translateX(4px);
            }
            
            .alert-row.critical { 
                border-left-color: #ff716c; 
            }
            .alert-row.critical:hover {
                background: linear-gradient(90deg, rgba(255,113,108,0.1) 0%, rgba(255,113,108,0) 100%);
                box-shadow: inset 2px 0 10px rgba(255,113,108,0.1);
            }
            
            .alert-row.warning { 
                border-left-color: #ffe083; 
            }
            .alert-row.warning:hover {
                background: linear-gradient(90deg, rgba(255,224,131,0.1) 0%, rgba(255,224,131,0) 100%);
                box-shadow: inset 2px 0 10px rgba(255,224,131,0.1);
            }
            
            .alert-row.info { 
                border-left-color: #3adffa; 
            }
            .alert-row.info:hover {
                background: linear-gradient(90deg, rgba(58,223,250,0.1) 0%, rgba(58,223,250,0) 100%);
                box-shadow: inset 2px 0 10px rgba(58,223,250,0.1);
            }
            
            .alert-time { 
                width: 170px; 
                font-family: 'Space Grotesk', monospace; 
                color: #8b99ad; 
                font-size: 13px; 
                letter-spacing: 0.05em;
            }
            
            .badge-container {
                width: 120px;
            }
            
            .alert-badge {
                font-size: 11px;
                font-family: 'Space Grotesk', sans-serif;
                font-weight: 700;
                letter-spacing: 0.15em;
                padding: 4px 8px;
                border-radius: 4px;
                display: inline-flex;
                align-items: center;
                gap: 6px;
                text-transform: uppercase;
            }
            
            .alert-badge::before {
                content: '';
                display: inline-block;
                width: 6px;
                height: 6px;
                border-radius: 50%;
            }
            
            .badge-critical { 
                color: #ff716c; 
                background: rgba(255,113,108,0.1);
                border: 1px solid rgba(255,113,108,0.2);
            }
            .badge-critical::before {
                background-color: #ff716c;
                box-shadow: 0 0 8px #ff716c;
                animation: pulse-crit 1.5s infinite;
            }
            
            .badge-warning { 
                color: #ffe083; 
                background: rgba(255,224,131,0.1);
                border: 1px solid rgba(255,224,131,0.2);
            }
            .badge-warning::before {
                background-color: #ffe083;
                box-shadow: 0 0 8px #ffe083;
            }
            
            .badge-info { 
                color: #3adffa; 
                background: rgba(58,223,250,0.1);
                border: 1px solid rgba(58,223,250,0.2);
            }
            .badge-info::before {
                background-color: #3adffa;
                box-shadow: 0 0 8px #3adffa;
            }
            
            @keyframes pulse-crit {
                0% { opacity: 1; transform: scale(1); }
                50% { opacity: 0.5; transform: scale(1.5); }
                100% { opacity: 1; transform: scale(1); }
            }
            
            .alert-desc { 
                flex-grow: 1; 
                font-size: 15px; 
                color: #dee5ff; 
                font-weight: 400;
                letter-spacing: 0.02em;
            }
            
            div[data-testid="stButton"] button {
                background: transparent !important;
                color: #3adffa !important;
                border: 1px solid rgba(58,223,250,0.4) !important;
                border-radius: 6px !important;
                font-family: 'Space Grotesk', sans-serif !important;
                font-weight: 600 !important;
                letter-spacing: 0.05em !important;
                transition: all 0.3s ease !important;
            }
            div[data-testid="stButton"] button:hover {
                background: rgba(58,223,250,0.1) !important;
                border-color: #3adffa !important;
                color: #fff !important;
                box-shadow: 0 0 15px rgba(58,223,250,0.3) !important;
                transform: translateY(-2px) !important;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-bottom:40px; display:flex; justify-content:space-between; align-items:flex-end;">
        <div>
            <div style="color:#3adffa; font-size:12px; font-family:'Space Grotesk'; letter-spacing:0.2em; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
                <span style="display:inline-block; width:8px; height:8px; background:#3adffa; border-radius:50%; box-shadow:0 0 10px #3adffa;"></span>
                NODE SECURE // ALPHA-7
            </div>
            <h2 style="font-family:'Space Grotesk'; font-size:42px; margin:0; font-weight:700; background:linear-gradient(90deg, #fff, #a3aac4); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">System Alerts Log</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1.5, 1.5, 2])
    with col1:
        st.markdown("""
        <div style="background:rgba(255,113,108,0.05); border:1px solid rgba(255,113,108,0.2); border-radius:8px; padding:24px; position:relative; overflow:hidden;">
            <div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(to right, #ff716c, transparent);"></div>
            <div style="font-size:11px; color:#ff716c; font-family:'Space Grotesk'; letter-spacing:0.15em; font-weight:bold;">CRITICAL INCIDENTS (24H)</div>
            <div style="font-size:52px; font-weight:700; color:#ff716c; font-family:'Space Grotesk'; line-height:1.2; text-shadow:0 0 20px rgba(255,113,108,0.4);">14</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="background:rgba(58,223,250,0.05); border:1px solid rgba(58,223,250,0.2); border-radius:8px; padding:24px; position:relative; overflow:hidden;">
            <div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(to right, #3adffa, transparent);"></div>
            <div style="font-size:11px; color:#3adffa; font-family:'Space Grotesk'; letter-spacing:0.15em; font-weight:bold;">SYSTEM ANOMALIES</div>
            <div style="font-size:52px; font-weight:700; color:#3adffa; font-family:'Space Grotesk'; line-height:1.2; text-shadow:0 0 20px rgba(58,223,250,0.4);">03</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="background:rgba(109,254,156,0.05); border:1px solid rgba(109,254,156,0.2); border-radius:8px; padding:24px; position:relative; overflow:hidden; height:100%;">
            <div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(to right, #6dfe9c, transparent);"></div>
            <div style="font-size:11px; color:#6dfe9c; font-family:'Space Grotesk'; letter-spacing:0.15em; font-weight:bold;">PREDICTIVE UPTIME</div>
            <div style="font-size:52px; font-weight:700; color:#6dfe9c; font-family:'Space Grotesk'; line-height:1.2; text-shadow:0 0 20px rgba(109,254,156,0.4);">99.2%</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="alert-card" style="padding:0; overflow:hidden;">
    <div style="background:rgba(10, 15, 30, 0.9); padding:16px 24px; display:flex; font-size:11px; color:#6d758c; font-family:'Space Grotesk'; letter-spacing:0.15em; font-weight:bold; border-bottom:1px solid rgba(58,223,250,0.1);">
    <div style="width:170px;">TIMESTAMP</div>
    <div style="width:120px;">SEVERITY</div>
    <div style="flex-grow:1;">DESCRIPTION</div>
    </div>
    
    <div class="alert-row critical">
    <div class="alert-time">{times[0]}</div>
    <div class="badge-container"><div class="alert-badge badge-critical">CRITICAL</div></div>
    <div class="alert-desc">High Vibration Detected - Main Turbine Axis B</div>
    </div>
    
    <div class="alert-row warning">
    <div class="alert-time">{times[1]}</div>
    <div class="badge-container"><div class="alert-badge badge-warning">WARNING</div></div>
    <div class="alert-desc">Thermal Variance Threshold Exceeded (+12°C)</div>
    </div>
    
    <div class="alert-row info">
    <div class="alert-time">{times[2]}</div>
    <div class="badge-container"><div class="alert-badge badge-info">INFO</div></div>
    <div class="alert-desc">Routine Calibration Protocol Initiated by AI Node</div>
    </div>
    
    <div class="alert-row critical">
    <div class="alert-time">{times[3]}</div>
    <div class="badge-container"><div class="alert-badge badge-critical">CRITICAL</div></div>
    <div class="alert-desc">Emergency Stop Triggered: Hydraulic Pressure Drop</div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("← Back to Dashboard"):
        st.session_state.current_page = "dashboard"; st.rerun()
    

if st.session_state.current_page == "login":
    render_login()
elif st.session_state.current_page == "dashboard":
    render_dashboard()
elif st.session_state.current_page == "sensors":
    render_sensors()
elif st.session_state.current_page == "alerts":
    render_alerts()
