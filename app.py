import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('logi.sav')

st.title('Delivery Delay Prediction App')
st.write('Enter the features to predict if a delivery will be delayed.')

# Input fields for each feature
delivery_distance = st.number_input('Delivery Distance', min_value=0.0, value=20.0)
traffic_congestion = st.slider('Traffic Congestion (1-5)', 1, 5, 3)
weather_condition = st.slider('Weather Condition (1-5)', 1, 5, 3)
delivery_slot = st.slider('Delivery Slot (1-3)', 1, 3, 2)
driver_experience = st.number_input('Driver Experience (years)', min_value=0, value=5)
num_stops = st.number_input('Number of Stops', min_value=0, value=5)
vehicle_age = st.number_input('Vehicle Age (years)', min_value=0, value=5)
road_condition_score = st.slider('Road Condition Score (1-5)', 1, 5, 3)
package_weight = st.number_input('Package Weight (kg)', min_value=0.0, value=10.0)
fuel_efficiency = st.number_input('Fuel Efficiency (km/l)', min_value=0.0, value=15.0)
warehouse_processing_time = st.number_input('Warehouse Processing Time (minutes)', min_value=0, value=60)

# Create a DataFrame from user inputs
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

if st.button('Predict Delivery Delay'):
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    st.subheader('Prediction Result:')
    if prediction[0] == 1:
        st.error('The delivery is predicted to be DELAYED.')
    else:
        st.success('The delivery is predicted to be ON TIME.')
    
    st.write(f'Probability of Delay: {prediction_proba[0][1]:.2f}')
    st.write(f'Probability of On Time: {prediction_proba[0][0]:.2f}')
