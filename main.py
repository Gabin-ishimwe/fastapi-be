from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {
        'message': 'Hello world in FastAPI Version 1'
    }

@app.get('/home')
def home():
    return {
        'message': 'Homepage'
    }
