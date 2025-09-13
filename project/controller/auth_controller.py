from model.user import User
from model.db import db
from flask import session
from datetime import datetime
from flask_jwt_extended import create_access_token
from view.app import bcrypt

def register_user(email: str, password: str) -> User:
    if db.session.query(User).filter_by(email=email).first():
        raise ValueError("O email já está em uso.")
    
    try:
        password_hash = bcrypt.generate_password_hash(password)
        new_user = User(email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except Exception as e:
        db.session.rollback()
        raise ValueError("Erro ao registrar usuário.") from e

#TODO: Change JWT SECRET_KEY to production configuration file
def authenticate_user(email: str, password: str) -> User:
    user = db.session.query(User).filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password_hash, password):
        session['user_id'] = user.id
        user.last_interaction = datetime.now()
        db.session.commit()
        access_token = create_access_token(identity=str(user.id))
        return access_token
    
    else:
        raise ValueError("Credenciais inválidas.")
