import pandas as pd
import os

# Get the current working directory
current_dir = os.getcwd()
print("Current Working Directory:", current_dir)

# Construct the correct file path dynamically
file_path = os.path.join(current_dir, "data", "sales_data.csv")

# Check whether the file exists before reading
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print(df.head())
else:
    print(f"❌ File not found at: {file_path}")
    print("👉 Check if the 'data' folder and 'sales_data.csv' file exist!")
Prepartion



import pandas as pd

data = {
    'product': ['A', 'B', 'C'],
    'sales': [100, None, 300]
}

df = pd.DataFrame(data)
total_sales = df['sales'].sum()
print("Total Sales:", total_sales)
