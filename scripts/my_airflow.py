import pandas as pd
import os
from datetime import datetime
import shutil

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the booster directory
booster_dir = os.path.abspath(os.path.join(current_dir, os.pardir))  # Go up one level from the current directory
data_dir = os.path.join(booster_dir, 'data')
to_process_dir = os.path.join(data_dir, 'toProcess')
result_dir = os.path.join(data_dir, 'result')
processed_dir = os.path.join(data_dir, 'already_processed')

# Ensure the data directory and its subdirectories exist
os.makedirs(data_dir, exist_ok=True)
os.makedirs(to_process_dir, exist_ok=True)
os.makedirs(result_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)

def process_files():
    # Process each file in the toProcess directory
    for filename in os.listdir(to_process_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(to_process_dir, filename)
            
            # Load the CSV file
            df = pd.read_csv(file_path)
            
            # Calculate the average price
            average_price = df['price'].mean()
            
            # Create the result file
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            result_file = os.path.join(result_dir, f'result_{timestamp}.csv')
            result_df = pd.DataFrame({'average_price': [average_price]})
            result_df.to_csv(result_file, index=False)
            
            # Move the processed file to already_processed directory
            shutil.move(file_path, os.path.join(processed_dir, filename))

if __name__ == "__main__":
    process_files()
