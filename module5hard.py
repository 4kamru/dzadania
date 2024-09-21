import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    # переопределяем __str__ иначе принт выведет лишнее
    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    # переопределяем __str__ иначе принт выведет лишнее
    def __str__(self):
        return f'{self.title}' ########################


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    # вход в систему
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                # print(f'Пользователь {nickname} вошёл в систему')
                return
        pass
        # по идее нужно так: print('Нет такого пользователя или неверный пароль')

    # регистрация, если такого пользователя нет
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        reg_user = User(nickname, password, age)
        # добавим в список пользователей
        self.users.append(reg_user)
        # автоматический вход после регистрации
        self.log_in(nickname, password)
        # или так: устанавлимаем текущего пользователя - по сути автоматический вход после регистрации
        # self.current_user = reg_user


    # выход
    def log_out(self):
        # кто выходит ?
        goodbye_user = self.current_user.nickname
        self.current_user = None
        print(f'{goodbye_user} вышел из системы')
        goodbye_user = None

    # добавление видео
    def add(self, *videos):
        for video in videos:
            # если такого видео нет, то добавляем
            if video not in self.videos:
                self.videos.append(video)


    # поиск видео без учета регистра поисковой строки
    def get_videos(self, search_str):
        # тут будут результаты поиска
        searched_video_list = []
        # приводим к нижнему регистру поисковую строку
        search_str = search_str.lower()
        for i in range(len(self.videos)):
            if search_str in self.videos[i].title.lower():
                searched_video_list.append(self.videos[i].title)

        return searched_video_list

    # есть более короткий вариант, но оставлю то, что выше (не люблю длинные строки):
    # def get_videos(self, search_str):
    #     search_str_lower = search_str.lower()
    #     return [video.title for video in self.videos if search_str_lower in video.title.lower()]

    # вызов видео для просмотра
    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if (video.adult_mode == True) and (self.current_user.age < 18):
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for t_second in range(video.time_now, video.duration):
                    print(t_second + 1, end=' ')
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                return
        pass  # по идее нужно вывести "видео не найдено"


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

print()
print('доп проверки')
ur.log_out()
ur.watch_video('Для чего девушкам парень программист?')
ur.log_in('urban_pythonist','iScX4vIJClb9YQavjAgF' )
ur.watch_video('Для чего девушкам парень программист?')

