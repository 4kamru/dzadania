from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()
# словарь, куда будут помещаться пользователи (как бы база данных)
users = {'1': 'Имя: Example, возраст: 18'}

# Вывод списка пользователей
@app.get("/users")
async def get_users():
  return users

# Сделано с ограничением по возрасту, а также имя пользователя, как в предыдущей задаче
@app.post("/user/{username}/{age}")
async def add_user(
        username: Annotated[
            str,
            Path(title='Enter username', min_length=5, max_length=20, example='UrbanUser')
        ],
        age: Annotated[
            int,
            Path(title='Enter age', ge=18, le=120, example=24)
        ]
):
    max_id = max(map(int, users.keys()))
    new_user_id = str(max_id + 1)
    users[new_user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {new_user_id} is registered'

# обновить данные о пользователе
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[
            str,
            Path(title='Введите ID пользователя', example='1')
        ],
        username: Annotated[
            str,
            Path(title='Введите имя пользователя', min_length=5, max_length=20, example='UrbanProfi')
        ],
        age: Annotated[
            int,
            Path(title='Введите возраст', ge=18, le=120, example=28)
        ]
):
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f'User {user_id} has been updated'
    else:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")


# delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару
@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[
            str,
            Path(title='Введите ID пользователя', example='2')
        ]
):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")


