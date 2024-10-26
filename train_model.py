import pickle
from sklearn.linear_model import LinearRegression

# Example model training with 4 features
model = LinearRegression()
X = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]  # Replace with your actual data
y = [10, 15, 20]  # Replace with your actual target values
model.fit(X, y)

# Save the model
with open('C:\\Users\\mohammed ansar ur ra\\renewable_energy_project\\models\\energy_model.pkl', 'wb') as f:
    pickle.dump(model, f)
