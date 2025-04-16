# 🩺 Smart Health Checker - Disease Prediction with SVM & Deep Learning

This repository contains a **Machine Learning and Deep Learning** based smart health checker capable of predicting diseases from symptoms using a trained **SVM model**, and an image classifier trained on **CIFAR-10** using a **Convolutional Neural Network (CNN)**. A **Streamlit** web app interface with **Ngrok tunneling** is also provided for easy deployment and interaction.

---

## 📂 Project Structure

- **`diseases_model.sav`** – Trained SVM model for disease prediction
- **`app.py`** – Streamlit web application
- **`diseases_training.csv`** – Dataset with symptoms and diagnoses
- **`CNN model`** – Built using TensorFlow/Keras for image classification (CIFAR-10)
- **`Visualization Notebooks`** – For EDA and plotting insights
- **`ngrok` integration** – For deploying the Streamlit app remotely

---

## 🎯 Features

- Predicts disease from 12 common symptoms using SVM.
- GUI using **Streamlit** for real-time input and output.
- Ngrok tunneling for remote access.
- Visualization of symptoms, health status, and prediction confidence.
- CNN model to classify CIFAR-10 images (for learning purposes).

---

## ⚙️ Technologies Used

- Python 🐍
- Scikit-learn (SVM)
- TensorFlow/Keras (CNN)
- Pandas, NumPy
- Matplotlib, Seaborn (Visualization)
- Streamlit (Web UI)
- Ngrok (Remote Deployment)
- Pickle (Model Serialization)

---

## 📊 Dataset Overview

### 🧪 Disease Prediction Dataset
- **Source**: Custom/predefined dataset
- **Rows**: 4920
- **Features**: 12 symptoms + 1 target label (`diagnosis`)
- **Symptoms**:
  - Itching, Skin Rash, Continuous Sneezing, Chills, Joint Pain, Vomiting, Fatigue, Weight Loss, Cough, High Fever, Headache, Yellowish Skin

### 🧠 CIFAR-10 Dataset
- Used to train a CNN for 10-class image classification (e.g., airplane, dog, cat, car, etc.)

---

## 📈 Model Performance

- **SVM Accuracy**
  - Train: ~72.48%
  - Test: ~70.93%
- **CNN Model (CIFAR-10)** trained using:
  - Conv2D, MaxPooling, Dropout layers
  - Validation accuracy and training loss tracked
- **Evaluation**:
  - Confusion Matrix
  - Classification Report

---

## 🚀 How to Run the Project

### 🧪 Disease Prediction App

1. Clone the repo
   ```bash
   git clone https://github.com/yourusername/disease-predictor
   cd disease-predictor
