import jwt
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN

from app.user.service import crud_user
from app.api.utils.db import get_db
from app.user.models import User
from app.base.schemas import TokenPayload
from app.security import SECRET_KEY, ALGORITHM

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


def get_current_user(
    db: Session = Depends(get_db), token: str = Security(reusable_oauth2)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    user = crud_user.get(db, id=token_data.user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
