from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():  #must be right underneath
    return render_template('index.html')

@app.route('/about')
def about():  #must be right underneath
    return render_template('about.html')

app.run(debug=True)