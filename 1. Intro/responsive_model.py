from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()

@app.get('/test', response_class=JSONResponse)
def test_endpoint():
    return {
        'test key': 'some value',
        'anather key': 'anather value',
        4 : 'some more value',
        5:4,

    }

@app.get('/', response_class=PlainTextResponse)
def home():
    return 'welcome'
