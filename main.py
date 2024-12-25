from database import mycursor
from fastapi import FastAPI
from typing import Union


app = FastAPI()


@app.get("/")
def read_root():
    mycursor.execute("SELECT * FROM user")

    myresult = mycursor.fetchall()

    return {"customers": myresult}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

