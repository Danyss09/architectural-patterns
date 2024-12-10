from flask import Flask
from flask_restx import Api, Resource

# Initialize Flask and Flask-RESTX
app = Flask(__name__)

# Define API with custom Swagger information
api = Api(
    app,
    version='1.0',
    title='Hello World API',
    description='This API returns "Hello World, my name is Daniela Cáceres!"',
    doc='/swagger/',  # Custom path for Swagger UI
)

# Define a simple Resource
@api.route('/')
class HelloWorld(Resource):
    def get(self):
        """
        Returns a hello world message
        ---
        responses:
            200:
                description: A hello world message
                schema:
                    type: string
                    example: 'Hello World, my name is Daniela Cáceres!'
        """
        return 'Hello World, my name is Daniela Cáceres!'

if __name__ == '__main__':
    app.run(debug=True)
