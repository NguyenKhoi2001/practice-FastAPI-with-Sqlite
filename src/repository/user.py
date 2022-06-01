from fastapi import HTTPException, status
from pydantic import parse_obj_as
from typing import List
from src.utils import schemas
from src.utils.database import selectQuery, insertQuery, deleteQuery
from src.security import hashing


def create(request: schemas.User):
    query = '''
    insert into user (name, email, password)
    values ("%s","%s","%s");
    ''' %(request.name, request.email, hashing.Hash.bcrypt(request.password))
    # new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    insertQuery(query)
    user = selectQuery('SELECT * FROM user ORDER BY id DESC LIMIT 0, 1')
    userCreate = user[0]
    res = [{"name": userCreate[1], "email": userCreate[2]}]
    res = parse_obj_as(List[schemas.showUserBase],res)
    return res[0]

def show(id: int):
    query = '''
    select *
    from user
    where user.id = %s
    ''' % id
    user = selectQuery(query)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no user with id {id} found')
    users = user[0]
    res = [{"name": users[1], "email": users[2]}]
    res = parse_obj_as(List[schemas.showUserBase],res)
    return res[0]

def deleteUser(id: int):
    user = show(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no user with id {id} found')
    query = '''
    delete from user
    where user.id = %s
    ''' %id
    deleteQuery(query)
    return 'done'
