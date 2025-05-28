# test_o-complex
Django Weather App

## Описание

Простое веб-приложение на Django, позволяющее пользователю ввести название города и получить актуальный прогноз погоды. Используется API от OpenWeatherMap для получения данных о погоде.

## Требования

- Python 3.12
- PostgreSQL
- Django
- OpenWeatherMap API
- Docker

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:dariazueva/test_o-complex.git
```

```
cd test_o-complex 
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Создайте файл .env и заполните его своими данными по образцу:

```
WEATHER_API_KEY = ваш-токен-OpenWeatherMap
POSTGRES_DB=weatherdb
POSTGRES_USER=weatheruser
POSTGRES_PASSWORD=secret
DB_HOST=db
DB_PORT=5432
```

#### Запустите систему контейнеров.
```bash
docker-compose up --build
```
#### Выполните миграции в контейнере backend.
```bash
docker-compose exec web python manage.py migrate
```
#### Создайте суперпользователя.
```bash
docker-compose exec web python manage.py createsuperuser
```
#### Запустите тесты.
```bash
docker-compose exec web python manage.py test 
```
#### Остановить контейнер.
```bash
docker-compose down
```

### Эндпоинты

GET     */*             — Главная страница с формой ввода города.

POST    */weather/*     — Обработка формы, отображение прогноза погоды.

GET     */stats/*       — API со статистикой по частоте введённых городов.

GET     */admin/*       — Панель администратора Django.


## Автор
Зуева Дарья Дмитриевна
Github https://github.com/dariazueva/