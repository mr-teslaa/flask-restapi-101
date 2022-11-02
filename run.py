from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

# as we are server now our - 
# POST = receive data
# GET = send data

stores = [
    {
        'name': 'a car store',
        'items': [
            {
                'name': 'an item like tire',
                'price': 399.55
            }
        ]
    }
]


# POST /store/ data: {name}   will receive a name
@app.route('/store/', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data['name'],
        "items": []
    }

    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>/')
def get_store(name):
    # if the store name matches then return that store
    # othewise return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        
    return jsonify({"message": "store not found"})


# GET /store/    show all store
@app.route('/store/')
def get_stores():
    # in our case stores is a list, json can't be list. it must be object
    # so we need convert this list into a python object and then jsoinfy that
    return jsonify({"stores": stores})    


# POST /store/<string:name>/item {name, price}
@app.route('/store/<string:name>/item/', methods=['POST'])
def create_items_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                "name": request_data['name'],
                "price": request_data['price']
            }

            store['items'].append(new_item)
            return jsonify(new_item)
    
    return jsonify({"message": "store not found"})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item/')
def get_items_store(name):
    # same method as get_store() 
    for store in stores:
        if store['name'] == name:
            return jsonify({"items": store['items']})
        
    return jsonify({"message": "store not found"})