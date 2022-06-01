from fastapi import APIRouter
from src.utils import schemas
from src.repository import user

router = APIRouter(
    prefix='/user',
    tags = ['users']
)

@router.post('/')
def create_user(request: schemas.User):
    return user.create(request)


@router.get('/{id}')
def showUser(id: int):
    return user.show(id)

@router.delete('/{id}')
def destroy_User(id : int): 
    return user.deleteUser(id)