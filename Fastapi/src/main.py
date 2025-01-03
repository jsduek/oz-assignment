from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# @app.get("/")
# def health_check_handler():   # djnago에서 view의 역할
#     return {"ping": "pong"}

# @app.get("/hello")
# def hello_handler():
#     return {"hello": "world"}

items = [
    {"id": 1, "name": "i-phone 16", "price": 100},
    {"id": 2, "name": "Galaxy 25", "price": 200},
    {"id": 3, "name": "Huawei", "price": 50},
]

# 전체 상품 목록 조회 API
# Query Param: 127.0.0.1:8000/items?price_lt=10000
# 상품 가격 100 ~ 200원
@app.get("/items")
def item_handler(
    min_price: Optional[int] = None, # int | None = None 이지만 python version이 낮아서 optional 사용
    max_price: Optional[int] = None,
):
    result = items
    if min_price:
        # 가격이 min_price 이상인 상품
        result = [item for item in result if item["price"] >= min_price]

    if max_price:
        # 가격이 max_price 이하인 상품
        result = [item for item in result if item["price"] <= max_price]

    return {"items": result}
    # default 값 없으면 필수값(required)으로 해석
    # Optional 한 값으로 처리하고 싶으면, default  -> = 1000
    # lt: less tnan = 미만
    # gt: greater than = 초과

    # lte, le: less than or equal to = 이하
    # gte, ge: greater than or equal to = 이상

    # if price_lt:
    #     pass
    #     # return 가격이 1만원 미만인 상품만 찾아서 반환
    # else:
        # return 전체 상품
    # int | None -> int or None
    # int | str | bool =? int or str or bool

# 특정 상품 반환 API
@app.get("/items/{item_id}")
def item_handler(
    item_id: int, # path 변수
    max_price: Optional[int] = None, # query param
):
    result = None # 데이터가 없는 상태
    for item in items:
        if item["id"] == item_id:
            result = item
            print(f"max_price: {max_price}")
    return {"item": result}