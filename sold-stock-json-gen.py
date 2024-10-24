import json
import random
from datetime import datetime, timedelta

# Load the initial stock data from the previous file
with open('initial_stock.json', 'r') as f:
    initial_stock = json.load(f)

# Function to generate sold stock data
def generate_sold_stock(initial_stock, max_days_ago):
    sold_stock_data = []
    today = datetime.now()
    three_months_ago = today - timedelta(days=max_days_ago)

    for item in initial_stock:
        # Randomly determine if the item was sold
        if random.choice([True, False]):  # Randomly choose if an item was sold
            sold_item = {
                "Category": item["Category"],
                "Model": item["Model"],
                "ID": item["ID"],
                "Date": (three_months_ago + timedelta(days=random.randint(0, max_days_ago))).date().isoformat(),  # Random date within the last 3 months
            }
            sold_stock_data.append(sold_item)

    return sold_stock_data

# Define the parameters
max_days_ago = 90  # Days in the past (3 months)

# Generate sold stock dataset
sold_stock = generate_sold_stock(initial_stock, max_days_ago)

# Save the dataset to a JSON file
with open('sold_stock.json', 'w') as f:
    json.dump(sold_stock, f, indent=4)

print("Sold stock dataset generated successfully!")
