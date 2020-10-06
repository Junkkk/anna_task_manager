<h2 align="center">FastAPI task manager</h2>


### Описание проекта:
Веб-сервис написаный на FastAPI.
- JWT авторизация
- CRUD пользователей
- CRUD задач пользователей

### Инструменты разработки

**Стек:**
- Python >= 3.8
- FastAPI == 0.52.0
- PostgreSQL

## Разработка

##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) установить pipenv

    pip install pipenv
    
##### 3) Создать виртуальное окружение

    pipenv shell
    
##### 4) Установить зависимости

    pipenv install

##### 5) Запустить образ базы данных
    
    docker-compose run postgres

##### 6) Выполнить команду для выполнения миграций

    alembic upgrade head
    
##### 7.1) Запустить сервер

    uvicorn main:app --reload
    
##### 7.2) Или запустить сервер так

    python main.py   
    
##### 8) Перейти по адресу

    http://127.0.0.1:8000/docs
    