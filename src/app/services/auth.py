import jwt
from jwt.exceptions import ExpiredSignatureError
import json
from datetime import datetime, timedelta

from passlib.hash import sha256_crypt

class PasswordHashing:
    
    @staticmethod
    def craete_hash(password:str):
        return sha256_crypt.encrypt(password)
    
    @staticmethod
    def decode_hash(password:str, hashed_password:str):
        return sha256_crypt.verify(password, hashed_password)


class JWTEncodeDecode:
    
    def __init__(self):
        self.JWT_SECRET = 'secret'
        self.JWT_ALGORITHM = 'HS256'
        self.JWT_EXP_DELTA_SECONDS = 2000
    
    def encode(self, user_id: int):
        try:
            expiry_time = datetime.now() + timedelta(minutes=self.JWT_EXP_DELTA_SECONDS)
            payload_data = {"user_id": user_id, "expiry": str(expiry_time)}
            token = jwt.encode(payload_data, self.JWT_SECRET, self.JWT_ALGORITHM)
        except Exception as e:
            print(e, )
            token = None
        return token
    
    def validate_token(self, token):
        pass
    
    def decode(self, token: str):
        if token:
            try:
                payload = jwt.decode(token, self.JWT_SECRET, self.JWT_ALGORITHM)
                if datetime.strptime(payload['expiry'], "%Y-%m-%d %H:%M:%S.%f") < datetime.now():
                    
                    response = {"message": "token expired", "success": False, 'error': 401}
                else:
                    response = {"message": "decoded succesfully", "success": True, "data":payload}
            except ExpiredSignatureError:
                response = {"jwt_data": 401, "message": "Token signiture", "success": False}
            except Exception as e:
                response = {"error": 401, "message": "Token decoding fail", "success": False}
        else:
            response = {"error": 401, "message": "Token required", "success": False}
        return response