# todo-api
This is an example of how to build a RESTful API that performs CRUD operations on a Postgres database using Flask and the extension, Flask-RESTful.
The particular application is creating a to-do list.

## Contents:
**todo.py** - Defines the flask app, and the Flask RESTful api endpoints defined on top of it     
**models.py** - Defines the data model, implemented with the Flask SQLAlchemy ORM    
**tests.py** - Testing of API endpoints using Python unittest module

## Resources:
**Designing a RESTful API using Flask-RESTful**     
This is Part 3 of a 3-part blog post by @miguelgrinberg on designing RESTful API's with Flask.
This particular post was useful for explaining how the Flask-RESTful extension differs from using base Flask and demonstrating the additional functionality it brings. There are github links in the article to an API built with both Flask and Flask-RESTful.
https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful      

**Test Driven Development of a Flask API**     
This is a great blog post that uses Flask-RESTful, sqlalchemy, postgres, and the 
nose testing framework to demonstrate how to write and test a simple API that performs CRUD operations. This was a really helpful example,
though in my implementation I used the python unittest module over nose, and made use of `field` and `marshal` functionality in Flask-RESTful. 
http://mkelsey.com/2013/05/15/test-driven-development-of-a-flask-api/

**Flask-RESTful documentation**      
Definitely read through the docs before building your own API. Start with the quickstart API
and then move on to using argument parsing and field marshaling. Be aware that the API reference page
is currently empty, and that there are other typos in the docs. Also, the `reqparse` functionality is being deprecated
in favor of the external `marshmallow` package. I found that there weren't enough examples in the docs to figure out how to fit all of the components together
in one app, but the docs were useful to refer to after looking at other examples. 
https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html#full-example
