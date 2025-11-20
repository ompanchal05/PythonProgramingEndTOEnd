from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask!"

@app.route("/about")
def about():
    return "This is About Page"

app.run()
