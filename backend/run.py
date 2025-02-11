from app import create_app, db
from app.models import User
import os

app = create_app()

def init_db():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        try:
            # Create admin user if it doesn't exist
            if not User.query.filter_by(email='admin@example.com').first():
                admin = User(
                    username='admin',
                    email='admin@example.com'
                )
                admin.set_password('adminpassword')
                db.session.add(admin)
                db.session.commit()
                print("Admin user created successfully!")
        except Exception as e:
            print(f"Error creating admin user: {e}")
            db.session.rollback()

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=os.environ.get('FLASK_ENV') == 'development'
    )
