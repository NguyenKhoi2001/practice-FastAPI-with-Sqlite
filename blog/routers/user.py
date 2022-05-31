from fastapi import APIRouter
from sqlalchemy.orm import Session
from .. import schemas, models
from ..repository import user
from pydantic import parse_obj_as
from typing import List

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