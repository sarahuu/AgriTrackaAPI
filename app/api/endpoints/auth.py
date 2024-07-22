from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from app.schemas.auth import Token,LoginForm
from app.core.config import settings
from app.core.auth import verify_access_token,verify_password,create_access_token,get_password_hash,oauth2_scheme


router = APIRouter()


@router.post('/login', status_code=200, response_model=Token)
def login(form_data:LoginForm):
    """
    Authenticates a user and issues an access token.

    **Parameters:**
    - `form_data` (LoginForm): Contains `username` and `password`.

    **Returns:**
    - `Token`: Contains `access_token` and `token_type` ('bearer').

    **Errors:**
    - `HTTP 401 Unauthorized`: For invalid username or password.

    **Authentication:**
    - No authentication required to access this endpoint.
    """

    if form_data.username != settings.API_USERNAME or not verify_password(form_data.password, get_password_hash(settings.API_PASSWORD)):
        print(settings.API_USERNAME)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password", headers={"WWW-Aunthenticate":"Bearer"})
    access_token = create_access_token(data={'sub':form_data.username})
    return {'access_token':access_token,'token_type':'bearer'}