from flask import Flask, render_template, g, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import sqlite3
from config import Config, SQLITE_DB_PATH
from models import db, User
import datetime
import os

app = Flask(__name__)
app.config.from_object(Config)

# Create instance directory if it doesn't exist
os.makedirs(os.path.dirname(SQLITE_DB_PATH), exist_ok=True)

jwt = JWTManager(app)
db.init_app(app)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(SQLITE_DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.db.close()

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400
        
    user = User(
        username=data['username'],
        email=data['email']
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"message": "User created successfully"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and user.check_password(data['password']):
        access_token = create_access_token(
            identity=user.id,
            expires_delta=datetime.timedelta(days=1)
        )
        return jsonify({"token": access_token, "user_id": user.id}), 200
    
    return jsonify({"error": "Invalid email or password"}), 401

@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({"message": f"Hello {user.username}!"}), 200

def init_db():
    with app.app_context():
        db.create_all()
        # You can also execute raw SQL if needed
        conn = get_db()
        conn.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
