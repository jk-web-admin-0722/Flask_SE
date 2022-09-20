from Flask import Flask, render_template

app = flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/kontakti')
def kontakti():
    return "seit ir kontakti"

@app.route('/iepriekseja.html')
def iepriekseja():
    return render_template(iepriekseja.html)

if __name__ == '_main_':

    app.run (debug = True)