from fastapi import FastAPI
from fastapi import Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def read_admin():
    return{"message": "Вы вошли как администратор"}

# Требования к userid -  целое, положительное, userid>=1 и userid<=100
# описание 'Enter User ID' и пример значения: 12 (чтобы облегчить выбор пользователю))
@app.get("/user/{user_id}")
async def get_user(user_id: Annotated[
    int,
    Path(ge=1, le=100, example=12 )
]):

    return {"message": f"Вы вошли как пользователь № {user_id}"}

# ограничиваем длину имени пользователя не менее 5 и не более 20 символов)
# добавляем к пользователю возраст ( age>=18 и age<=120)
# меняю имя своей функции ( с read_user_info на get_user_info ) для более полного соответствия сути запроса
@app.get("/user/{username}/{age}")
async def get_user_info(
        username: Annotated[
            str,
            Path(title='Enter username', min_length=5, max_length=20, example='UrbanUser')
        ],
        age: Annotated[
            int,
            Path(title='Enter age', ge=18, le=120, example=19)
        ]
):
    return (f"Информация о пользователе. Имя: {username}, Возраст: {age}")








