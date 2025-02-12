import pandas as pd
import os

def load_data(file_path):
    """Load sales data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully!")
        print("📌 Columns in the dataset:", df.columns.tolist())  # Debug: Show column names
        return df
    except FileNotFoundError:
        print(f"❌ Error: File not found -> {file_path}")
        exit(1)

def clean_data(df):
    """Clean the sales data."""
    # Standardize column names (remove spaces, convert to lowercase)
    df.columns = df.columns.str.strip().str.lower()
    
    # Rename 'order date' to 'date' for consistency
    if 'order date' in df.columns:
        df.rename(columns={'order date': 'date'}, inplace=True)
    else:
        raise ValueError("❌ Error: The dataset does not contain an 'Order Date' column. Please check the CSV file.")

    # Handle missing values using forward-fill
    df.ffill(inplace=True)
    
    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Remove rows where 'date' could not be converted
    df = df.dropna(subset=['date'])

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    return df

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Define file paths
    INPUT_FILE = os.path.join(BASE_DIR, 'data', 'sales_data.csv')
    OUTPUT_FILE = os.path.join(BASE_DIR, 'data', 'cleaned_sales_data.csv')

    # Ensure the input file exists
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: File not found -> {INPUT_FILE}")
        exit(1)

    # Load data
    sales_data = load_data(INPUT_FILE)

    # Clean data
    cleaned_data = clean_data(sales_data)
    
    # Save the cleaned data
    cleaned_data.to_csv(OUTPUT_FILE, index=False)
    
    print("✅ Cleaned data saved successfully!")
    print(cleaned_data.head())
