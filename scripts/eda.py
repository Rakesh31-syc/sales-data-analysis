# scripts/eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_trends(df):
    """Plot sales trends over time."""
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='date', y='revenue')
    plt.title('Sales Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load cleaned data
    cleaned_data = pd.read_csv('../data/cleaned_sales_data.csv')
    plot_sales_trends(cleaned_data)