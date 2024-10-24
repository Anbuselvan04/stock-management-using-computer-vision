import json
from datetime import datetime

# Function to generate initial stock data
def generate_initial_stock(categories, models_per_category, items_per_model, date):
    stock_data = []
    date_str = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")

    for category in categories:
        for model_index in range(models_per_category):
            model = f"{category[:2].upper()}{model_index + 1}"  # e.g., WM1, AC1
            for item_index in range(items_per_model):
                stock_item = {
                    "Category": category,
                    "Model": model,
                    "ID": f"{model}{10000 + item_index:02d}",  # Unique ID
                    "Date": date_str  # Common date
                }
                stock_data.append(stock_item)

    return stock_data

# Define categories, models, and date
categories = ["Washing Machine", "AC", "Fridge", "TV", "Home Theatre"]
models_per_category = 3
items_per_model = 20
common_date = "2024-07-06"

# Generate initial stock dataset
initial_stock = generate_initial_stock(categories, models_per_category, items_per_model, common_date)

# Save the dataset to a JSON file
with open('initial_stock.json', 'w') as f:
    json.dump(initial_stock, f, indent=4)

print("Initial stock dataset generated successfully!")
