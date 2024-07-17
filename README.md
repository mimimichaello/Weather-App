# Приложение Погоды

## Описание
Это приложение погоды, которое позволяет пользователям искать информацию о погоде по названию города. Приложение также сохраняет историю поиска для каждого пользователя и предоставляет автодополнение подсказок при вводе города.

## Реализовано
- Написаны unit-тесты для приложения
- Приложение помещено в Docker контейнер
- Реализовано автодополнение подсказок при вводе города
- История поиска сохраняется для каждого пользователя

## Используемые технологии
- Django 4.2
- Python 3.11
- Gunicorn 22.0.0
- Docker

## Запуск приложения
1. Создайте образ Docker, выполнив команду `docker build -t weather_app .` в корневом каталоге репозитория.
2. Запустите контейнер, выполнив команду `docker run -p 8001:8000 weather_app`.
3. Выполните миграции, создайте суперпользователя и войдите в админ панель, выполнив команды:
    ```
    docker exec -it weather_app python manage.py migrate
    docker exec -it weather_app python manage.py createsuperuser
    ```
4. Перейдите на страницу http://localhost:8001/weather/weather/ для начала использования приложения.

## Тесты

Тесты для приложения находятся в файле tests.py. Они могут быть запущены с помощью команды python manage.py test.