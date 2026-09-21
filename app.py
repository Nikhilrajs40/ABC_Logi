import streamlit as st
import joblib
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Delivery Delay Predictor",
    page_icon="🚚",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* ---------- MAIN PAGE ---------- */

    .stApp {
        background: #f4f7fb;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 35px;
        padding-bottom: 40px;
    }

    /* ---------- HEADER ---------- */

    .header {
        background: linear-gradient(135deg, #173b7a, #2563b8);
        padding: 35px 40px;
        border-radius: 22px;
        margin-bottom: 28px;
        box-shadow: 0 8px 25px rgba(37, 99, 184, 0.18);
    }

    .header-title {
        color: white;
        font-size: 38px;
        font-weight: 800;
        margin: 0;
    }

    .header-subtitle {
        color: #dbeafe;
        font-size: 16px;
        margin-top: 8px;
    }

    /* ---------- SECTION CARD ---------- */

    .section-card {
        background: white;
        padding: 28px 30px;
        border-radius: 20px;
        margin-bottom: 22px;
        border: 1px solid #e5eaf1;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.05);
    }

    .section-heading {
        font-size: 21px;
        font-weight: 750;
        color: #172033;
        margin-bottom: 18px;
    }

    .section-description {
        color: #7b8494;
        font-size: 14px;
        margin-top: -10px;
        margin-bottom: 22px;
    }

    /* ---------- INPUT LABELS ---------- */

    label {
        font-weight: 600 !important;
        color: #374151 !important;
    }

    /* ---------- BUTTON ---------- */

    div.stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 13px;
        border: none;
        background: linear-gradient(135deg, #2563eb, #174ea6);
        color: white;
        font-size: 17px;
        font-weight: 700;
        box-shadow: 0 6px 15px rgba(37, 99, 235, 0.22);
        transition: 0.2s;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #174ea6, #123d85);
        transform: translateY(-1px);
    }

    /* ---------- RESULT ---------- */

    .result-card {
        padding: 30px;
        border-radius: 20px;
        margin-top: 25px;
        text-align: center;
        background: white;
        border: 1px solid #e5eaf1;
        box-shadow: 0 7px 25px rgba(15, 23, 42, 0.07);
    }

    .result-title {
        font-size: 14px;
        font-weight: 700;
        color: #7b8494;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .delay-result {
        color: #dc2626;
        font-size: 34px;
        font-weight: 800;
    }

    .ontime-result {
        color: #059669;
        font-size: 34px;
        font-weight: 800;
    }

    .result-subtitle {
        color: #6b7280;
        font-size: 16px;
        margin-top: 8px;
    }

    /* ---------- PROBABILITY CARDS ---------- */

    .prob-card {
        background: #f8fafc;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        border: 1px solid #e8edf3;
    }

    .prob-label {
        color: #6b7280;
        font-size: 14px;
        font-weight: 600;
    }

    .prob-value {
        color: #172033;
        font-size: 28px;
        font-weight: 800;
        margin-top: 5px;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 13px;
        margin-top: 35px;
    }

    /* ---------- HIDE DEFAULT STREAMLIT ---------- */

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

st.markdown("""
<div class="header">

    <div class="header-title">
        🚚 Delivery Delay Predictor
    </div>

    <div class="header-subtitle">
        Machine learning based prediction of delivery performance
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# DELIVERY INFORMATION
# =========================================================

st.markdown("""
<div class="section-card">

    <div class="section-heading">
        📦 Delivery Information
    </div>

    <div class="section-description">
        Enter the delivery and traffic conditions
    </div>

</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    delivery_distance = st.number_input(
        "Delivery Distance (km)",
        min_value=0.0,
        value=20.0,
        step=1.0
    )

with col2:
    traffic_congestion = st.slider(
        "Traffic Congestion",
        min_value=1,
        max_value=5,
        value=3
    )

with col3:
    weather_condition = st.slider(
        "Weather Condition",
        min_value=1,
        max_value=5,
        value=3
    )


col1, col2, col3 = st.columns(3)

with col1:
    delivery_slot = st.slider(
        "Delivery Slot",
        min_value=1,
        max_value=3,
        value=2
    )

with col2:
    driver_experience = st.number_input(
        "Driver Experience (years)",
        min_value=0,
        value=5,
        step=1
    )

with col3:
    num_stops = st.number_input(
        "Number of Stops",
        min_value=0,
        value=5,
        step=1
    )


# =========================================================
# VEHICLE & PACKAGE
# =========================================================

st.markdown("""
<div class="section-card">

    <div class="section-heading">
        🚛 Vehicle & Package Information
    </div>

    <div class="section-description">
        Provide information about the vehicle, road and package
    </div>

</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    vehicle_age = st.number_input(
        "Vehicle Age (years)",
        min_value=0,
        value=5,
        step=1
    )

with col2:
    road_condition_score = st.slider(
        "Road Condition Score",
        min_value=1,
        max_value=5,
        value=3
    )

with col3:
    package_weight = st.number_input(
        "Package Weight (kg)",
        min_value=0.0,
        value=10.0,
        step=0.5
    )


col1, col2 = st.columns(2)

with col1:
    fuel_efficiency = st.number_input(
        "Fuel Efficiency (km/l)",
        min_value=0.0,
        value=15.0,
        step=0.5
    )

with col2:
    warehouse_processing_time = st.number_input(
        "Warehouse Processing Time (minutes)",
        min_value=0,
        value=60,
        step=5
    )


# =========================================================
# INPUT DATA
# =========================================================

input_data = pd.DataFrame([{

    "Delivery_Distance": delivery_distance,

    "Traffic_Congestion": traffic_congestion,

    "Weather_Condition": weather_condition,

    "Delivery_Slot": delivery_slot,

    "Driver_Experience": driver_experience,

    "Num_Stops": num_stops,

    "Vehicle_Age": vehicle_age,

    "Road_Condition_Score": road_condition_score,

    "Package_Weight": package_weight,

    "Fuel_Efficiency": fuel_efficiency,

    "Warehouse_Processing_Time": warehouse_processing_time

}])


# =========================================================
# PREDICT BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    predict = st.button(
        "🔍  Predict Delivery Status"
    )


# =========================================================
# RESULT
# =========================================================

if predict:

    prediction = model.predict(input_data)

    prediction_proba = model.predict_proba(input_data)

    ontime_probability = prediction_proba[0][0]

    delay_probability = prediction_proba[0][1]


    # -----------------------------------------------------
    # MAIN RESULT
    # -----------------------------------------------------

    if prediction[0] == 1:

        st.markdown(f"""
        <div class="result-card">

            <div class="result-title">
                PREDICTION RESULT
            </div>

            <div class="delay-result">
                ⚠️ DELIVERY DELAYED
            </div>

            <div class="result-subtitle">
                The model predicts that this delivery is likely to be delayed.
            </div>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class="result-card">

            <div class="result-title">
                PREDICTION RESULT
            </div>

            <div class="ontime-result">
                ✓ DELIVERY ON TIME
            </div>

            <div class="result-subtitle">
                The model predicts that this delivery is likely to arrive on time.
            </div>

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # PROBABILITIES
    # -----------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-heading">
        📊 Prediction Probabilities
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class="prob-card">

            <div class="prob-label">
                ✓ Probability of On Time
            </div>

            <div class="prob-value">
                {ontime_probability:.1%}
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.progress(float(ontime_probability))


    with col2:

        st.markdown(f"""
        <div class="prob-card">

            <div class="prob-label">
                ⚠ Probability of Delay
            </div>

            <div class="prob-value">
                {delay_probability:.1%}
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.progress(float(delay_probability))


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    Delivery Delay Prediction System • Logistic Regression
</div>
""", unsafe_allow_html=True)
