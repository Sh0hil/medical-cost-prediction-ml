Medical Insurance Premium Predictor 🏥

# Overview
The Medical Insurance Premium Predictor is an end-to-end Machine Learning application designed to estimate health insurance costs based on individual demographic and lifestyle factors.

This repository contains the complete pipeline: from data exploration and model training using a Jupyter Notebook to a fully functional, interactive web application built with Streamlit.

Key Features
Interactive Web Interface: A user-friendly front-end built with Streamlit that allows users to input their details and receive instant premium estimates.

Robust Machine Learning Model: Utilizes a RandomForestRegressor from Scikit-Learn to accurately capture complex, non-linear relationships in the data.

Comprehensive Data Analysis: Includes a Jupyter Notebook detailing Exploratory Data Analysis (EDA), data preprocessing, and model evaluation metrics.


# Exploratory Data Analysis (EDA)
During the development of this model, extensive data exploration was conducted to understand the distribution of features and their impact on insurance charges. Below are some of the key visualizations from the analysis:

### 1. Distribution of Insurance Charges
<p align="center">
  <img src="count_charges.png" alt="Distribution of Charges" width="600"/>
</p>

**Insight:** The target variable, `charges`, is heavily right-skewed. Most beneficiaries incur lower medical costs (typically under $15,000), while a smaller subset of individuals faces significantly higher premiums. This skewness indicates that a few key risk factors are driving up the costs for certain individuals.

### 2. The Impact of Smoking Status
<p align="center">
  <img src="smoker_nonSmoker.png" alt="Smoker vs Non-Smoker" width="600"/>
</p>

**Insight:** Smoking is the most critical feature in the dataset. As shown in the plot, there is a stark contrast between smokers and non-smokers. Smokers form a distinct cluster with drastically higher baseline medical charges compared to non-smokers, making this a highly influential predictor for the machine learning model.

### 3. BMI (Body Mass Index) Trends
<p align="center">
  <img src="count_VS_bmi.png" alt="BMI Analysis" width="600"/>
</p>

**Insight:** Body Mass Index shows a normal distribution, with most individuals falling between the 25 and 35 range. When combined with other risk factors (like smoking), a higher BMI exponentially increases the overall medical insurance premium, highlighting the compound effect of multiple health risks.

### 4. Age Demographics
<p align="center">
  <img src="count_age.png" alt="Age Distribution" width="600"/>
</p>

**Insight:** The dataset includes individuals ranging from 18 to 64 years old. Interestingly, there is a massive spike in the 18-19 age group, representing a large influx of young adults entering the insurance pool. Outside of that spike, the distribution is relatively uniform across other age groups.


Tech Stack
Language: Python 

Front-end Framework: Streamlit

Machine Learning: Scikit-Learn

Data Manipulation & Analysis: Pandas, NumPy

Data Visualization: Matplotlib, Seaborn

Serialization: Pickle

Project Structure
Plaintext
├── app.py                               # Streamlit application script
├── medical_insurance_prediction.ipynb   # Jupyter notebook for EDA and model training
├── MIPML.pkl                            # Serialized Random Forest model
├── insurance.csv                        # Dataset (required for training notebook)
└── README.md                            # Project documentation


How It Works
The application takes six inputs from the user to calculate the predicted premium:

Age: Numeric value (5 to 90 years).

Gender: Male or Female.

BMI (Body Mass Index): Numeric value (5.0 to 70.0) indicating body fat based on weight and height.

Children: Number of dependents covered by the insurance (0 to 5).

Smoker: Smoking status (Yes or No).

Region: Residential area in the US (NorthWest, NorthEast, SouthWest, SouthEast).

The inputs are preprocessed to match the training data format (e.g., categorical variables like 'Smoker' and 'Gender' are label-encoded) and fed into the pre-trained Random Forest model (MIPML.pkl) to output the estimated cost.

Installation and Setup

1. Clone the repository:

Bash
git clone https://github.com/yourusername/medical-insurance-predictor.git
cd medical-insurance-predictor

2. Create a virtual environment (Recommended):

Bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:
Ensure you have the necessary libraries installed. You can install them manually or create a requirements.txt file containing:

Bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn

4. Run the Streamlit application:

Bash
streamlit run app.py
The application will launch in your default web browser at http://localhost:8501.


Model Training
If you wish to retrain the model or explore the data:

Open medical_insurance_prediction.ipynb in Jupyter Notebook or Jupyter Lab.

Ensure insurance.csv is in the same directory.

Run the cells to execute the EDA, train the RandomForestRegressor, and generate a new MIPML.pkl file.