import unittest
from todo import app
from models import db, connect_to_db, Todo, load_example_data
import requests
import json


class TestAPI(unittest.TestCase):
    """Tests with DB."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///todo_test")

        # Create tables in testdb
        db.create_all()
        load_example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_get_todo(self):
        """Test retrieving todo item from db"""

        result = self.client.get("/todo/1")
        self.assertEqual(result.status_code, 200)

        data = json.loads(result.data)
        self.assertEqual(data["description"], "Buy eggs and spinach")
        self.assertEqual(data["name"], "Buy groceries")

    def test_post_todo(self):
        """Test posting a todo item"""

        result = self.client.post("/todo/",
                                  data=json.dumps({
                                    "name": "Clean apartment",
                                    "description": "Sweep, do dishes"
                                  }),
                                  content_type='application/json')

        self.assertEqual(result.status_code, 200)

        # Check for the item in the db
        todo = Todo.query.get(2)
        self.assertEqual(todo.name, "Clean apartment")
        self.assertEqual(todo.description, "Sweep, do dishes")


if __name__ == '__main__':
    unittest.main()
