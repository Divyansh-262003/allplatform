from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api import bp
from app.models import User
import datetime

@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({
        "message": f"Hello {user.username}!",
        "user": user.to_dict()
    }), 200

@bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify({
        "users": [user.to_dict() for user in users]
    }), 200

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat()
    }), 200
