from flask import Flask
from flask_restful import Resource
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


# RESOURCE is all about what you are providing through api
# this is a resource, in our case our resources is STUDENTS

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        
        return {'item': None}, 404    # 404 is the data is not found in the server

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201       # 201 status code is for successfult post method
    
# we don't need to define the route differently when we are using api
# instead we should define that in this way, after the adding resouces we need to
# tell the route
api.add_resource(Item, '/item/<string:name>') # localhost/student/Jhon


app.run()