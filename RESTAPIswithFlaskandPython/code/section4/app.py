from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required


from security import authenticate, identity


# Resources is thing that api can return , create, delete and so on
# Resource are usually mapped into databases tables as well.


#Config the api
app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth


items = []


#Defining our resource
#Every resource has to be a class
class Item(Resource):

    #added this 2 lines (parser) due to this criteria will be in 'post' and 'put'
    #notice this properties belong to the Item class, so that's why we need to apply Item.parser.parse_args()
    #see 'data = Item.parser.parse_args()' in post method, same with 'put' method
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )


    @jwt_required()
    #method that the resource is going to accept(get), also could be (post, delete, etc.)
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        #doing the same below:
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400



        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):

        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')  #This is my endpoint, this the way how to be access
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True) # port 5000 is by default, just put it by explaining


