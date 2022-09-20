from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "esi sveiks"

@app.route('/kontakti')
def kontakti():
    return "seit ir kontakti"

if __name__ == '_main_':
    app.run(debug = True)