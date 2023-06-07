![Deploy badge](https://github.com/belikrastr/foodgram-project-react/actions/workflows/foodgram_workfow.yml/badge.svg)

# Foodgram. «Продуктовый помощник»
### Описание
Сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

### Технологии
- Python 
- Django 
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
- Теперь сайт доступен по ссылке [Foodgram Pages](http://localhost/recipes)
### Примеры запросов к API.
- Список пользователей
###
GET http://ibelikbot.hopto.org/api/users/


- Регистрация пользователя
###
POST http://ibelikbot.hopto.org/api/users/
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
GET  http://ibelikbot.hopto.org/api/users/2/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a


- Текущий пользователь
###
GET  http://ibelikbot.hopto.org/api/users/me/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a


- Изменение пароля
###
POST http://ibelikbot.hopto.org/api/users/set_password/
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
POST http://ibelikbot.hopto.org/api/auth/token/login/
Content-Type: application/json
```js
{
    "password": "Abc2332325.",
    "email": "user1@user1.ru"
}
```

- Удаление токена
###
POST http://ibelikbot.hopto.org/api/auth/token/logout/
Authorization: Token b51f7cbe34a87a866fbb1316a71ce3d339698751
Content-Type: application/json



- Cписок тегов
###
GET http://ibelikbot.hopto.org/api/tags/


- Получение тега
###
GET http://ibelikbot.hopto.org/api/tags/1/


- Список рецептов
###
GET http://ibelikbot.hopto.org/api/recipes/


- Создание рецепта
###
POST http://ibelikbot.hopto.org/api/recipes/
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
GET http://ibelikbot.hopto.org/api/recipes/9/


- Обновление рецепта
###
PATCH http://ibelikbot.hopto.org/api/recipes/9/
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
DELETE  http://ibelikbot.hopto.org/api/recipes/7/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Скачать список покупок
###
GET  http://ibelikbot.hopto.org/api/recipes/download_shopping_cart/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a


- Добавить рецепт в список покупок
###
POST http://ibelikbot.hopto.org/api/recipes/9/shopping_cart/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Удалить рецепт из списка покупок
###
DELETE  http://ibelikbot.hopto.org/api/recipes/9/shopping_cart/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Добавить рецепт в избранное
###
POST http://ibelikbot.hopto.org/api/recipes/9/favorite/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Удалить рецепт из избранного
###
DELETE  http://ibelikbot.hopto.org/api/recipes/9/favorite/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Мои подписки
###
GET  http://ibelikbot.hopto.org/api/users/subscriptions/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a


- Подписаться на пользователя
###
POST http://ibelikbot.hopto.org/api/users/1/subscribe/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Отписаться от пользователя
###
DELETE  http://ibelikbot.hopto.org/api/users/1/subscribe/
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a
Content-Type: application/json


- Список ингредиентов
###
GET  http://ibelikbot.hopto.org/api/ingredients/?search=р
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a


- Получение ингредиента
###
GET  http://ibelikbot.hopto.org/api/ingredients/46002
Authorization: Token de82a223ca36916a5fd4be6657caeec9a4618c8a

### Проект в интернете
- Ссылка на развернутый проект на сервере [Foodgram Pages](http://ibelikbot.hopto.org/recipes)
- Админ панель доступна по адресу [Admin Pages](http://ibelikbot.hopto.org/admin/)
- Username/Password/Email суперпользователя: admin/admin/admin@admin.ru
### Автор проекта
Беликов Владимир - [Telegram](https://t.me/belikrastr) - belikrastr@yandex.ru

Project Link: [https://github.com/belikrastr/foodgram-project-react](https://github.com/belikrastr/foodgram-project-react)
