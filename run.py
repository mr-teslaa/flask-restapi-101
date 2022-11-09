from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        
        return {'item': None}, 404   

    def post(self, name):
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