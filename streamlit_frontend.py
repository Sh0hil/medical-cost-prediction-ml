import streamlit as st
import requests
import os

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Insurance Predictor",
    page_icon="🏥",
    layout="centered"
)

# =========================================================
# HEADER
# =========================================================
st.title("Medical Insurance Cost Predictor")
st.markdown("""
Adjust the demographic and health parameters below to get a real-time estimate of medical insurance premiums.  
This UI is powered by a FastAPI backend running an optimized Machine Learning pipeline.
""")
st.divider()

# =========================================================
# FORM UI
# =========================================================
with st.form("prediction_form"):
    st.subheader("Patient Profile")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30, help="Age of the primary beneficiary")
        gender = st.selectbox("Gender", ["Male", "Female"])
        bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, help="Body Mass Index")

    with col2:
        children = st.number_input("Dependents", min_value=0, max_value=10, value=0, help="Number of dependents covered")
        smoker = st.selectbox("Smoker", ["Yes", "No"])
        region = st.selectbox("Region", ["Southeast", "Southwest", "Northeast", "Northwest"])

    submitted = st.form_submit_button("Predict Premium", type="primary", use_container_width=True)

# =========================================================
# API CALL SECTION
# =========================================================
if submitted:

    input_data = {
        "age": int(age),
        "sex": gender.lower(),
        "bmi": float(bmi),
        "children": int(children),
        "smoker": smoker.lower(),
        "region": region.lower()
    }

    # Docker / Localhost Smart Toggle
    if os.environ.get("DOCKER_ENV"):
        base_url = "http://api:8000"
    else:
        base_url = "http://127.0.0.1:8000"

    health_url = f"{base_url}/health"
    predict_url = f"{base_url}/predict"

    try:
        # ---------------------------------------------
        # Step 1: Check Backend Health
        # ---------------------------------------------
        health_response = requests.get(health_url, timeout=5)

        if health_response.status_code != 200:
            st.error("Backend health check failed.")
        else:
            # ---------------------------------------------
            # Step 2: Make Prediction Request
            # ---------------------------------------------
            with st.spinner("Analyzing patient data..."):
                response = requests.post(predict_url, json=input_data, timeout=10)

            if response.status_code == 200:
                result = response.json()

                if "predicted_premium" in result:
                    premium = result["predicted_premium"]

                    st.divider()
                    st.subheader("Prediction Results")
                    st.metric("Estimated Annual Premium Cost", f"${premium:,.2f}")
                    st.caption("Note: This is an AI-generated estimate based on historical medical insurance data.")

                else:
                    st.error(f"Prediction Error: {result}")

            else:
                st.error(f"API Error ({response.status_code}): {response.text}")

    except requests.exceptions.ConnectionError as e:
        st.error(f"Cannot connect to backend server.\n\nDetails: {e}")

    except requests.exceptions.Timeout:
        st.error("Backend request timed out. Please try again.")

    except Exception as e:
        st.error(f"Unexpected Error: {e}")