import streamlit as st
from predict import predict_price

st.title("🏠 House Price Predictor")
st.markdown("Enter house details to predict the price")

bedrooms = st.number_input("Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1.0, step=0.25)
sqft_living = st.number_input("Sqft Living", min_value=100, step=50)
floors = st.number_input("Floors", min_value=1, step=1)

if st.button("Predict"):
    result = predict_price(bedrooms, bathrooms, sqft_living, floors)
    st.success(f"Estimated Price: ₹{result:,.2f}")
