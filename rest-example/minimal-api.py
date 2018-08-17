from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        print(request.data)
        todos[todo_id] = request.data.json()
        return {todo_id: todos[todo_id]}

class HelloWorld(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}


class Todo1(Resource):
    def get(self,todo_id):
        # Default to 200 OK
        return {'task': 'Hello world'}

class Todo2(Resource):
    def get(self,todo_id):
        print(todo_id)
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

class Todo3(Resource):
    def get(self,todo_id):
        # Set the response code to 201 and return custom headers
        print(todo_id)
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

# api.add_resource(TodoSimple, '/<string:todo_id>')
# api.add_resource(Todo1, '/Todo1/<string:todo_id>')
# api.add_resource(Todo2, '/Todo2/<string:todo_id>')
# api.add_resource(Todo3, '/Todo3/<string:todo_id>')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
