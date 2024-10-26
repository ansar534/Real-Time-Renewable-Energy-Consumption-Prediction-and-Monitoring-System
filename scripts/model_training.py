import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

def model_training():
    # Load the dataset
    data = pd.read_csv('C:/Users/mohammed ansar ur ra/renewable_energy_project/data/combined_data.csv')

    # Check available columns (no need to print)
    # print("Available columns:", data.columns)

    # Drop columns that are not needed or are non-numeric
    columns_to_drop = ['time', 'city_name', 'weather_main', 'weather_description', 'weather_icon']
    columns_to_drop = [col for col in columns_to_drop if col in data.columns]
    X = data.drop(columns=columns_to_drop)
    y = data['total load actual']

    # Identify categorical columns for encoding
    categorical_columns = X.select_dtypes(include=['object']).columns
    numeric_columns = X.select_dtypes(include=['number']).columns

    # Preprocess the data: encode categorical variables and scale numeric variables
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', 'passthrough', numeric_columns),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
        ])

    # Create a pipeline with preprocessing and model training
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('model', LinearRegression())])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model using the pipeline
    pipeline.fit(X_train, y_train)

    # Save the model
    joblib.dump(pipeline, 'C:/Users/mohammed ansar ur ra/renewable_energy_project/models/energy_model.pkl')

    # Print model training results
    print("Model training completed.")
    print(f"Model score on training set: {pipeline.score(X_train, y_train)}")
    print(f"Model score on test set: {pipeline.score(X_test, y_test)}")

if __name__ == "__main__":
    model_training()
