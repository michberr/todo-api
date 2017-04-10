from flask import Flask, request, abort
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from models import Todo, db, connect_to_db


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

#####################################################
#               Define Resources                    #
#####################################################


class TodoView(Resource):

    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
                                 type=str,
                                 required=True,
                                 help='No name provided',
                                 location='json')
        self.parser.add_argument('description',
                                 type=str,
                                 default="",
                                 location='json')

    # When we return a Todo object from an api method,
    # these fields will appear in the response.
    # We can also cast data to a different type here
    # by specifying as 'fields.Integer' or fields.String
    todo_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'description': fields.String
    }

    @marshal_with(todo_fields)
    def get(self, todo_id):
        """Retrieve a todo item by id"""

        todo = Todo.query.get(todo_id)

        if not todo:
            abort(404, "That id does not exist in the database")

        return todo

    @marshal_with(todo_fields)
    def post(self):
        """Create a new todo item"""

        args = self.parser.parse_args()
        print args

        todo = Todo(name=args['name'],
                    description=args['description'])

        db.session.add(todo)
        db.session.commit()

        return todo

    @marshal_with(todo_fields)
    def put(self, todo_id):
        """Update a todo item"""

        args = self.parser.parse_args()

        todo = Todo.query.get(todo_id)

        if not todo:
            abort(404, "That id does not exist in the database")

        todo.name = args["name"]
        todo.description = args["description"]
        db.session.commit()

        return todo


#####################################################
#                Add resources to API               #
#####################################################
api.add_resource(TodoView,
                 '/todo/',
                 '/todo/<int:todo_id>')


#####################################################
#                      Run App                      #
#####################################################
if __name__ == '__main__':

    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0', debug=True)
