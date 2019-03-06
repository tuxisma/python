from flask import Flask
from flask_restful import Resource, Api

# Resources is thing that api can return , create, delete and so on
# Resource are usually mapped into databases tables as well.


#Config the api
app = Flask(__name__)
api = Api(app)

#Every resource has to be a class

items = []

#Defining our resource
class Item(Resource):
    #method that the resource is going to accept(get), also could be (post, delete, etc.)
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item

api.add_resource(Item, '/item/<string:name>')  #This is my endpoint, this the way how to be access

app.run(port=5000) # port 5000 is by default, just put it by explaining


