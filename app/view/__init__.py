from flask import Blueprint

view = Blueprint('view', __name__)

@view.route('/hs', methods=['GET', 'POST'])
def hs():
    return 'OK'