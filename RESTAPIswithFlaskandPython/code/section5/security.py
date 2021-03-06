from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    #getting into the mehod within the class(User)
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    # getting into the mehod within the class(User)
    return User.find_by_id(user_id)
