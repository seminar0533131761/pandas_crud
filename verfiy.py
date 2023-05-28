# from flask import Flask, jsonify, request
# from flask_jwt import JWT, jwt_required, current_identity
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your own secret key
#
# # Mock user and authentication functions
# class User(object):
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password
#
# users = [
#     User(1, 'chani', '1'),
#     User(2, 'shani', '2')
# ]
#
# def authenticate(username, password):
#     for user in users:
#         if user.username == username and user.password == password:
#             return user
#
# def identity(payload):
#     user_id = payload['identity']
#     for user in users:
#         if user.id == user_id:
#             return user
#
# jwt = JWT(app, authenticate, identity)
#
# # Protected route
# @app.route('/protected')
# @jwt_required()
# def protected():
#     return jsonify({'message': 'This is a protected route', 'user_id': current_identity.id})
#
#
# app.run()
