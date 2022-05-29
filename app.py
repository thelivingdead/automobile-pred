import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("car price.pkl","rb")
price_finder=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome!!"

#@app.route('/predict',methods=["Get"])
def car_price_predictor(year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner):
    
    
   
    prediction=price_finder.predict([[year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]])
    print(prediction)
    return prediction



def main():
    st.title("Automobile Price Prediction")
    html_temp = """
    <div style="background-color:olivedrab;padding:15px">
    <h2 style="color:white;text-align:center;">Check your Car Prices</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    year = st.text_input("Year","")
    Present_Price = st.text_input("Present Price(in lakhs)","")
    Kms_Driven = st.text_input("KiloMeters Driven","")
    Fuel_Type = st.selectbox("Fuel Type",("Petrol","Diesel"))
    if Fuel_Type=="Petrol":
        Fuel_Type=0
    else:
        Fuel_Type=1
    Seller_Type = st.selectbox("Seller Type",("Dealer","Individual"))
    if Seller_Type=="Dealer":
        Seller_Type=0
    else:
        Seller_Type=1
    Transmission = st.selectbox("Transmission",("Manual","Automatic"))
    if Transmission=="Manual":
        Transmission=0
    else:
        Transmission=1
    Owner = st.text_input("Owner By default enter 0 ","")


    result=0
    if st.button("Predict"):
        result=car_price_predictor(year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner)
    st.success('The output is {} lakhs'.format(result))
    if st.button("About"):
        st.text("Divya Bisht")
        st.text("Microsoft Engage 2022 Project")
        st.text("Email: divyabishtcse@gmail.com")

if __name__=='__main__':
    main()
    
