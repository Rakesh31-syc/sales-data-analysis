# sales-data-analysis

## Project Overview

The Sales Performance Analysis project is a web application designed to analyze sales data, visualize trends, and provide insights into sales performance. The application allows users to explore sales data through interactive charts, filter data by date ranges, and download reports. It aims to help businesses make informed decisions based on historical sales data.

## Features

- **Data Visualization**: Interactive charts displaying sales trends over time.
- **Comparison Charts**: Visualize sales vs. expenses.
- **Monthly Sales Trends**: View total sales revenue on a monthly basis.
- **Sales by Product**: Show which products generate the most sales.
- **Sales Performance by Region**: Analyze sales performance across different regions.
- **Sales Growth Rate**: Visualize the growth rate of sales over time.
- **Customer Segmentation**: Visualize customer segments based on purchasing behavior.
- **Date Range Filters**: Filter sales data based on custom date ranges.
- **Download Reports**: Export sales data as CSV files.

## Technologies Used

- Python
- Flask
- Pandas
- Matplotlib
- Seaborn
- Plotly
- HTML/CSS

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/sales-data-analysis.git
   cd sales-data-analysis
   ```

2. **Install Required Packages**:
   Make sure you have Python installed. Then, create a virtual environment and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Prepare the Data**:
   Ensure you have the `sales_data.csv` file in the `data` directory. You can update this file with your sales data.

4. **Run the Data Cleaning Script**:
   Before running the web application, clean the data:
   ```bash
   python scripts/data_cleaning.py
   ```

5. **Run the Flask Application**:
   Navigate to the `webapp` directory and start the Flask server:
   ```bash
   cd webapp
   python app.py
   ```

6. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:5000/` to access the Sales Performance Analysis application.

## Usage

- Use the main page to view sales trends.
- Filter data by selecting a date range and clicking the "Filter" button.
- Download the sales report by clicking the "Download Sales Report" button.
- View the revenue vs. expenses comparison chart by clicking the "View Revenue vs Expenses" button.
- Explore additional features such as monthly sales trends, sales by product, sales by region, sales growth rate, and customer segmentation.

## Common Commands

- **Run the Data Cleaning Script**: Cleans and prepares the sales data.
  ```bash
  python scripts/data_cleaning.py
  ```

- **Run the Flask Application**: Starts the web server.
  ```bash
  python app.py
  ```

- **Download Sales Report**: Exports the sales data as a CSV file.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.


## Acknowledgments

- Thanks to the open-source community for providing the libraries and tools used in this project.
