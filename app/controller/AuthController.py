from app.model.user import Users
from app import response, app
from flask import request

def login():
    try:
        email = request.json['email']
        password = request.json['password']

        user = Users.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Empty....')

        if not user.checkPassword(password):
            return response.badRequest([], 'Your credentials is invalid')

        data = singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }

    return data