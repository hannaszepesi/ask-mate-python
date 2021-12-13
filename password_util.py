from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def generate_hashed_password(plain_text_password):
    hashed_password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    return hashed_password

def verify_hashed_password(hashed_password, plain_text_password):
    checked_password = bcrypt.check_password_hash(hashed_password, plain_text_password)
    return checked_password