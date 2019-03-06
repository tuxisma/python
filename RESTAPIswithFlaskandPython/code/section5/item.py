from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
import json

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
        #commenting the next lines due to now we are using a database
        # item = next(filter(lambda x: x['name'] == name, items), None)
        # return {'item': item}, 200 if item else 404

        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        # now we are using a database
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    @jwt_required()
    def post(self, name):
        # if next(filter(lambda x: x['name'] == name, items), None):
        #     return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # if Item.find_by_name(name):
        # or
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400


        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}

        try:
            self.insert(item)
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

    @jwt_required()
    def delete(self, name):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):

        data = Item.parser.parse_args()

        item = self.find_by_name(name)

        updated_item = {'name': name, 'price': data['price']}

        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {"message": "An error occurred updating the item."}, 500
        return updated_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})


        connection.close()

        return {'items': items}, 201

