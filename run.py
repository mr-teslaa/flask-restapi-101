from re import A
from flask import Flask
from flask_restful import Resource
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


# RESOURCE is all about what you are providing through api
# this is a resource, in our case our resources is STUDENTS

class Student(Resource):
    def get(self, name):
        return {"student": name}

# we don't need to define the route differently when we are using api
# instead we should define that in this way, after the adding resouces we need to
# tell the route
api.add_resource(Student, '/student/<string:name>') # localhost/student/Jhon


app.run()