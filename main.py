from datetime import datetime

from fastapi import FastAPI
from pydantic_model import BookCreate,BookResponse

app = FastAPI()

books : dict[int,dict]={}
counter = 0

@app.get('/books')
def get_books():
    return books

@app.post('/books')
def add_book(note:BookCreate):
    global counter
    counter+=1
    books[counter]={
        "id":counter,
        "added_at":datetime.now(),
        **note.model_dump()
    }
    return books[counter]