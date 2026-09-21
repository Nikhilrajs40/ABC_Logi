import streamlit as st
import joblib
import pandas as pd
import time

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Delivery Delay Predictor",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Remove Streamlit default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fb 0%, #eef2f7 100%);
    }

    /* Header */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #172033;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #687386;
        margin-bottom: 35px;
    }

    /* Section headings */
    .section-title {
        font-size: 21px;
        font-weight: 700;
        color: #172033;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    /* Input card */
    .input-card {
        background: white;
        padding: 24px;
        border-radius: 18px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.06);
        margin-bottom: 20px;
        border: 1px solid #e9edf3;
    }

    /* Prediction container */
    .prediction-card {
        background: white;
        border-radius: 22px;
        padding: 35px;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0,0,0,0.08);
        margin-top: 30px;
        border: 1px solid #e9edf3;
    }

    .prediction-label {
        color: #687386;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .prediction-delay {
        color: #d62828;
        font-size: 38px;
        font-weight: 800;
        margin: 5px 0;
    }

    .prediction-ontime {
        color: #159957;
        font-size: 38px;
        font-weight: 800;
        margin: 5px 0;
    }

    .probability-text {
        font-size: 18px;
        color: #4d586b;
        margin-top: 15px;
    }

    /* Countdown */
    .countdown {
        text-align: center;
        font-size: 70px;
        font-weight: 900;
        color: #2563eb;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #8a94a6;
        font-size: 13px;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #dde2ea;
    }

    /* Button */
    div.stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 14px;
        border: none;
        background: linear-gradient(90deg, #2563eb, #1d4ed8);
        color: white;
        font-size: 18px;
        font-weight: 700;
        box-shadow: 0 6px 15px rgba(37,99,235,0.25);
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 9px 20px rgba(37,99,235,0.35);
        background: linear-gradient(90deg, #1d4ed8, #1e40af);
    }

    /* Metric cards */
    .metric-card {
        background: #f8fafc;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #e5eaf0;
    }

    .metric-title {
        font-size: 14px;
        color: #7a8496;
        margin-bottom: 5px;
    }

    .metric-value {
        font-size: 27px;
        font-weight: 800;
        color: #172033;
    }

    /* Hide Streamlit menu/footer */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("logi.sav")

model = load_model()

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🚚 Delivery Delay Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict whether a delivery will arrive on time or experience a delay</div>',
    unsafe_allow_html=True
)

# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">📦 Delivery Information</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="input-card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    delivery_distance = st.number_input(
        "📍 Delivery Distance (km)",
        min_value=0.0,
        value=20.0,
        step=1.0
    )

with col2:
    traffic_congestion = st.slider(
        "🚦 Traffic Congestion",
        1, 5, 3
    )

with col3:
    weather_condition = st.slider(
        "🌦️ Weather Condition",
        1, 5, 3
    )

col4, col5, col6 = st.columns(3)

with col4:
    delivery_slot = st.slider(
        "🕒 Delivery Slot",
        1, 3, 2
    )

with col5:
    driver_experience = st.number_input(
        "👨‍✈️ Driver Experience (years)",
        min_value=0,
        value=5,
        step=1
    )

with col6:
    num_stops = st.number_input(
        "📍 Number of Stops",
        min_value=0,
        value=5,
        step=1
    )

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# VEHICLE & PACKAGE SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🚛 Vehicle & Package Information</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="input-card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    vehicle_age = st.number_input(
        "🚗 Vehicle Age (years)",
        min_value=0,
        value=5,
        step=1
    )

with col2:
    road_condition_score = st.slider(
        "🛣️ Road Condition Score",
        1, 5, 3
    )

with col3:
    package_weight = st.number_input(
        "📦 Package Weight (kg)",
        min_value=0.0,
        value=10.0,
        step=0.5
    )

col4, col5 = st.columns(2)

with col4:
    fuel_efficiency = st.number_input(
        "⛽ Fuel Efficiency (km/l)",
        min_value=0.0,
        value=15.0,
        step=0.5
    )

with col5:
    warehouse_processing_time = st.number_input(
        "🏭 Warehouse Processing Time (minutes)",
        min_value=0,
        value=60,
        step=5
    )

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# CREATE INPUT DATA
# =========================================================

input_data = pd.DataFrame([{
    'Delivery_Distance': delivery_distance,
    'Traffic_Congestion': traffic_congestion,
    'Weather_Condition': weather_condition,
    'Delivery_Slot': delivery_slot,
    'Driver_Experience': driver_experience,
    'Num_Stops': num_stops,
    'Vehicle_Age': vehicle_age,
    'Road_Condition_Score': road_condition_score,
    'Package_Weight': package_weight,
    'Fuel_Efficiency': fuel_efficiency,
    'Warehouse_Processing_Time': warehouse_processing_time
}])

# =========================================================
# PREDICTION BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

button_col1, button_col2, button_col3 = st.columns([1, 2, 1])

with button_col2:

    predict_button = st.button(
        "🔍  Predict Delivery Status"
    )

# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # Countdown
    countdown_placeholder = st.empty()

    for number in [3, 2, 1]:

        countdown_placeholder.markdown(
            f'<div class="countdown">{number}</div>',
            unsafe_allow_html=True
        )

        time.sleep(0.7)

    countdown_placeholder.empty()

    # Prediction
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    delay_probability = prediction_proba[0][1]
    ontime_probability = prediction_proba[0][0]

    # =====================================================
    # RESULT
    # =====================================================

    if prediction[0] == 1:

        st.markdown(
            f"""
            <div class="prediction-card">

                <div class="prediction-label">
                    PREDICTION RESULT
                </div>

                <div class="prediction-delay">
                    ⚠️ DELIVERY DELAYED
                </div>

                <div class="probability-text">
                    Probability of Delay:
                    <b>{delay_probability:.1%}</b>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="prediction-card">

                <div class="prediction-label">
                    PREDICTION RESULT
                </div>

                <div class="prediction-ontime">
                    ✅ DELIVERY ON TIME
                </div>

                <div class="probability-text">
                    Probability of On Time:
                    <b>{ontime_probability:.1%}</b>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # PROBABILITY SECTION
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📊 Prediction Confidence</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    🚚 Probability of On Time
                </div>

                <div class="metric-value">
                    {ontime_probability:.1%}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(float(ontime_probability))

    with col2:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    ⚠️ Probability of Delay
                </div>

                <div class="metric-value">
                    {delay_probability:.1%}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(float(delay_probability))

    # =====================================================
    # INPUT SUMMARY
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📋 Input Summary</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Distance",
            f"{delivery_distance:.1f} km"
        )

    with col2:
        st.metric(
            "Traffic",
            f"{traffic_congestion}/5"
        )

    with col3:
        st.metric(
            "Stops",
            f"{num_stops}"
        )

    with col4:
        st.metric(
            "Warehouse Time",
            f"{warehouse_processing_time} min"
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Delivery Delay Prediction System &nbsp;•&nbsp; Machine Learning Model
    </div>
    """,
    unsafe_allow_html=True
)
