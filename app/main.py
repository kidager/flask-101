from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qQkB51eOJ9evoHhLaM0BaxdUFhNdbdPLuyJv8YrdU'

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/test')
def test():
   return "hello world! Just testing"
