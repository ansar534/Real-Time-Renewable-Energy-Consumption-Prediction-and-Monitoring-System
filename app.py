from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

app = Flask(__name__)

# Load the trained model
with open('C:\\Users\\mohammed ansar ur ra\\renewable_energy_project\\models\\energy_model.pkl', 'rb') as f:
    model = pickle.load(f)

def send_email_alert(to_email, predicted_value, threshold):
    from_email = 'thelectricity76@gmail.com'
    from_password = 'uboj xbwt hwle knyz'
    
    subject = "Energy Consumption Alert"
    body = f"Your predicted energy consumption is {predicted_value:.2f} MW, which exceeds your set threshold of {threshold:.2f} MW."
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

@app.route('/')
def index():
    # Example real-time data (this would be replaced by actual live data in a real-world scenario)
    energy_sources = {
        'Solar': random.uniform(50, 100),
        'Wind': random.uniform(20, 80),
        'Hydro': random.uniform(30, 90),
        'Geothermal': random.uniform(10, 50)
    }
    total_consumption = random.uniform(150, 300)
    grid_stability = random.choice(['Stable', 'Unstable'])

    return render_template('index.html', 
                           energy_sources=energy_sources, 
                           total_consumption=total_consumption,
                           grid_stability=grid_stability)

@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')

@app.route('/predictions')
def predictions():
    return render_template('predictions.html')

@app.route('/predict', methods=['POST'])
def predict():
    temperature = float(request.form['temperature'])
    wind_speed = float(request.form['wind_speed'])
    humidity = float(request.form['humidity'])
    pressure = float(request.form['pressure'])
    threshold = float(request.form['threshold'])
    email = request.form['email']

    # Create a DataFrame for the input
    input_data = pd.DataFrame([[temperature, wind_speed, humidity, pressure]], 
                              columns=['temperature', 'wind_speed', 'humidity', 'pressure'])
    
    # Make prediction
    prediction = model.predict(input_data)[0]

    # Check if the prediction exceeds the threshold
    if prediction > threshold:
        send_email_alert(email, prediction, threshold)

    return render_template('predictions.html', prediction=prediction, 
                           temperature=temperature, wind_speed=wind_speed, 
                           humidity=humidity, pressure=pressure, 
                           threshold=threshold, email=email)

# Route for the Energy Savings Calculator page
@app.route('/savings')
def savings():
    return render_template('savings.html', savings=None)

# Route to calculate and display the savings
@app.route('/calculate_savings', methods=['POST'])
def calculate_savings():
    current_consumption = float(request.form['current_consumption'])
    energy_rate = float(request.form['energy_rate'])
    renewable_source = request.form['renewable_source']
    installation_cost = float(request.form['installation_cost'])

    # Assumptions for savings calculation
    efficiency_improvement = {
        'solar': 0.20,
        'wind': 0.30,
        'hydro': 0.25
    }

    annual_savings = current_consumption * energy_rate * efficiency_improvement[renewable_source] - installation_cost / 10

    return render_template('savings.html', savings=annual_savings)

if __name__ == '__main__':
    app.run(debug=True)
