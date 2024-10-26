import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def preprocess_data():
    # Load data
    energy_data = pd.read_csv('C:/Users/mohammed ansar ur ra/renewable_energy_project/data/energy_dataset.csv')
    weather_data = pd.read_csv('C:/Users/mohammed ansar ur ra/renewable_energy_project/data/weather_features.csv')

    # Convert time columns to datetime
    energy_data['time'] = pd.to_datetime(energy_data['time'], utc=True)
    weather_data['time'] = pd.to_datetime(weather_data['time'], utc=True)

    # Ensure both DataFrames are sorted by time
    energy_data = energy_data.sort_values('time')
    weather_data = weather_data.sort_values('time')

    # Merge data on time
    combined_data = pd.merge_asof(energy_data, weather_data, on='time')

    # Remove columns with no observed values
    combined_data = combined_data.dropna(axis=1, how='all')

    # Impute missing values
    imputer = SimpleImputer(strategy='mean')
    numeric_data = combined_data.select_dtypes(include=[np.number])
    imputed_data = pd.DataFrame(imputer.fit_transform(numeric_data), columns=numeric_data.columns)
    combined_data[numeric_data.columns] = imputed_data

    # Save the preprocessed data
    combined_data.to_csv('C:/Users/mohammed ansar ur ra/renewable_energy_project/data/combined_data.csv', index=False)

if __name__ == "__main__":
    preprocess_data()
