import pickle
import streamlit as st

# loading the saved model
diseases_model = pickle.load(open('diseases_model.sav', 'rb'))

# Diseases Prediction Page title
st.title("Smart Health Checker")

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

def validate_input(symptom_input):
    return '0' if symptom_input not in ['0', '1'] else symptom_input

# getting the input data from the user
col1, col2, col3 = st.columns(3)

user_input = []

for i, symptom in enumerate(common_symptoms):
    with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3 as col:
        symptom_input = st.text_input(symptom, value='0', max_chars=1)
        validated_input = validate_input(symptom_input)
        user_input.append(validated_input)

# code for Prediction
disease_diagnosis = ''

# creating a button for Prediction
if st.button('Disease Test Result'):
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
