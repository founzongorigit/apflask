from flask import Blueprint, request, jsonify
import services.user_service as service

users_bp = Blueprint("users", __name__)

@users_bp.get("/")
def list_users():
    return jsonify(service.get_all_users())

@users_bp.post("/")
def add_user():
    data = request.json
    return jsonify(service.create_user(data)), 201
