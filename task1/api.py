from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route that returns "Hello, World!"
@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

# Run the Flask app on 0.0.0.0 so it's accessible outside the container
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
