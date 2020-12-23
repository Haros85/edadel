# edadel
**Дипломный проект для Яндекс.Практикум**

# Описание
Простая и понятная электронная поваренная книга.

# Установка
клонируйте проект:
```git clone https://github.com/Haros85/edadel```

# Создайте .env с настройками для подключения к БД
```
SECRET_KEY=django_secret_key
DB_ENGINE=db_engine
DB_NAME=db_name
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
DB_HOST=host
DB_PORT=5432
```
**Настройки Nginx находятся в ```nginx/conf.d/local.conf```**

# Создание docker контейнера
запуск проекта выполняется командой ```docker-compose up```

# Миграции и создание суперпользователя
 - открываем терминал ```docker-compose exec foodgram bash```
 - миграция ```python manage.py migrate```
 - создание администратора ```python manage.py createsuperuser```

# Flatpages
 - Войдите в админку сайта, Управление сайтом - Настройки сайта и добавьте настройки для текущего сайта.
 - Войдите в админку сайта, Простые страницы, добавте 2 страницы с адресами (```/about/``` и ```/technology/```).

# Сайт готов к наполнению и использованию!
При желании можно заполнить таблицу с Ингредиентами:
```python manage.py loaddata db.json```
