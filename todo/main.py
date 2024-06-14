from fastapi import FastAPI ,Depends
import uvicorn
from typing import Annotated

app = FastAPI()

def common_parametrs(p:int | None = None, name:str="Nasir"):
    return {"p":p, "name":name}

@app.get("/")
def rout():
    return "Rout path runing successfullay"

@app.get("/nasir/")
def nasir():
    return {"name":"Nasir Abbas"}

# dependancy injection: Means the function that depends on other function
@app.get("/items")
def checking(common:Annotated[dict, Depends(common_parametrs)]):
    return common

@app.get("/users")
def read_users(common:Annotated[dict, Depends(common_parametrs)]):
    return common["name"]


def start():
    uvicorn.run("todo.main:app", host="127.0.0.1", port= 8080, reload=True)


