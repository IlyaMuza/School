import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return self.nickname


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self, users=None, videos=None, current_user=None, adult_mode=False):
        if not users:
            self.users = []
        else:
            self.users = users
        if not videos:
            self.videos = []
        else:
            self.videos = videos
        self.current_user = current_user
        self.adult_mode = adult_mode

    def log_in(self, nickname, password):
        self.log_out()
        for i in self.users:
            if i.nickname == nickname:
                self.current_user = nickname if i.password == hash(password) else print('Неверный пароль')
                return
        if not self.current_user:
            print('Пользователь не существует')

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in range(len(args)):
            if args[i] not in self.videos:
                self.videos.append(args[i])
                # print(self.videos)

    def get_videos(self, find_str):
        find_film = []
        for i in range(len(self.videos)):
            if find_str.lower() in self.videos[i].title.lower():
                find_film.append(self.videos[i].title)
        return find_film

    def watch_video(self, watch_film):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        fl = False
        for i in self.videos:
            if watch_film == i.title:
                fl = True
                break
        if fl:
            if (i.adult_mode and self.current_user.age > 17) or not i.adult_mode:
                for j in range(i.time_now, i.duration+1):
                    print(j)
                    time.sleep(1)
                print('Конец видео')
            else:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 3, adult_mode=True)

# Добавление видео
    ur.add(v1, v2)
    ur.add(v1, v2)

# Проверка поиска
    print(ur.get_videos('[влорп'))
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    # ur.log_in('vasya_pupkin', 'lolkekcheburek2')
    # print(ur.current_user)
# Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
