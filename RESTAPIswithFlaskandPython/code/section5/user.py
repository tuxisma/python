import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    #adding "cls" to the class , because of @classmethod
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        #the only way to get data by username, is filter by a tuple: (username,)
        result = cursor.execute(query, (username,))
        #get the firt row
        row = result.fetchone()

        if row:
            # user = User(row[0], row[1], row[2])
            # another way
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


    #adding "cls" to the class , because of @classmethod
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        #the only way to get data by username, is filter by a tuple: (username,)
        result = cursor.execute(query, (_id,))
        #get the firt row
        row = result.fetchone()

        if row:
            # user = User(row[0], row[1], row[2])
            # another way
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):


    parser = reqparse.RequestParser()


    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )


    def post(self):

        data = UserRegister.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        if User.find_by_username(data['username']):
            return {"message":"A user with that username already exists"}, 400

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201


