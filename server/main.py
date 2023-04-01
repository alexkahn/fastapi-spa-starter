from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_sub():
    return {"message": "Hello World from sub app"}


@app.get("/me")
def get_me():
    return {"message": "Hello, it me."}
