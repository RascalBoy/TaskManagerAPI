from passlib.hash import pbkdf2_sha256

def get_hash(password:str)->str:
    return pbkdf2_sha256.hash(password)

def verify_hash(plain_password:str, hash_password:str):
    return pbkdf2_sha256.verify(plain_password,hash_password)