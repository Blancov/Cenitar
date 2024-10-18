from flask import Flask, render_template, request
import openai
import requests

app = Flask(__name__)
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    company = request.form['company']
    data = get_company_data(company)
    prompt = f"Analyze the following company data and provide predictions: {data}"
    prediction = get_prediction(prompt)
    return render_template('result.html', prediction=prediction)

def get_company_data(company):
    response = requests.get(f'https://financialmodelingprep.com/api/v3/profile/{company}?apikey=YOUR_FINANCIAL_API_KEY')
    return response.json()

def get_prediction(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


