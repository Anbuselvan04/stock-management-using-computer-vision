# import pandas as pd
# import json
# import numpy as np

# # Function to generate synthetic initial stock data
# def generate_initial_stock_data(num_records):
#     categories = ['Washing Machine', 'Refrigerator', 'Home Theatre']
#     models = ['WM1', 'WM2', 'WM3', 'RF1', 'RF2', 'HT1', 'HT2', 'HT3']
    
#     data = []
#     for i in range(num_records):
#         category = np.random.choice(categories)
#         model = np.random.choice(models)
#         model_id = f"{model}{str(i + 1).zfill(4)}"
#         timestamp = pd.Timestamp.now() - pd.Timedelta(days=np.random.randint(0, 30))  # Random timestamp in the last 30 days
#         data.append({
#             'Category': category,
#             'Model': model,
#             'ID': model_id,
#             'Timestamp': timestamp
#         })
    
#     return pd.DataFrame(data)

# # Function to generate synthetic sold stock data
# def generate_sold_stock_data(initial_stock_df, num_sales):
#     sold_data = []
#     for i in range(num_sales):
#         row = initial_stock_df.sample().iloc[0]
#         quantity_sold = np.random.randint(1, 20)  # Random quantity sold between 1 and 20
#         sold_data.append({
#             'Category': row['Category'],
#             'Model': row['Model'],
#             'ID': row['ID'],
#             'Timestamp': row['Timestamp'] + pd.Timedelta(minutes=np.random.randint(1, 60)),  # Random time after initial stock
#             'Quantity Sold': quantity_sold
#         })
    
#     return pd.DataFrame(sold_data)

# # Generate initial stock data
# initial_stock_df = generate_initial_stock_data(num_records=100)

# # Generate sold stock data based on the initial stock
# sold_stock_df = generate_sold_stock_data(initial_stock_df, num_sales=150)

# # Save to JSON files
# initial_stock_df.to_json('initial_stock.json', orient='records', date_format='iso', lines=True)
# sold_stock_df.to_json('sold_stock.json', orient='records', date_format='iso', lines=True)

# print("Synthetic initial stock and sold stock data generated and saved.")
#-----------------------------------------------------------------------------------------------------


# import pandas as pd
# import numpy as np
# import json
# from datetime import datetime, timedelta

# # Set random seed for reproducibility
# np.random.seed(42)

# # Function to generate initial stock data
# def generate_initial_stock():
#     categories = ['Washing Machine', 'Refrigerator', 'Home Theatre']
#     models = {
#         'Washing Machine': ['WM1', 'WM2', 'WM3'],
#         'Refrigerator': ['RF1', 'RF2', 'RF3'],
#         'Home Theatre': ['HT1', 'HT2', 'HT3']
#     }
    
#     initial_stock = []
#     for category in categories:
#         for model in models[category]:
#             for i in range(10):  # 10 items per model
#                 initial_stock.append({
#                     "Category": category,
#                     "Model": model,
#                     "ID": f"{model}{str(i+1).zfill(4)}",
#                     "Timestamp": datetime.now() - timedelta(days=np.random.randint(0, 90)),  # Random within last 90 days
#                     "Quantity Sold": np.random.randint(1, 20)  # Random quantity sold
#                 })
    
#     return initial_stock

# # Function to generate sold stock data
# def generate_sold_stock(initial_stock):
#     sold_stock = []
    
#     for item in initial_stock:
#         if np.random.rand() > 0.5:  # 50% chance of being sold
#             sold_stock.append({
#                 "Category": item['Category'],
#                 "Model": item['Model'],
#                 "ID": item['ID'],
#                 "Timestamp": item['Timestamp'] + timedelta(days=np.random.randint(1, 30)),  # Sold within 30 days of initial
#             })
    
#     return sold_stock

# # Generate datasets
# initial_stock_data = generate_initial_stock()
# sold_stock_data = generate_sold_stock(initial_stock_data)

# # Convert to DataFrame
# initial_stock_df = pd.DataFrame(initial_stock_data)
# sold_stock_df = pd.DataFrame(sold_stock_data)

# # Save to JSON files
# initial_stock_df.to_json('initial_stock.json', orient='records', date_format='iso', lines=False)
# sold_stock_df.to_json('sold_stock.json', orient='records', date_format='iso', lines=False)

# # Print the shapes and content of the DataFrames for verification
# print("Initial Stock DataFrame:")
# print(initial_stock_df.head())
# print("\nSold Stock DataFrame:")
# print(sold_stock_df.head())
#-----------------------------------------------------------------------------------------------------

import json
import random
from datetime import datetime, timedelta

# Function to generate random initial stock data
def generate_initial_stock(num_items=100, start_date="2024-07-01", categories=None, models=None):
    if categories is None:
        categories = ["Washing Machine", "Refrigerator", "Home Theatre"]
    if models is None:
        models = {
            "Washing Machine": ["WM1", "WM2", "WM3"],
            "Refrigerator": ["RF1", "RF2", "RF3"],
            "Home Theatre": ["HT1", "HT2", "HT3"]
        }

    stock_data = []
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")

    for i in range(num_items):
        category = random.choice(categories)
        model = random.choice(models[category])
        
        # Generate a random timestamp within the first 90 days
        timestamp = (start_datetime + timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d %H:%M:%S")

        stock_item = {
            "Category": category,
            "Model": model,
            "ID": f"{model}{1000 + i:04d}",  # Ensure unique ID
            "Timestamp": timestamp  # Timestamp when added to stock
        }
        stock_data.append(stock_item)

    return stock_data

# Function to generate sold stock data based on initial stock
def generate_sold_stock(initial_stock):
    sold_data = []

    for item in initial_stock:
        sold_item = item.copy()

        # Parse the initial timestamp to ensure sold date is after the initial stock date
        stock_timestamp = datetime.strptime(sold_item["Timestamp"], "%Y-%m-%d %H:%M:%S")
        
        # Sold timestamp is 1 to 30 days after the stock timestamp
        sold_timestamp = stock_timestamp + timedelta(days=random.randint(1, 30))
        sold_item["Timestamp"] = sold_timestamp.strftime("%Y-%m-%d %H:%M:%S")

        sold_data.append(sold_item)

    return sold_data

# Generate initial stock and sold stock datasets
initial_stock = generate_initial_stock(num_items=100)
sold_stock = generate_sold_stock(initial_stock)

# Save the datasets to JSON files
with open('initial_stock.json', 'w') as f:
    json.dump(initial_stock, f, indent=4)

with open('sold_stock.json', 'w') as f:
    json.dump(sold_stock, f, indent=4)

print("Initial and sold stock datasets generated successfully!")

