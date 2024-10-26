import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations():
    # Load the combined preprocessed data
    combined_data = pd.read_csv('C:/Users/mohammed ansar ur ra/renewable_energy_project/data/combined_data.csv')

    # Display the available columns for verification
    print("Available columns:", combined_data.columns)

    # Convert 'time' column to datetime
    combined_data['time'] = pd.to_datetime(combined_data['time'])

    # Exclude non-numeric columns for correlation matrix
    numeric_data = combined_data.select_dtypes(include=[np.number])

    # Correlation matrix
    correlation_matrix = numeric_data.corr()
    plt.figure(figsize=(14, 12))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.tight_layout()

    # Save the heatmap
    if not os.path.exists('C:/Users/mohammed ansar ur ra/renewable_energy_project/static/plots'):
        os.makedirs('C:/Users/mohammed ansar ur ra/renewable_energy_project/static/plots')
    plt.savefig('C:/Users/mohammed ansar ur ra/renewable_energy_project/static/plots/correlation_heatmap.png')
    plt.close()

    # Plot energy consumption over time
    plt.figure(figsize=(14, 7))
    plt.plot(combined_data['time'], combined_data['total load actual'], label='Total Load Actual')
    plt.xlabel('Time')
    plt.ylabel('Total Load Actual')
    plt.title('Energy Consumption Over Time')
    plt.legend()
    plt.tight_layout()
    plt.savefig('C:/Users/mohammed ansar ur ra/renewable_energy_project/static/plots/energy_consumption_over_time.png')
    plt.close()

    # Contribution of each energy source
    energy_sources = ['generation fossil gas', 'generation fossil hard coal', 
                      'generation fossil oil', 'generation hydro run-of-river and poundage', 
                      'generation hydro water reservoir', 'generation nuclear', 'generation other', 
                      'generation other renewable', 'generation solar', 'generation wind onshore']
    
    total_energy = combined_data[energy_sources].sum()
    plt.figure(figsize=(14, 7))
    total_energy.plot(kind='bar')
    plt.xlabel('Energy Source')
    plt.ylabel('Total Energy Generated')
    plt.title('Contribution of Each Energy Source')
    plt.tight_layout()
    plt.savefig('C:/Users/mohammed ansar ur ra/renewable_energy_project/static/plots/energy_sources_contribution.png')
    plt.close()

    # Load vs Temperature (using 'temp' column)
    if 'temp' in combined_data.columns:
        plt.figure(figsize=(14, 7))
        plt.scatter(combined_data['temp'], combined_data['total load actual'])
        plt.xlabel('Temperature')
        plt.ylabel('Total Load Actual')
        plt.title('Load vs Temperature')
        plt.tight_layout()
        plt.savefig('C:/Users/mohammed ansar ur ra/renewable_energy_project/static/plots/load_vs_temperature.png')
        plt.close()
    else:
        print("Temperature column not found in the data.")

if __name__ == "__main__":
    create_visualizations()
