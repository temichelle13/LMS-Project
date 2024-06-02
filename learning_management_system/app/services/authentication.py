# app/services/authentication.py
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from database import SessionLocal

class AuthenticationService:
    def __init__(self):
        self.db_session = SessionLocal()

    def register_user(self, username, email, password):
        """Registers a new user."""
        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        self.db_session.add(user)
        self.db_session.commit()
        return user

    def authenticate_user(self, username, password):
        """Authenticates a user."""
        user = self.db_session.query(User).filter(User.username == username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

    def logout_user(self, user):
        """Logs out a user."""
        # Placeholder for session management logic
        pass

# Example usage:
# auth_service = AuthenticationService()
# user = auth_service.register_user('username', 'email@example.com', 'password123')
# authenticated_user = auth_service.authenticate_user('username', 'password123')
# if authenticated_user:
#     print(f"Welcome back, {authenticated_user.username}!")
# else:
#     print("Invalid username or password.")
