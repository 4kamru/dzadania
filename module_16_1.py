from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def read_admin():
    return{"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def read_user_info(user_name: str, user_age: int):
    return (f"Информация о пользователе. Имя: {user_name}, Возраст: {user_age}")







