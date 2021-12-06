from app import app
from app.controller import UserController
from flask import request

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello, World!"

# @app.route('/users')
# def users():
#     return UserController.index()

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()

@app.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)