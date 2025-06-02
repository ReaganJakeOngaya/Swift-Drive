from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Car
from app.extensions import db

cars_bp = Blueprint('cars', __name__)

@cars_bp.route("/", methods=["GET"])
def get_all_cars():
    cars = Car.query.all()
    return jsonify([{
        "id": car.id,
        "name": car.name,
        "brand": car.brand,
        "price": car.price,
        "image_url": car.image_url,
        "model_url": car.model_url,
        "description": car.description
    } for car in cars])

@cars_bp.route("/", methods=["POST"])
@jwt_required()
def add_car():
    user = get_jwt_identity()
    if not user["is_admin"]:
        return jsonify({"message": "Admins only"}), 403
    data = request.get_json()
    car = Car(**data)
    db.session.add(car)
    db.session.commit()
    return jsonify({"message": "Car added"}), 201

@cars_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_car(id):
    user = get_jwt_identity()
    if not user["is_admin"]:
        return jsonify({"message": "Admins only"}), 403
    data = request.get_json()
    car = Car.query.get_or_404(id)
    for key, value in data.items():
        setattr(car, key, value)
    db.session.commit()
    return jsonify({"message": "Car updated"})

@cars_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_car(id):
    user = get_jwt_identity()
    if not user["is_admin"]:
        return jsonify({"message": "Admins only"}), 403
    car = Car.query.get_or_404(id)
    db.session.delete(car)
    db.session.commit()
    return jsonify({"message": "Car deleted"})
