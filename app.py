import streamlit as st
import joblib
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Delivery Delay Prediction",
    page_icon="🚚",
    layout="wide"
)

# -------------------------------
# Simple Styling
# -------------------------------

st.markdown("""
<style>

body {
    background-color: #f5f7fa;
}

.main {
    background-color: #f5f7fa;
}

h1 {
    color: #1f3c88;
    text-align: center;
    font-size: 38px;
}

h2 {
    color: #1f3c88;
}

.stButton > button {
    width: 100%;
    background-color: #1f3c88;
    color: white;
    border-radius: 8px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #162f6b;
    color: white;
}

.result {
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    background-color: white;
    border: 1px solid #dddddd;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------
# Load Model
# -------------------------------

model = joblib.load("logi.sav")


# -------------------------------
# Title
# -------------------------------

st.title("🚚 Delivery Delay Prediction")

st.markdown(
    "<p style='text-align:center; color:gray;'>"
    "Enter the delivery details to predict whether the delivery will be delayed."
    "</p>",
    unsafe_allow_html=True
)

st.divider()


# -------------------------------
# Delivery Information
# -------------------------------

st.header("📦 Delivery Information")

col1, col2, col3 = st.columns(3)

with col1:
    delivery_distance = st.number_input(
        "Delivery Distance (km)",
        min_value=0.0,
        value=20.0
    )

with col2:
    traffic_congestion = st.slider(
        "Traffic Congestion",
        1, 5, 3
    )

with col3:
    weather_condition = st.slider(
        "Weather Condition",
        1, 5, 3
    )


col1, col2, col3 = st.columns(3)

with col1:
    delivery_slot = st.slider(
        "Delivery Slot",
        1, 3, 2
    )

with col2:
    driver_experience = st.number_input(
        "Driver Experience (years)",
        min_value=0,
        value=5
    )

with col3:
    num_stops = st.number_input(
        "Number of Stops",
        min_value=0,
        value=5
    )


st.divider()


# -------------------------------
# Vehicle & Package Information
# -------------------------------

st.header("🚛 Vehicle & Package Information")

col1, col2, col3 = st.columns(3)

with col1:
    vehicle_age = st.number_input(
        "Vehicle Age (years)",
        min_value=0,
        value=5
    )

with col2:
    road_condition_score = st.slider(
        "Road Condition Score",
        1, 5, 3
    )

with col3:
    package_weight = st.number_input(
        "Package Weight (kg)",
        min_value=0.0,
        value=10.0
    )


col1, col2 = st.columns(2)

with col1:
    fuel_efficiency = st.number_input(
        "Fuel Efficiency (km/l)",
        min_value=0.0,
        value=15.0
    )

with col2:
    warehouse_processing_time = st.number_input(
        "Warehouse Processing Time (minutes)",
        min_value=0,
        value=60
    )


st.divider()


# -------------------------------
# Create Input Data
# -------------------------------

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


# -------------------------------
# Prediction Button
# -------------------------------

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    predict = st.button("🔍 Predict Delivery Status")


# -------------------------------
# Prediction
# -------------------------------

if predict:

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)

    ontime_probability = probability[0][0]
    delay_probability = probability[0][1]

    st.divider()

    st.header("📊 Prediction Result")

    if prediction[0] == 1:

        st.error(
            "⚠️ DELIVERY DELAYED"
        )

    else:

        st.success(
            "✅ DELIVERY ON TIME"
        )


    # Probability

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Probability of On Time",
            f"{ontime_probability:.1%}"
        )

        st.progress(float(ontime_probability))


    with col2:

        st.metric(
            "Probability of Delay",
            f"{delay_probability:.1%}"
        )

        st.progress(float(delay_probability))
