from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/kontakti')
def kontakti():
    return "seit ir kontakti"


if __name__ == '_main_':
    app.run( debug = True)