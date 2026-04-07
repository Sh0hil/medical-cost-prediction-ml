@echo off
echo 🚀 Setting up the Medical Insurance Premium Predictor...

:: Create a virtual environment
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Upgrade pip
python -m pip install --upgrade pip

:: Install the required libraries
echo 📦 Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo ✅ Setup complete! Launching the application...

:: Run the Streamlit app
streamlit run app.py
pause