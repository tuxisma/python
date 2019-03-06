from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

#importing two methods from security.py
from security import authenticate, identity
#Importing class(UserRegister) from user.py
from user import UserRegister
from item import Item, ItemList

# Resources is thing that api can return , create, delete and so on
# Resource are usually mapped into databases tables as well.


#Config the api
app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<string:name>')  #This is my endpoint, this the way how to be access
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True) # port 5000 is by default, just put it by explaining


