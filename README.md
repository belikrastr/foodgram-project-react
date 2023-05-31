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
### Проект в интернете
- Ссылка на развернутый проект на сервере [Foodgram Pages](http://ibelikbot.hopto.org/recipes)
- Админ панель доступна по адресу [Admin Pages](http://ibelikbot.hopto.org/admin/)
- Username/Password/Email суперпользователя: admin/admin/admin@admin.ru
### Автор проекта
Беликов Владимир - [Telegram](https://t.me/belikrastr) - belikrastr@yandex.ru

Project Link: [https://github.com/belikrastr/foodgram-project-react](https://github.com/belikrastr/foodgram-project-react)
