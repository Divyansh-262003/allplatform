from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.auth import bp
from app.models import User
from app import db
import datetime

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    if not all(k in data for k in ['username', 'email', 'password']):
        return jsonify({"error": "Missing required fields"}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400
        
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username already taken"}), 400
    
    user = User(
        username=data['username'],
        email=data['email']
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        "message": "User created successfully",
        "user": user.to_dict()
    }), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not all(k in data for k in ['email', 'password']):
        return jsonify({"error": "Missing email or password"}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    
    if user and user.check_password(data['password']):
        access_token = create_access_token(
            identity=str(user.id),  # Convert user.id to string
            expires_delta=datetime.timedelta(days=1)
        )
        return jsonify({
            "token": access_token,
            "user": user.to_dict()
        }), 200
    
    return jsonify({"error": "Invalid email or password"}), 401

@bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()
    user = User.query.get(int(current_user_id))
    
    if not user:
        return jsonify({"error": "User not found"}), 404
        
    return jsonify(user.to_dict()), 200
