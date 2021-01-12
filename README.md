# edadel
**Дипломный проект для Яндекс.Практикум**
http://edadel.antonenko.me:8000

# Описание
Простая и понятная электронная поваренная книга.

# Установка
клонируйте проект:
`git clone https://github.com/Haros85/edadel`

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
**Настройки Nginx находятся в `nginx/conf.d/local.conf`**

# Создание docker контейнера
запуск проекта выполняется командой `docker-compose up --build -d`

# Миграции и создание суперпользователя
 - открываем терминал `docker-compose exec project bash`
 - миграция `python manage.py migrate`
 - создание администратора `python manage.py createsuperuser`

# Flatpages
 - Войдите в админку сайта, Управление сайтом - Настройки сайта и добавьте Доменное и Отображаемое имя.
 - Войдите в админку сайта, Простые страницы, добавте 2 страницы с адресами (`/author/` и `/spec/`).

Пример кода для **Простых страниц**
```
<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
 <div class="col-auto d-none d-lg-block">
   <img src="/static/images/dante.png" width="300" height="480">
 </div>
 <div class="col p-4 d-flex flex-column position-static">
   <h3 class="mb-0">Руслан d'Ante Антоненко</h3><br>
   <strong class="d-inline-block mb-2 text-primary">Подзаголовок:</strong>
   <p class="card-text mb-auto">Какой-то текст об авторе. Желательно обо мне))</p>
 </div>
 <div class="text-center hide-scrollbar d-flex my-7" data-horizontal-scroll="">
 <a href="https://github.com/Haros85" class="d-block text-reset mr-7 mr-lg-6" 
    style="margin-top: 1.25rem!important; margin-right: 1.25rem!important;">
  <div  class="avatar avatar-sm avatar-online mb-3">
   <img height="40px" src="/static/images/github.svg" alt="GitHub">
  </div>
  <div class="small">@Haros85</div>
 </a>
 <a href="https://www.instagram.com/rantonenko/" class="d-block text-reset mr-7 mr-lg-6"
    style="margin-top: 1.25rem!important; margin-right: 1.25rem!important;">
  <div class="avatar avatar-sm avatar-online mb-3">
   <img height="40px" src="/static/images/instagram.svg" alt="Instagram">
  </div>
  <div class="small">@rantonenko</div>
 </a>
</div>
</div>
```

# Сайт готов к наполнению и использованию!
При желании можно заполнить сайт тестовыми данными:
```python manage.py loaddata db.json```
