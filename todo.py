from flask import Flask, request
from flask_restful import Resource, Api
from models import Todo, db, connect_to_db


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


class TodoView(Resource):
    def get(self, todo_id):
        """Retrieve a todo item by id"""

        todo = Todo.query.get(todo_id)
        return todo.as_dict()

    def post(self):
        """Create a new todo item"""

        raw_dict = request.get_json()

        todo = Todo(name=raw_dict['name'],
                    description=raw_dict['description'])

        db.session.add(todo)
        db.session.commit()

        return todo.as_dict()

api.add_resource(TodoView,
                 '/todo/',
                 '/todo/<int:todo_id>')


###############################################################
if __name__ == '__main__':

    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0', debug=True)
