import streamlit as st
import requests

# 1. Page Configuration (Looks professional in the browser tab)
st.set_page_config(page_title="Insurance Predictor", page_icon="🏥", layout="centered")

# 2. Header Section
st.title("Medical Insurance Cost Predictor")
st.markdown("""
Adjust the demographic and health parameters below to get a real-time estimate of medical insurance premiums. 
This UI is powered by a FastAPI backend backend running an optimized Machine Learning pipeline.
""")
st.divider()

# 3. Using st.form (Crucial for performance)
with st.form("prediction_form"):
    st.subheader("Patient Profile")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Added 'help' tooltips for better UX
        age = st.number_input("Age", min_value=18, max_value=100, value=30, help="Age of the primary beneficiary")
        gender = st.selectbox("Gender", ["Male", "Female"])
        bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, help="Body Mass Index")
        
    with col2:
        children = st.number_input("Dependents", min_value=0, max_value=10, value=0, help="Number of children covered by insurance")
        smoker = st.selectbox("Smoker", ["Yes", "No"])
        region = st.selectbox("Region", ["Southeast", "Southwest", "Northeast", "Northwest"])

    # The submit button is tied to the form; use_container_width makes it look like a modern web app button
    submitted = st.form_submit_button("Predict Premium", type="primary", use_container_width=True)

# 4. Handle the API Call
if submitted:
    # Package data. Using .lower() ensures the data matches standard scikit-learn formatting expectations
    input_data = {
        "age": age,
        "sex": gender.lower(), 
        "bmi": bmi,
        "children": children,
        "smoker": smoker.lower(),
        "region": region.lower()
    }

    api_url = "http://127.0.0.1:8000/predict" 
    
    try:
        with st.spinner("Analyzing patient data..."):
            response = requests.post(api_url, json=input_data)
        
        if response.status_code == 200:
            result = response.json()
            premium = result["predicted_premium"]
            
            # 5. Creative Output Display (Using st.metric instead of standard text)
            st.divider()
            st.subheader("Prediction Results")
            st.metric(label="Estimated Annual Premium Cost", value=f"${premium:,.2f}")
            st.caption("Note: This is an AI-generated estimate based on historical health data.")
            
        else:
            st.error(f"API Error ({response.status_code}): {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("Backend Offline: Please ensure the FastAPI server is running on port 8000.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")