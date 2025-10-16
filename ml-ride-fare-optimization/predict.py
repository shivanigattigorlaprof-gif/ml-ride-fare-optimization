import streamlit as st
import joblib
import numpy as np

class PricePredictor:
    def __init__(self):
        self.best_rf_model = joblib.load('models/best_rf_model.pkl')
        self.best_gb_model = joblib.load('models/best_gb_model.pkl')
        self.meta_model = joblib.load('models/new_meta_model.pkl')
        self.scaler = joblib.load('models/scaler.pkl')

    def preprocess_input(self, number_of_riders, number_of_drivers, expected_ride_duration, vehicle_type):
        vehicle_type_numeric = 1 if vehicle_type == 'Premium' else 0
        number_of_riders = np.array(number_of_riders)
        number_of_drivers = np.array(number_of_drivers)
        expected_ride_duration = np.array(expected_ride_duration)
        coefficients = np.polyfit(number_of_riders.ravel(), number_of_drivers.ravel(), deg=2)
        poly = np.poly1d(coefficients)
        division_feature = poly(number_of_riders / number_of_drivers)
        return [number_of_riders, number_of_drivers, expected_ride_duration, vehicle_type_numeric, division_feature]

    def predict_adjusted_ride_cost(self, preprocessed_input):
        scaled_input_data = self.scaler.transform([preprocessed_input])
        rf_pred = self.best_rf_model.predict(scaled_input_data)
        gb_pred = self.best_gb_model.predict(scaled_input_data)
        X_test_stacked = np.column_stack((rf_pred, gb_pred))
        meta_pred = self.meta_model.predict(X_test_stacked)
        return np.expm1(meta_pred)

    def run(self):
        st.set_page_config(page_title="Price Predictor", page_icon="📊")
        st.subheader('Ride Pricing Precision - Dynamic Pricing with ML', anchor=False, divider="rainbow")
        
        number_of_riders = st.number_input('Number of Riders', min_value=1)
        number_of_drivers = st.number_input('Number of Drivers', min_value=1)
        expected_ride_duration = st.number_input('Expected Ride Duration (minutes)', min_value=1)
        vehicle_type = st.selectbox('Vehicle Type', ['Economy', 'Premium'])

        if st.button('Predict'):
            scaled_input_data = self.preprocess_input(number_of_riders, number_of_drivers, expected_ride_duration, vehicle_type)
            predicted_adjusted_ride_cost = self.predict_adjusted_ride_cost(scaled_input_data)
            st.subheader('Dynamic Predicted Price for This Ride ', anchor=False, divider="rainbow")
            st.subheader(round(predicted_adjusted_ride_cost[0], 3))

if __name__ == '__main__':
    predictor = PricePredictor()
    predictor.run()
