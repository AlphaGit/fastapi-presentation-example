from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

class UserModel(BaseModel):
    id: int = Field(
        description="Id of the user"
    )
    username: str = Field(
        min_length=3,
        max_length=200,
        example="jdoe",
        description="Username of the user",
    )
    email: str = Field(
        min_length=3,
        max_length=200,
        example="user@example.com",
        description="Email of the user",
    )

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserModel:
    # in a real app, we'd do some real validation of the token here
    return UserModel(id=1, username=token, email="jdoe@example.com")

@router.get('/me', response_model=UserModel)
async def get_me(current_user: UserModel = Depends(get_current_user)):
    return current_user

@router.post('/login', dependencies=[])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # in a real app, we'd do some real authentication here
    return {"access_token": f"Token for {form_data.username}", "token_type": "bearer"}
