from flask import Flask
from flask_restx import Api, Resource

# Initialize Flask and Flask-RESTX
app = Flask(__name__)
api = Api(app, version='1.0', title='API Example', description='A simple Hello World API')

# Define the root route to display links to both pages
@app.route('/')
def index():
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome!</h1>
        <p>
            <a href="/hello">View the Hello World Page</a>
        </p>
        <p>
            <a href="/swagger/">View the Swagger UI</a>
        </p>
    </body>
    </html>
    """

# Define the "Hello World" page route
@app.route('/hello')
def hello_world():
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello World, my name is Daniela Cáceres!</h1>
    </body>
    </html>
    """

# Define a simple Resource for Swagger UI
@api.route('/api')
class HelloWorld(Resource):
    def get(self):
        """Returns a hello world message in JSON"""
        return {'message': 'Hello World, my name is Daniela Cáceres!'}

if __name__ == '__main__':
    app.run(debug=True)
