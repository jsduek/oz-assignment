import os
import shutil
import uuid
from datetime import date

from fastapi import APIRouter, UploadFile

from users.request import UserCreateUserRequestBody

router = APIRouter()

users = [
    {"id": 1, "name": "Elon Musk", "date_of_birth": date(1970, 1, 1)}
]

# (Read) 전체 유저 목록 조회 API
@router.get("/users")
def get_users_handler():
    return users

# 새로운 유저 생성 API
@router.post("/users")
def create_user_handler(body: UserCreateUserRequestBody):
    # 1. 사용자로부터 데이터를 받고
    # 2. 받은 데이터의 유효성 검사

    # 3. 새로운 유저 데이터를 유저 목록에 추가
    new_user = {
        "id": len(users) + 1,
        "name": body.name,
        "date_of_birth": body.date_of_birth,
    }
    users.append(new_user)
    return new_user

# R : 상세 유저 조회 API
@router.get("/users/{user_id}")
def get_user_handler(user_id: int):
    for user in users :
        if user["id"] == user_id:
            return user

# U : 유저 업데이트 API
@router.patch("/users/{user_id}")
def update_user_handler(user_id: int, body: UserCreateUserRequestBody):
    for user in users :
        if user["id"] == user_id:
            user["name"] = body.name
            return user
        
# U: 사용자 프로필 이미지 업데이트 API
@router.post("/users/{user_id}/images")
def update_profile_image_handler(user_id: int, profile_image: UploadFile):
    for user in users :
        if user["id"] == user_id:

            unique_filename = f"{uuid.uuid4()}_{profile_image.filename}"
            user["image"] = profile_image.filename

            
            file_path = os.path.join("users.images", unique_filename)
            with open(file_path, "wb") as f:
                shutil.copyfileobj(profile_image.file, f)

            user["image"] = unique_filename
            return user
        
# D : 유저 정보 삭제 API
@router.delete("/users/{user_id}")
def delete_user_handler(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
        return users