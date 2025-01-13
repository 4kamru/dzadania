from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()
# словарь, куда будут помещаться пользователи (как бы база данных)
users = []

class User(BaseModel):
    id: int
    age: int
    username: str

# GET
# Вывод списка пользователей
@app.get("/users")
async def get_users():
  return users

# POST
# Добавление пользователя в список (из предыдущей задачи, почти готово)
# все делается с подсказками и примерами
# Чтобы было однообразие - запросы и сообщения на одном языке
@app.post("/user/{username}/{age}")
async def add_user(
        username: Annotated[
            str,
            Path(title='Enter username', min_length=5, max_length=20, example='UrbanUser')
        ],
        age: Annotated[
            int,
            Path(title='Enter age', ge=0, le=120, example=24)
        ]
):
    if len(users):
        # new_user_id = len(users)
        new_user_id = users[-1].id + 1
    else:
        new_user_id = 1

    # Новый объект класса Users - он же новый пользователь
    new_user = User(id=new_user_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT
# обновить данные о пользователе
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[
            int,
            Path(title='Enter new user ID', ge=1)
        ],
        username: Annotated[
            str,
            Path(title='Enter new username', min_length=5, max_length=20, example='UrbanProfi')
        ],
        age: Annotated[
            int,
            Path(title='Enter age', ge=0, le=120, example=28)
        ]
):
    # if user_id in users:
    #     tmp_user = User(id=user_id, username=username, age=age)
    #     return tmp_user
    # else:
    #     raise HTTPException(status_code=404, detail=f"User {user_id} was not found")
    for upd_user in users:
        if upd_user.id == user_id:
            upd_user.username = username
            upd_user.age = age
            return upd_user
    # Если пользователь не найден, выбрасываем исключение
    raise HTTPException(status_code=404, detail="User was not found")


# DELETE
# delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару
@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[
            int,
            Path(title='Enter user ID ', example='2')
        ]
):
    # if user_id in users:
    #     del users[user_id]
    #     return User(id =user_id)
    # else:
    #     raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    # Если пользователь не найден, выбрасываем исключение
    raise HTTPException(status_code=404, detail="User was not found")



