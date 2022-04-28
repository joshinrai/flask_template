from ..service import *
from app.models.user import UserBean

class UserService():
    def __init__(self):
        self.name = 'user'
    def getUsers(self):
        ret = {}
        try:
            db = mysqlconn()
            data = []
            users = db.query(UserBean).all()
            for item in users:
                a = {
                    'id': item.id,
                    'role': item.role,
                    'username': item.username,
                    'truename': item.truename,
                }
                data.append(a)
            ret = {
                'errcode': 0,
                'data': data,
            }
        except BaseException as err:
            ret = {
                'errcode': 10001,
                'msg': str(err),
            }
        finally:
            db.close()
            return jsonify(ret)
