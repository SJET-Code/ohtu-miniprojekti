"""Functions to save, encrypt and get user data from the database"""
import secrets
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, OperationalError
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from services.validation_service import ValidationType


class UserRepository:
    def __init__(self, db, validation_service):
        self.db = db
        self.__validation_service = validation_service

    def create_user(self, username, password):
        self.__validation_service.validate(username, ValidationType.USERNAME)
        self.__validation_service.validate(password, ValidationType.PASSWORD)

        hash_value = generate_password_hash(password)
        try:
            sql = text("""INSERT INTO users (username, password_hash)
                       VALUES (:username,:password_hash)""")
            self.db.session.execute(
                sql, {"username": username, "password_hash": hash_value})
            self.db.session.commit()
        except (AttributeError, OperationalError, IntegrityError):
            return False
        return self.login_user(username, password)


    def login_user(self, username, password):
        sql = text("""SELECT id, username, password_hash
                    FROM users 
                    WHERE username = :username""")
        result = self.db.session.execute(sql, {"username": username})
        user = result.fetchone()
        if not user:
            return False
        if check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            session["csrf_token"] = secrets.token_hex(16)
            return True
        return False

    def delete_user(self, user_id):
        sql = self.db.text("DELETE FROM users WHERE id=:user_id")
        self.db.session.execute(sql, {"user_id": user_id})
        self.db.session.commit()

    def logout(self):
        del session["user_id"]

    def user_id(self):
        return session.get("user_id", 0)

    def is_user(self):
        return self.user_id() != 0
