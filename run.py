from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from flask_jwt import JWT
from flask_jwt import jwt_required

from security import authenticate
from security import indentity

app = Flask(__name__)
app.secret_key = "asuperstrongkey"
api = Api(app)

jwt = JWT(app, authenticate, indentity)   # it will create a new route '/auth'

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # MAKE THIS LOOP SIMPLER WITH LAMBDA FUNCTION
        # next() is only for getting a single element
        item = next(filter(lambda x: x['name'] == name, items), None)
        
        return {'item': None}, 200 if item else 404   

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {"message": f"An item with name {name} already exist"}
            
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201      
    

class Items(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Items, '/items/')
api.add_resource(Item, '/item/<string:name>') 

app.run(debug=True)