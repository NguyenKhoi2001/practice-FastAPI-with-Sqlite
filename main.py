from distutils.log import debug
import sys
sys.path.insert(0, "C:\\Users\\Dell\\Desktop\\python\\FastAPI")

import uvicorn
from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication 

app = FastAPI()

@app.get('/')
def home():
    return {"Hello": "World"}

models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)

if __name__ == '__main__':
    # host = 'localhost' if run local else 'api_gateway'
    uvicorn.run(app, host='0.0.0.0', port=8888, debug=True)