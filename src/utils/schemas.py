from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name: str
    email: str
    password: str

class BlogBase(BaseModel):
    tittle: str
    body: str
    user_id: int
    
class Blog(BlogBase):
    class Config():
        orm_mode = True

class showUserBase(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True
    
class showUser(showUserBase):
    blogs: List[Blog] = []
    

class showBlog(BaseModel):
    tittle: str
    body: str
    creator: Optional[showUserBase]
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str
    

