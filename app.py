from flask import Flask, render_template, url_for, request, redirect
import csv
from checkmypass import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/submit_password', methods=['POST', 'GET'])
def submit_password():
    if request.method == 'POST':
        try:
            user_pass = request.form['password']
            msg = main(user_pass)
            return render_template("result.html", msg = msg )
            
        except:
            return "did not save!!!"
    else:
        return 'somthing went wrong. try again'


def write_to_csv(data):
    with open('./database.csv', newline='', mode='a') as database:
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,message])

@app.route('/content_form', methods=['POST', 'GET'])
def content_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('thankyou.html')
        except:
            return "did not save!!!"
    else:
        return 'somthing went wrong. try again'
