import json
from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI()

json1 = '{"name": "John", "age": 30, "city": "New York"}'
json_dict = json.loads(json1)

print(json_dict)
#/go-to-home 경로로 GET 요청을 보내면, 
#사용자를 /home으로 리다이렉트하도록 FastAPI 코드를 작성해라

@app.get("/go-to-home")
def go_to_home():
    return RedirectResponse(url="/home")


class FormData(BaseModel):
    username: str
    age: int

@app.post("/submit-form")
async def submit_form(form: FormData):
    username = form.username
    age = form.age
    return RedirectResponse(
        url=f"/user-info/{username}?age={age}",
        status_code=status.HTTP_303_SEE_OTHER,
    )

@app.get("/user-info/{username}")
async def user_info(username: str, request: Request):
  age = request.query_params.get("age")
  return HTMLResponse(content=f"<h1>User Info</h1><p>Username: {username}</p><p>Age: {age}</p>")