from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags = ['blogs']
)

@router.get('/')
def all():
    return blog.get_all()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog):
    return blog.create(request)

@router.get('/{id}', status_code=200, response_model=schemas.showBlog)
def show(id : int):
    return blog.showBlog(id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request : schemas.Blog):
    return blog.update(id, request)

@router.delete('/{id}')
def destroy(id : int): 
    return blog.delete(id)