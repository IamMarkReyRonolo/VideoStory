
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher():
    def __init__(self):
        pass      

    def hash_password(self, password: str):
        password_encoded = password.encode('utf-8')        
        return pwd_context.hash(password_encoded)                
    
    def verify_password(self, login_password, original_password):
        matched: bool = False
        try:                                       
            if pwd_context.verify(login_password.encode('utf-8'), original_password.encode('utf-8')):
                matched = True
        except Exception as error:
            matched = False    
        return matched