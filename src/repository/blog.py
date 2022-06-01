from fastapi import HTTPException, status
from logging import raiseExceptions
from src.utils.database import selectQuery, insertQuery, deleteQuery, updateQuery
from src.utils import schemas
from src.repository import user
from pydantic import parse_obj_as
from typing import List

def get_all():
    query = '''
    select *
    from blog
    '''
    blogs = selectQuery(query)
    res = []
    for eachBlog in blogs:
        blogUser = findUser(eachBlog[-1])
        blogInList = list(eachBlog)
        blogInList[-1] = blogUser
        res.append(blogInList)
    blogs = res
    res = []
    for eachBlog in blogs:
        res.append({'tittle':eachBlog[1],'body':eachBlog[2],'creator':eachBlog[3]})
    res = parse_obj_as(List[schemas.showBlog],res)
    return res

def create(request: schemas.Blog):
    query = '''
    insert into blog (tittle, body, user_id)
    values ("%s","%s","%s");
    ''' %(request.tittle, request.body, request.user_id)
    # new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    insertQuery(query)
    blog = selectQuery('SELECT * FROM blog ORDER BY id DESC LIMIT 0, 1')
    blog = blog[0]
    res = [{'tittle':blog[1],'body':blog[2],'creator':findUser(request.user_id)}]
    res = parse_obj_as(List[schemas.showBlog],res)
    return res[0]

def showBlog(id: int):
    query = '''
    select *
    from blog
    where blog.id = %s
    ''' % id
    blog = selectQuery(query)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no blog with id {id} found')
    blog = blog[0]
    res = [{'tittle':blog[1],'body':blog[2],'creator':findUser(findUserID(id))}]
    res = parse_obj_as(List[schemas.showBlog],res)
    return res[0]

def update(id: int, request: schemas.Blog):
    blog = showBlog(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} is not found')

    query = '''
    update blog
    set tittle = "%s" , body = "%s"
    where id = "%s"
    ''' %(request.tittle, request.body, id)
    updateQuery(query)
    newBlog = showBlog(id)
    showUpdate = [blog,newBlog]
    return showUpdate

def delete(id: int):
    blog = showBlog(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} is not found')
    query='''
    delete from blog
    where id = %s
    ''' %id
    try:
        deleteQuery(query)
    except:
        raiseExceptions('query erorr')
    else:
        return 'done'

def findUser(id: int):
    blogUser = user.show(id)
    return blogUser # return user model

def findUserID(id: int):
    query='''
    select user_id
    from blog
    where id = %s
    ''' %id
    userID = selectQuery(query)[0][0] #chang from {(1,)} -> int
    return userID