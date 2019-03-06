from flask import Flask, jsonify, request, render_template

app = Flask(__name__) #creating a object of Flask using a unique name

stores = [
    {
        'name': 'My wonderful store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST']) #route where the server will receive a request
def create_store():
    request_data = request.get_json() #this request is that was made for the browser
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    # if the store name matches, return it
    # if none match, return a error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify(stores)

# POST /store/<string:name>/item  {name: price}
@app.route('/store/<string:name>/item', methods=['POST']) #route where the server will receive a request
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


app.run(port=5000)

