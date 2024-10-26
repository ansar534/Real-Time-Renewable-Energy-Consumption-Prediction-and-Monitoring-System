This project provides an end-to-end solution for predicting and monitoring energy consumption, focusing on renewable energy sources. Using machine learning and real-time data, the project helps users monitor consumption, calculate potential savings, and receive alerts when consumption surpasses predefined thresholds
Overview
This application predicts energy consumption based on environmental factors such as temperature, humidity, wind speed, and atmospheric pressure. By providing real-time visualizations and integrating a notification system, it empowers users to make informed decisions, optimize their energy usage, and maximize savings through renewable energy.

Features
Energy Consumption Prediction: Predicts consumption based on temperature, humidity, wind speed, and pressure.
Real-time Monitoring: Displays live data for energy production and grid stability through an interactive map.
Alert System: Sends email alerts when predicted consumption exceeds a specified threshold.
Savings Calculator: Estimates cost savings from switching to renewable sources.
Architecture
The project is structured as follows:

Data Preprocessing: Cleaning, feature selection, and normalization.
Exploratory Data Analysis (EDA): Visual insights into energy consumption trends.
Feature Engineering: Creating new features to improve model performance.
Machine Learning Model: A linear regression model for prediction.
Real-time Data Visualization: Map-based visualization using Leaflet.js and OpenStreetMap API.
Dataset
The dataset includes:

Environmental data (temperature, humidity, wind speed, pressure).
Renewable energy production statistics.
Geographical data for energy sources.
