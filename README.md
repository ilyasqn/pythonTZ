🛍️ Barter API
REST API для платформы обмена товарами между пользователями. Реализовано с использованием Django, Django REST Framework и токен-авторизации.

📦 Стек технологий
Python 3.12+

Django 5.2+

Django REST Framework

SQLite по умолчанию

Pytest для тестирования

🚀 Установка и запуск локально
1. Клонируй репозиторий
git clone https://github.com/ilyasqn/pythonTZ
cd barter
2. Создай виртуальное окружение и активируй его
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
# или .venv\Scripts\activate — для Windows
3. Установи зависимости
pip install -r requirements.txt
🛠️ Миграции и суперпользователь
1. Применение миграций
python manage.py migrate
2. Создание суперпользователя
python manage.py createsuperuser
▶️ Запуск сервера
python manage.py runserver
Теперь сервер доступен по адресу:

http://127.0.0.1:8000
📑 Документация API
Swagger доступен по адресу:
http://127.0.0.1:8000/api/docs/swagger/

🔐 Авторизация (для отправки запросов)
Зарегистрируйтесь через /api/register/

Получите токен через Swagger-UI

Используйте токен в кнопке "Authorize" Swagger-интерфейса

🧪 Запуск тестов
pytest

