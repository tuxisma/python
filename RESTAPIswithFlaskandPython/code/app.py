from flask import Flask, request
from flask_restful import Resource, Api, reqparse


# Resources is thing that api can return , create, delete and so on
# Resource are usually mapped into databases tables as well.


#Config the api
app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)


items = []


#Defining our resource
#Every resource has to be a class
class Item(Resource):
    #method that the resource is going to accept(get), also could be (post, delete, etc.)
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        #doing the same below:
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')  #This is my endpoint, this the way how to be access
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True) # port 5000 is by default, just put it by explaining


