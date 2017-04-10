from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Todo(db.Model):
    """A ToDo class"""

    __tablename__ = "todos"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        """Display when printing a ToDo object"""

        return "<ToDo: {}>".format(self.name)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

###############################################################


def connect_to_db(app, db_uri="postgresql:///todo"):
    """Connect the database to Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def load_example_data():
    """Example data for testing"""

    todo = Todo(name="Buy groceries",
                description="Buy eggs and spinach")

    db.session.add(todo)
    db.session.commit()

if __name__ == "__main__":

    # Work with database directly if run interactively
    from todo import app
    connect_to_db(app)

    # Create all tables if they don't already exist
    db.create_all()

    print "Connected to DB."
