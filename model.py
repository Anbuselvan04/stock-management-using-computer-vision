# import numpy as np
# import pandas as pd
# from datetime import datetime
# from sklearn.preprocessing import MinMaxScaler
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense
# import json

# # Load JSON data from two files
# with open('initial_stock.json', 'r') as f:
#     initial_stock = json.load(f)

# with open('sold_stock.json', 'r') as f:
#     sold_stock = json.load(f)

# # Convert JSON to DataFrame
# initial_df = pd.DataFrame(initial_stock)
# sold_df = pd.DataFrame(sold_stock)

# # Convert Timestamp to datetime
# initial_df['Timestamp'] = pd.to_datetime(initial_df['Timestamp'])
# sold_df['Timestamp'] = pd.to_datetime(sold_df['Timestamp'])

# # Merge data based on ID, Category, and Model to compare timestamps
# merged_df = pd.merge(initial_df, sold_df, on=['Category', 'Model', 'ID'], suffixes=('_initial', '_sold'))

# # Calculate Time Delta (days between initial stock and sold stock)
# merged_df['Days_Sold'] = (merged_df['Timestamp_sold'] - merged_df['Timestamp_initial']).dt.days

# # For simplicity, assume "1 unit sold per ID per period" since quantity is not given
# merged_df['Quantity_Sold'] = 1

# # Prepare data for LSTM (use Days_Sold as time feature)
# data = merged_df[['Days_Sold', 'Quantity_Sold']].values

# # Normalize the data
# scaler = MinMaxScaler(feature_range=(0, 1))
# scaled_data = scaler.fit_transform(data)

# # Create sequences for LSTM (X: Days_Sold, y: Quantity_Sold)
# def create_sequences(data, seq_length):
#     X, y = [], []
#     for i in range(len(data) - seq_length):
#         X.append(data[i:i + seq_length, 0])  # Days_Sold as feature
#         y.append(data[i + seq_length, 1])    # Predict Quantity_Sold
#     return np.array(X), np.array(y)

# seq_length = 1  # Since we have few records, set sequence length to 1
# X, y = create_sequences(scaled_data, seq_length)

# # Reshape for LSTM input (samples, time steps, features)
# X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# # Build LSTM Model
# model = Sequential()
# model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
# model.add(LSTM(units=50, return_sequences=False))
# model.add(Dense(units=25))
# model.add(Dense(units=1))  # Output Quantity Sold

# # Compile the model
# model.compile(optimizer='adam', loss='mean_squared_error')

# # Train the model
# model.fit(X, y, batch_size=1, epochs=10)

# # Future prediction (example)
# future_days = np.array([[30]])  # Predict for 30 days out (just an example)

# # MinMaxScaler expects two features (Days_Sold and Quantity_Sold), 
# # so we need to expand future_days to match the same structure
# future_days_scaled = scaler.transform(np.concatenate((future_days, np.zeros((future_days.shape[0], 1))), axis=1))

# # Reshape for LSTM input
# future_days_reshaped = np.reshape(future_days_scaled[:, 0], (future_days_scaled.shape[0], 1, 1))  # Only use Days_Sold for prediction
# predicted_quantity = model.predict(future_days_reshaped)

# # Inverse transform to get the actual value, appending dummy second feature (Quantity_Sold)
# predicted_quantity = scaler.inverse_transform(np.concatenate((future_days, predicted_quantity), axis=1))[:, 1]

# print(f"Predicted quantity to be sold in 30 days: {predicted_quantity[0]}")
#-----------------------------------------------------------------------------------------------------------------------------------

import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from datetime import datetime

# Load initial stock data
with open('initial_stock.json', 'r') as f:
    initial_stock = json.load(f)

# Load sold stock data
with open('sold_stock.json', 'r') as f:
    sold_stock = json.load(f)

# Convert to DataFrames
initial_df = pd.DataFrame(initial_stock)
sold_df = pd.DataFrame(sold_stock)

# Convert 'Date' to datetime
initial_df['Date'] = pd.to_datetime(initial_df['Date'])
sold_df['Date'] = pd.to_datetime(sold_df['Date'])

# Count quantity sold by model
sales_data = sold_df.groupby(['Category', 'Model']).size().reset_index(name='Quantity Sold')

# Merge initial stock with sales data
merged_data = pd.merge(initial_df, sales_data, on=['Category', 'Model'], how='left')
merged_data['Quantity Sold'] = merged_data['Quantity Sold'].fillna(0)

# Prepare data for LSTM
# Use only relevant features and sort by date
merged_data = merged_data[['Date', 'Quantity Sold']].sort_values('Date')
merged_data['Date'] = merged_data['Date'].map(datetime.toordinal)  # Convert date to ordinal

# Scale the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(merged_data['Quantity Sold'].values.reshape(-1, 1))

# Create sequences for LSTM
def create_dataset(data, time_step=1):
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        a = data[i:(i + time_step), 0]
        X.append(a)
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)

time_step = 7  # Number of days for predicting future sales
X, y = create_dataset(scaled_data, time_step)

# Reshape X to be [samples, time steps, features]
X = X.reshape(X.shape[0], X.shape[1], 1)

# Build the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(1))

# Compile and train the model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=50, batch_size=32)

# Predict future sales for the next 30 days
predictions = model.predict(X[-time_step:])  # Use the last 'time_step' days for prediction
predicted_sales = scaler.inverse_transform(predictions)  # Rescale back to original

# Output predicted sales
for i, quantity in enumerate(predicted_sales):
    print(f"Day {i+1}: Predicted Quantity Sold = {quantity[0]:.2f}")
