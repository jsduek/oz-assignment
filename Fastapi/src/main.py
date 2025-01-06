from datetime import datetime

from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

from pydantic import BaseModel

from items.routers import router as item_router
from users.routers import router as user_router

app = FastAPI()
app.include_router(item_router)
app.include_router(user_router)

class NowResponse(BaseModel):
    now: datetime

@app.get("/now")
def get_now_handler():
    html = f"<html><body><h1>now: {datetime.now()}</h1></body></html>"
    # Python datetime 객체 -> JSON String
    return NowResponse(now=datetime.now())