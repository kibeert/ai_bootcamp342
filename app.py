import pickle
import streamlit as st

# loading the saved model
diabetes_model = pickle.load(open('diseases_model.sav', 'rb'))

# Diseases Prediction Page title
st.title('Diseases Prediction using ML')

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Fever = st.text_input('Fever check', value='0')

with col2:
    Chills = st.text_input('Chills check', value='0')

with col3:
    Congestion = st.text_input('Congestion check', value='0')

with col1:
    Cough = st.text_input('Cough check', value='0')

with col2:
    Fatigue = st.text_input('Fatigue check', value='0')

with col3:
    Muscle_Aches = st.text_input('Muscle Ache check', value='0')

with col1:
    Headache = st.text_input('Headache check', value='0')

with col2:
    Diarrhea = st.text_input('Diarrhea check', value='0')

with col3:
    Nausea = st.text_input('Nausea check', value='0')

with col1:
    Vomiting = st.text_input('Vomiting check', value='0')

# code for Prediction
disease_diagnosis = ''

# creating a button for Prediction
if st.button('Disease Test Result'):

    user_input = [Fever, Chills, Congestion, Cough, Fatigue, Muscle_Aches, Headache, Diarrhea, Nausea, Vomiting]

    user_input = [float(x) for x in user_input]

    disease_prediction = diabetes_model.predict([user_input])

    if disease_prediction[0] == 1:
        disease_diagnosis = 'The patient is suffering from Common Cold.'
    elif disease_prediction[0] == 2:
        disease_diagnosis = 'The patient is suffering from Flu.'
    elif disease_prediction[0] == 3:
        disease_diagnosis = 'The patient is suffering from COVID-19.'
    elif disease_prediction[0] == 4:
        disease_diagnosis = 'The patient is suffering from Gastroenteritis.'
    elif disease_prediction[0] == 5:
        disease_diagnosis = 'The patient is suffering from Hepatitis.'
    elif disease_prediction[0] == 6:
        disease_diagnosis = 'The patient is suffering from Respiratory Syncytial Virus (RSV).'
    elif disease_prediction[0] == 7:
        disease_diagnosis = 'The patient is suffering from Strep Throat.'
    elif disease_prediction[0] == 8:
        disease_diagnosis = 'The patient is suffering from Salmonella.'
    elif disease_prediction[0] == 9:
        disease_diagnosis = 'The patient is suffering from Tuberculosis.'
    elif disease_prediction[0] == 10:
        disease_diagnosis = 'The patient is suffering from Whooping Cough.'
    elif disease_prediction[0] == 11:
        disease_diagnosis = 'The patient is suffering from Chlamydia.'
    elif disease_prediction[0] == 12:
        disease_diagnosis = 'The patient is suffering from Gonorrhea.'
    elif disease_prediction[0] == 13:
        disease_diagnosis = 'The patient is suffering from Urinary Tract Infections (UTIs).'
    elif disease_prediction[0] == 14:
        disease_diagnosis = 'The patient is suffering from E. coli.'
    elif disease_prediction[0] == 15:
        disease_diagnosis = 'The patient is suffering from Clostridioides difficile.'
    elif disease_prediction[0] == 16:
        disease_diagnosis = 'The patient is suffering from Ringworm.'
    elif disease_prediction[0] == 17:
        disease_diagnosis = 'The patient is suffering from Fungal Nail Infections.'
    elif disease_prediction[0] == 18:
        disease_diagnosis = 'The patient is suffering from Thrush.'
    elif disease_prediction[0] == 19:
        disease_diagnosis = 'The patient is suffering from Giardiasis.'
    elif disease_prediction[0] == 20:
        disease_diagnosis = 'The patient is suffering from Toxoplasmosis.'
    else:
        disease_diagnosis = 'The patient is suffering from some disease.'

st.success(disease_diagnosis)
