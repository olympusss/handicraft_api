from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 90

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    phone_number: str = payload.get("sub")
    return phone_number



def get_token(header_param):
    header = header_param.headers.get('WWW-Authentication')
    if not header:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error" : True, "body" : "Token not found"})
    if header == "Bearer":
        return header
    else:
        token_data = header.split('Bearer ')[1]
    return token_data
