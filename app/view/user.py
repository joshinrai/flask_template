from ..view import *
from app.service.user import UserService

@view.route('/users', methods=['POST', 'GET'])
def users():
    return UserService().getUsers()