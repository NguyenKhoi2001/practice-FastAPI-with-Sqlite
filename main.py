from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name':'Khoi'}}

@app.get('/about')
def about():
    return {'data':{'page':'about page'}}