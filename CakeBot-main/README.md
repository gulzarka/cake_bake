# CakeBot

# База данных Торты

Этобаза данных тортов для заказа

## Описание моделей

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте БД командой `python manage.py migrate`
- Запустите сервер командой `python manage.py runserver`

## Администрирование

- Перейдите по адресу http://127.0.0.1:8000/admin
- Используйте данные для авторизации

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_NAME` — путь до базы данных, например: `db.sqlite3`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
 
