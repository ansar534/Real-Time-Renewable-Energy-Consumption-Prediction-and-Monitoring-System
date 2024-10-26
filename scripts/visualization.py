import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations():
    # Load the dataset
    data = pd.read_csv('C:/Users/mohammed ansar ur ra/renewable_energy_project/data/combined_data.csv')

    # Convert 'time' column to datetime
    data['time'] = pd.to_datetime(data['time'])

    # Set the 'time' column as the index
    data.set_index('time', inplace=True)

    # Plot total load actual over time
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['total load actual'], label='Total Load Actual')
    plt.xlabel('Time')
    plt.ylabel('Total Load Actual')
    plt.title('Total Load Actual Over Time')
    plt.legend()
    plt.savefig('C:/Users/mohammed ansar ur ra/renewable_energy_project/static/total_load_actual_over_time.png')
    plt.close()

    # Correlation heatmap
    numeric_data = data.select_dtypes(include=['number'])
    correlation_matrix = numeric_data.corr()

    plt.figure(figsize=(14, 12))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('C:/Users/mohammed ansar ur ra/renewable_energy_project/static/correlation_heatmap.png')
    plt.close()

    print("Visualizations created and saved.")

if __name__ == "__main__":
    create_visualizations()
