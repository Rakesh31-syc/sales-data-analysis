from flask import Flask, render_template, request, make_response
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans

app = Flask(__name__)

# Load cleaned data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the current directory
cleaned_data_path = os.path.join(BASE_DIR, '..', 'data', 'cleaned_sales_data.csv')

try:
    cleaned_data = pd.read_csv(cleaned_data_path)
except FileNotFoundError:
    print(f"❌ Error: {cleaned_data_path} not found. Please ensure it exists.")
    exit(1)

@app.route('/')
def index():
    """Main page displaying sales trends."""
    plot_sales_trends()
    return render_template('index.html')

def plot_sales_trends():
    """Plot sales trends and save the figure."""
    if 'date' not in cleaned_data.columns or 'sales' not in cleaned_data.columns:
        print("❌ Error: 'date' or 'sales' column missing in dataset!")
        return

    # Convert date column to datetime
    cleaned_data['date'] = pd.to_datetime(cleaned_data['date'], errors='coerce')

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=cleaned_data, x='date', y='sales')
    plt.title('Sales Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(os.path.join('static/plots', 'sales_trends.png'))
    plt.close()

    print(f"📊 Sales trends plot saved at: static/plots/sales_trends.png")

@app.route('/comparison')
def comparison():
    """Display revenue vs expenses chart."""
    if 'sales' not in cleaned_data.columns:
        raise ValueError("The 'sales' column is missing from the dataset.")
    
    cleaned_data['expenses'] = cleaned_data['sales'] * 0.6  # Example expense calculation
    fig = px.bar(cleaned_data, x='date', y=['sales', 'expenses'], title='Sales vs Expenses')
    fig.write_html('templates/comparison.html')
    return render_template('comparison.html')

@app.route('/filter', methods=['GET'])
def filter_data():
    """Filter data based on date range."""
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    filtered_data = cleaned_data[(cleaned_data['date'] >= start_date) & (cleaned_data['date'] <= end_date)]
    return render_template('filtered_data.html', data=filtered_data)

@app.route('/download')
def download_report():
    """Download sales report as CSV."""
    output = make_response(cleaned_data.to_csv())
    output.headers["Content-Disposition"] = "attachment; filename=sales_report.csv"
    output.headers["Content-type"] = "text/csv"
    return output

@app.route('/sales-by-product')
def sales_by_product():
    """Display sales by product."""
    product_data = cleaned_data.groupby('product')['sales'].sum().reset_index()
    fig = px.pie(product_data, names='product', values='sales', title='Sales by Product')
    fig.write_html('templates/sales_by_product.html')
    return render_template('sales_by_product.html')

@app.route('/sales-by-region')
def sales_by_region():
    """Display sales performance by region."""
    region_data = cleaned_data.groupby('region')['sales'].sum().reset_index()
    fig = px.bar(region_data, x='region', y='sales', title='Sales Performance by Region')
    fig.write_html('templates/sales_by_region.html')
    return render_template('sales_by_region.html')

@app.route('/sales-growth')
def sales_growth():
    """Display sales growth rate."""
    cleaned_data['growth_rate'] = cleaned_data['sales'].pct_change() * 100
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=cleaned_data, x='date', y='growth_rate')
    plt.title('Sales Growth Rate Over Time')
    plt.xlabel('Date')
    plt.ylabel('Growth Rate (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join('static/plots', 'sales_growth.png'))
    plt.close()
    return render_template('sales_growth.html')

@app.route('/customer-segmentation')
def customer_segmentation():
    """Display customer segmentation."""
    kmeans = KMeans(n_clusters=3)
    cleaned_data['segment'] = kmeans.fit_predict(cleaned_data[['sales', 'quantity_sold']])
    fig = px.scatter(cleaned_data, x='sales', y='quantity_sold', color='segment', title='Customer Segmentation')
    fig.write_html('templates/customer_segmentation.html')
    return render_template('customer_segmentation.html')

if __name__ == '__main__':
    app.run(debug=True)
