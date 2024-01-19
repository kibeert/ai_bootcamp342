import pickle
import streamlit as st

# loading the saved model
diseases_model = pickle.load(open('diseases_model.sav', 'rb'))

# Diseases Prediction Page title
st.title("France's Smart Health Checker")

# Define a subset of common diseases
common_diseases = [
    "Paroymsal Positional Vertigo", "AIDS", "Acne", "Alcoholic Hepatitis", "Allergy", "Arthritis",
    "Bronchial Asthma", "Cervical Spondylosis", "Chickenpox", "Chronic Cholestasis", "Common Cold",
    "Dengue", "Diabetes", "Dimorphic Hemorrhoids (Piles)", "Drug Reaction", "Fungal Infection", "GERD",
    "Gastroenteritis", "Heart Attack", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E",
    "Hypertension", "Hyperthyroidism", "Hypoglycemia", "Hypothyroidism", "Impetigo", "Jaundice", "Malaria",
    "Migraine", "Osteoarthritis", "Paralysis (Brain Hemorrhage)", "Peptic Ulcer Disease", "Pneumonia",
    "Psoriasis", "Tuberculosis", "Typhoid", "Urinary Tract Infection", "Varicose Veins", "Hepatitis A",
]

# Define a subset of common symptoms
common_symptoms = [
    "Itching", "Skin Rash", "Continuous Sneezing", "Chills", "Joint Pain", "Vomiting",
    "Fatigue", "Weight Loss", "Cough", "High Fever", "Headache", "Yellowish Skin"
]

# getting the input data from the user
col1, col2, col3 = st.columns(3)

def validate_input(value):
    if value not in ['0', '1']:
        return '0'  # Default to 0 if input is not 0 or 1
    return value

with col1:
    Itching = st.text_input('Itching', value='0', max_chars=1)
    Itching = validate_input(Itching)

with col2:
    Skin_Rash = st.text_input('Skin Rash', value='0', max_chars=1)
    Skin_Rash = validate_input(Skin_Rash)

with col3:
    Continuous_Sneezing = st.text_input('Continuous Sneezing', value='0', max_chars=1)
    Continuous_Sneezing = validate_input(Continuous_Sneezing)

with col1:
    Chills = st.text_input('Chills', value='0', max_chars=1)
    Chills = validate_input(Chills)

with col2:
    Joint_Pain = st.text_input('Joint Pain', value='0', max_chars=1)
    Joint_Pain = validate_input(Joint_Pain)

with col3:
    Vomiting = st.text_input('Vomiting', value='0', max_chars=1)
    Vomiting = validate_input(Vomiting)

with col1:
    Fatigue = st.text_input('Fatigue', value='0', max_chars=1)
    Fatigue = validate_input(Fatigue)

with col2:
    Weight_Loss = st.text_input('Weight Loss', value='0', max_chars=1)
    Weight_Loss = validate_input(Weight_Loss)

with col3:
    Cough = st.text_input('Cough', value='0', max_chars=1)
    Cough = validate_input(Cough)

with col1:
    High_Fever = st.text_input('High Fever', value='0', max_chars=1)
    High_Fever = validate_input(High_Fever)

with col2:
    Headache = st.text_input('Headache', value='0', max_chars=1)
    Headache = validate_input(Headache)

with col3:
    Yellowish_Skin = st.text_input('Yellowish Skin', value='0', max_chars=1)
    Yellowish_Skin = validate_input(Yellowish_Skin)

# code for Prediction
disease_diagnosis = ''

# creating a button for Prediction
if st.button('Disease Test Result'):

    user_input = [Itching, Skin_Rash, Continuous_Sneezing, Chills, Joint_Pain, Vomiting,
                  Fatigue, Weight_Loss, Cough, High_Fever, Headache, Yellowish_Skin]

     # Check if all inputs are zero
    if all(x == '0' for x in user_input):
        disease_diagnosis = "Everything looks great healthwise. Keep taking care of yourself!"
    else:
        user_input = [float(x) for x in user_input]
        disease_prediction = diseases_model.predict([user_input])

        if 1 <= disease_prediction[0] <= len(common_diseases):
            disease_diagnosis = f'You might be suffering from {common_diseases[disease_prediction[0] - 1]}.'
        else:
            disease_diagnosis = 'You might be suffering from some disease.'

        # Add a message about consulting a professional doctor
        disease_diagnosis += ' Kindly see a professional doctor for proper check-up and medication.'

st.success(disease_diagnosis)
