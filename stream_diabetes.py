import pickle
import numpy as np
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title ('Data Mining Prediksi Diabetes')

col1,col2  = st.columns(2)
with col1: 
    Pregnancies = st.text_input('Input nilai pregnancies: ')
    BloodPressure = st.text_input('Input nilai Blood Pressure: ')
    Insulin = st.text_input('Input nilai Insulin: ')
    DiabetesPedigreeFunction = st.text_input('Input nilai Diabetes Pedigree Function: ')
with col2:
    Glucose = st.text_input('Input nilai glucose: ')
    SkinThickness = st.text_input('Input nilai Skin Thickness: ')
    BMI = st.text_input('Input nilai BMI: ')
    Age = st.text_input('Input nilai age: ')

# code untuk prediksi
diab_diagnosis = ''

# Membuat tombol prediksi
if st.button('Prediksi Diabetes'):
    try:
        # Gabungkan input menjadi array 2D
        input_data = np.array([[
            float(Pregnancies), 
            float(Glucose), 
            float(BloodPressure), 
            float(SkinThickness), 
            float(Insulin), 
            float(BMI), 
            float(DiabetesPedigreeFunction), 
            float(Age)
        ]])
        
        # Prediksi
        diab_prediction = diabetes_model.predict(input_data)
        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien terkena diabetes'
        else:
            diab_diagnosis = 'Pasien tidak terkena diabetes'
        
        st.success(diab_diagnosis)
    except ValueError:
        st.error("Pastikan semua input adalah angka yang valid!")