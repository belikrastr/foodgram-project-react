![Deploy badge](https://github.com/belikrastr/foodgram-project-react/actions/workflows/foodgram_workfow.yml/badge.svg)

# Foodgram. «Продуктовый помощник»
### Описание
Сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

### Технологии
- Python 3.7
- Django 2.2.19
- Django REST Framework
- Gunicorn
- Nginx
- Docker
- Github-Actions
- Postgresql

### Подготовка к запуску проекта
- Склонировать репозиторий на локальную мшину
```bash
git clone git@github.com:belikrastr/foodgram-project-react.git
```
- Cоздайте .env файл в директории backend/foodgram/fodgram/ и впишите:
```python
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Запуск проекта 
- Перейдите в директорию infra/ и запустите docker-compose:
```bash
docker-compose up -d --build
```
```bash
docker-compose up
```
- Выполните миграции:
```bash
docker-compose exec backend python manage.py migrate
```
- Создайте суперпользователя:
```bash
docker-compose exec backend python manage.py createsuperuser
```
- Соберите статику:
```bash
docker-compose exec backend python manage.py collectstatic --no-input
```
### Примеры запросов к API.
- Список пользователей
###
GET http://127.0.0.1:8000/api/users/


- Регистрация пользователя
###
POST http://127.0.0.1:8000/api/users/
Content-Type: application/json
```js
{
    "email": "user1@user1.ru",
    "username": "user1",
    "first_name": "user1",
    "last_name": "user1",
    "password": "Abc2332325"
}
```

- Профиль пользователя
###
GET  http://127.0.0.1:8000/api/users/2/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a


- Текущий пользователь
###
GET  http://127.0.0.1:8000/api/users/me/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a


- Изменение пароля
###
POST http://127.0.0.1:8000/api/users/set_password/
Authorization: Token b51f7cbe34a87a866fbb1316a71ce3d339698751
Content-Type: application/json
```js
{
"new_password": "Abc2332325.",
"current_password": "Abc2332325"
}
```

- Получить токен авторизации
###
POST http://127.0.0.1:8000/api/auth/token/login/
Content-Type: application/json
```js
{
    "password": "Abc2332325.",
    "email": "user1@user1.ru"
}
```

- Удаление токена
###
POST http://127.0.0.1:8000/api/auth/token/logout/
Authorization: Token b51f7cbe34a87a866fbb1316a71ce3d339698751
Content-Type: application/json



- Cписок тегов
###
GET http://127.0.0.1:8000/api/tags/


- Получение тега
###
GET http://127.0.0.1:8000/api/tags/1/


- Список рецептов
###
GET http://127.0.0.1:8000/api/recipes/


- Создание рецепта
###
POST http://127.0.0.1:8000/api/recipes/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json
```js
{
    "ingredients": [
        {
        "id": 45952,
        "amount": 10
        }
    ],
    "tags": [
        1
    ],
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
    "name": "string",
    "text": "string",
    "cooking_time": 1
}
```

- Получение рецепта
###
GET http://127.0.0.1:8000/api/recipes/9/


- Обновление рецепта
###
PATCH http://127.0.0.1:8000/api/recipes/9/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json
```js
{
    "ingredients": [
        {
        "id": 45952,
        "amount": 10
        }
    ],
    "tags": [
        1
    ],
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
    "name": "string",
    "text": "string",
    "cooking_time": 1
}
```

- Удаление рецепта
###
DELETE  http://127.0.0.1:8000/api/recipes/7/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Скачать список покупок
###
GET  http://127.0.0.1:8000/api/recipes/download_shopping_cart/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a


- Добавить рецепт в список покупок
###
POST http://127.0.0.1:8000/api/recipes/9/shopping_cart/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Удалить рецепт из списка покупок
###
DELETE  http://127.0.0.1:8000/api/recipes/9/shopping_cart/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Добавить рецепт в избранное
###
POST http://127.0.0.1:8000/api/recipes/9/favorite/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Удалить рецепт из избранного
###
DELETE  http://127.0.0.1:8000/api/recipes/9/favorite/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Мои подписки
###
GET  http://127.0.0.1:8000/api/users/subscriptions/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a


- Подписаться на пользователя
###
POST http://127.0.0.1:8000/api/users/1/subscribe/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Отписаться от пользователя
###
DELETE  http://127.0.0.1:8000/api/users/1/subscribe/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Список ингредиентов
###
GET  http://127.0.0.1:8000/api/ingredients/?search=р
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a


- Получение ингредиента
###
GET  http://127.0.0.1:8000/api/ingredients/46002
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a

### Проект в интернете
- Ссылка на развернутый проект на сервере [Foodgram Pages](http://ibelikbot.hopto.org/recipes)
- Админ панель доступна по адресу [Admin Pages](http://ibelikbot.hopto.org/admin/)
- Username/Password/Email суперпользователя: admin/admin/admin@admin.ru
### Автор проекта
Беликов Владимир - [Telegram](https://t.me/belikrastr) - belikrastr@yandex.ru

Project Link: [https://github.com/belikrastr/foodgram-project-react](https://github.com/belikrastr/foodgram-project-react)
