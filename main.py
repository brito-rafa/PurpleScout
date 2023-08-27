from flask import Flask, render_template, request, redirect, url_for, flash, session

# Create app
app = Flask(__name__)

# Index
@app.route('/')
def index():
    return render_template('home.html')

# Home
@app.route('/home.html')
def home():
    return render_template('home.html')

# Scout
@app.route('/scout.html')
def scout():
    return render_template('scout.html')

# Run app  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)