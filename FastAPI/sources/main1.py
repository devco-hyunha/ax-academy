# fastapi : 외부 라이브러리(설치한 패키지)
# fastapi 패키지 안에서 FastAPI라는 클래스만 가져오겠다.
from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel

# FastAPI instance 생성
# 이 객체가 웹 애플리케이션 전체를 대표함
# app는 이제 웹 서버 역할을 할 수 있는 실제 객체가 됨
app = FastAPI()

item_array = [
  {"name": "fast1"},
  {"name": "fast2"},
  {"name": "fast3"}
]

# /경로에 get요청이 들어오면, root함수 실행해!
@app.get("/")  # operation
async def root():
    return { "message" : "Hello World" }
# fastapi는 자동으로 dict -> json 변환해준다.

@app.get("/items")
async def read_items(skip: int = 0, limit: int = None):
  if limit:
    return item_array[skip : skip+limit]
  else:
    return {'not provided'}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
  return {"message": f"Item ID: {item_id}"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
  return {"user_id": user_id}

@app.get("/posts/{post_id}")
async def read_post(post_id: int):
  return {"post_id": post_id}

@app.get("/users/{user_id}/orders/{order_id}")
async def read_user_order(user_id: int, order_id: int):
  return {"user_id": user_id, "orders_id": order_id}


# 1) localhost:8081/search?keyword=날씨
@app.get("/search")
async def search(keyword: str):
  return {"keyword": keyword}

# 2) localhost:8081/users?page=1&size=10 이렇게 구현 (page, size 값이 없어도 돌아감) 
# localhost:8081/users?page=1&aa=3&&bb=3 넣어도 에러안남 (aa,bb 를 함수안에 선언하지 말고 그냥 url에 넣어보기)
@app.get("/users")
async def users(page: int = 1, size: int = 10,):
  return {"page": page, "size": size}

# 3) http://localhost:8081/calc?x=3&y=5 돌리면 8나옴
@app.get("/calc")
async def calc(x: int, y: int):
  return {"result": x + y}

@app.get("/members")
async def members(name: str = None, age: int = None):
  return {"name": name, "age": age}

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None

@app.post("/items_test")
async def create_item(item: Item):
  item_dict = item.model_dump() # item을 dict로 변환
  if item.tax is not None:
    price1 = item.price + item.tax
    item_dict.update({"price": price1})
  
  return item_dict


#   /books (POST)
# Request Body:
# { "title": "문자열(필수)", "author": "문자열(필수)", "year": "정수(선택, 기본값=2025)" }
# 응답: 등록된 도서 정보 전체 반환
book_array = []
class Book(BaseModel):
  title: str
  author: str
  year: int = 2025

@app.post("/books")
async def create_book(book: Book):
  book_dict = book.model_dump()
  book_array.append(book_dict)
  return book_array