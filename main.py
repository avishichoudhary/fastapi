from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class Avi(BaseModel):
  msg : str
  sal:str


@app.get("/")
def home():
  return {"Welcome" : " To the first page"}

@app.get("/second")
def home2():
  return {"Welcome ": "this is my second page"}

''''@app.get("/{name}")
def name(name:str):
  return {"welcome ":name}'''

@app.get("/{num1},{num2}")
def sum(num1: int ,num2: int):
  return {"the sum is ": num1+num2}

@app.post("/p/{name},{msg}")
def po(name: str,msg:str,a1:Avi):
  a1.msg=name
  a1.sal=msg
  return {a1.msg: a1.sal}



