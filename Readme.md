# Сайт сервиса WhereToGo

Проект блогера, представляющий собой интерактивную карту Москвы, на которой отображены все известные ему виды активного отдыха с подробными описаниями и комментариями.


### Опубликованную версию сайта можно посмотреть по адресу [https://lamerork.pythonanywhere.com](https://lamerork.pythonanywhere.com)


## Запуск локально

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Выполните миграции

```sh
python3 manage.py migrate
```

Запустите сервер

```sh
python3 manage.py runserver
```

Сайт, запущенный локально, будет доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Для входа в админку и добавления/изменения данных о локациях можно использовать адрес: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Наполнение контентом

#### Для того, чтобы наполнить контентом из уже имеющегося файла необходимо:
 - создать файл в формате *.json

пример *.json файла:

```json
{
    "title": "Название места",
    "imgs": [
        "https://ссылка_на_картинку.ком/картинка.jpg",
        "https://ссылка_на_картинку.ком/картинка.jpg",
        "https://ссылка_на_картинку.ком/картинка.jpg"
    ],
    "description_short": "Короткое описание места",
    "description_long": "<p>Длинное описание, с поддержкой тэгов</p>",
    "coordinates": {
        "lng": "37.764456",
        "lat": "55.4545643"
    }
}
```

Загрузить контент

```sh
python manage.py load_place http://адрес/файла.json
```

## Цели проекта
Данные взяты в рамках урока [Django - Урок 1 'Пишем Яндекс.Афишу'](https://dvmn.org/modules/django/)

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).