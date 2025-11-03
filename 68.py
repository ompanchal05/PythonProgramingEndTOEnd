#CODE FOR FLASK WEB APPLICATION

from flask import Flask

# Create a Flask object
app = Flask(__name__)

# Define a route (URL)
@app.route('/')
def home():
    return "Welcome to Om Panchal’s Flask App!"

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
