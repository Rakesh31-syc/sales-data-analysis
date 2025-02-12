import os
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

# Get the base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path for the cleaned data file
cleaned_data_path = os.path.join(BASE_DIR, 'data', 'cleaned_sales_data.csv')

# Check if file exists
if not os.path.exists(cleaned_data_path):
    print(f"❌ Error: {cleaned_data_path} not found. Please ensure it exists.")
    exit(1)

# Load the cleaned data
cleaned_data = pd.read_csv(cleaned_data_path)
print(f"✅ Loaded data from: {cleaned_data_path}")
