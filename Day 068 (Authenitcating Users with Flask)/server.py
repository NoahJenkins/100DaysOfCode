from flask import Flask
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, test):
        return {"data": name, "test": test}
    
    def post(self):
        return {"data": "Hello World"}
    
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

if __name__ == '__main__':
    app.run(debug=True)
