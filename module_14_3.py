from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from TGbot import config_bot as cfg

'''
# номера продуктов
C_1 = 1
C_2 = 2
C_3 = 3
C_4 = 4

# тексты для ценников в функции get_buying_list. А то там слишком длинно получается...
PRICE_1 = f'Название: Product{C_1} | Описание: описание {C_1} | Цена: {C_1*100}'
PRICE_2 = f'Название: Product{C_2} | Описание: описание {C_2} | Цена: {C_2*100}'
PRICE_3 = f'Название: Product{C_3} | Описание: описание {C_3} | Цена: {C_3*100}'
PRICE_4 = f'Название: Product{C_4} | Описание: описание {C_4} | Цена: {C_4*100}'

'''

api =""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Рассчитать')
        ],
        [
            KeyboardButton(text='Купить')
        ]
    ],resize_keyboard=True

)
# создание инлайн-клавиатуры, открывающейся по кнопке "Купить"
kb_buy = InlineKeyboardMarkup()
buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Product{cfg.c_1}', callback_data='product_buying'),
            InlineKeyboardButton(text=f'Product{cfg.c_2}', callback_data='product_buying'),
            InlineKeyboardButton(text=f'Product{cfg.c_3}', callback_data='product_buying'),
            InlineKeyboardButton(text=f'Product{cfg.c_4}', callback_data='product_buying')
        ]
    ], resize_keyboard=True
)

# инлайн-клавиатура, открывающаяся по кнопке "Рассчитать"
kb2 = InlineKeyboardMarkup()
# инлайн-клавиатура (старое задание - норма калорий и формулы)
calc_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas') # эти 2 кнопки во 2-й строке
        ]
    ], resize_keyboard=True
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создайте новую функцию main_menu(message), которая:
# Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
# Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=calc_menu)

# Создайте новую функцию get_formulas(call), которая:
# Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
# Будет присылать сообщение с формулой Миффлина-Сан Жеора.
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    msg = ('Упрощенный вариант формулы Миффлина-Сан Жеора:\n'
           + 'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n'
           +'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.message.answer(msg,reply_markup=kb2)
    await call.answer()


@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью", reply_markup=kb)

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я умею рассчитывать норму ккал (для мужчин) по упрощенной формуле Миффлина-Сан Жеора.')

# Измените функцию set_age и декоратор для неё:
# Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
# Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()



@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(txt_age=message.text)
    data = await state.get_data()

    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(txt_growth=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(txt_weight=message.text)
    data = await state.get_data()
    try:
        s_age = float(data["txt_age"])
        s_growth = float(data["txt_growth"])
        s_weight = float(data["txt_weight"])
    except:
        await message.answer(f'Невозможно преобразовать ваши данные в числа. Скорее всего некорректный ввод')
        await state.finish()
        return


    # вычисление нормы калорий
    norma = 10*float(s_weight) + 6.25*float(s_growth) - 5*float(s_age)

    await message.answer(f'Ваша норма калорий: {norma}')
    await state.finish()

# Тут выводятся картинки
# хотелось симметрии... примерно так для всех 4-х:
# await message.answer_photo(img_4, cfg.p_4, caption='Cap_for_product_4')
# ругается Питон:
# TypeError: answer_photo() got multiple values for argument 'caption'
# еще раньше хотел так
'''
@dp.message_handler(text='Купить')
async def get_buying_list_1(message):
    # витрина
    with open(f'files/{cfg.c_1}.png', 'rb') as img_1:
        await message.answer_photo(img_1, cfg.p_1, caption=f'Cap_for product_{c1}')
    # еще 3 раза
    # инлайн-меню выбрать продукт
    await message.answer('Выберите продукт для покупки:', reply_markup=buy_menu)
'''
# но видимо надо проще...
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    # витрина
    with open(f'files/{cfg.c_1}.png', 'rb') as img_1:
        await message.answer_photo(img_1, cfg.p_1)
    with open(f'files/{cfg.c_2}.png', 'rb') as img_2:
        await message.answer_photo(img_2, cfg.p_2)
    with open(f'files/{cfg.c_3}.png', 'rb') as img_3:
        await message.answer_photo(img_3, cfg.p_3)
    with open(f'files/{cfg.c_4}.png', 'rb') as img_4:
        await message.answer_photo(img_4, cfg.p_4)
    # инлайн-меню выбрать продукт
    await message.answer('Выберите продукт для покупки:', reply_markup=buy_menu)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()
# тут по идее надо различать, на какую кнопку нажал


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")



if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)


