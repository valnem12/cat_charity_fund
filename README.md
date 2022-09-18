## Приложение QRKot

Проект QRKot — приложение для Благотворительного фонда поддержки котиков.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/valnem12/cat_charity_fund
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3.10 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать файл .env:

```
APP_TITLE=Благотворительный фонд котиков
DESCRIPTION=Сбор пожертвований на нужды хвостатых
DATABASE_URL=your_database
SECRET=your_secret
FIRST_SUPERUSER_EMAIL=your_email
FIRST_SUPERUSER_PASSWORD=your_password
```

Автогенерация миграций:

```
alembic revision --autogenerate -m "First migration"
```

Применение миграций:

```
alembic upgrade head
```

Запуск проекта:

```
uvicorn app.main:app --reload
```

Документация API:

```
http://127.0.0.1:8000/docs
```

### Технологии:
- Python 3.10
- FastAPI
- SQLAlchemy 1.4
- Git