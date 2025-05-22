# 🛍️ Barter API

**Barter API** — это REST API для платформы обмена товарами между пользователями. Реализовано с использованием Django, Django REST Framework и токен-авторизации.

---

## 📦 Стек технологий

- Python 3.12+
- Django 5.2+
- Django REST Framework
- SQLite (по умолчанию)
- Pytest (для тестирования)

---

## 🚀 Установка и запуск локально

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/ilyasqn/pythonTZ
cd barter
2. Создайте виртуальное окружение и активируйте его
python -m venv .venv
source .venv/bin/activate        # для Linux/Mac
# или .venv\Scripts\activate     # для Windows
3. Установите зависимости
pip install -r requirements.txt
🛠️ Миграции и создание суперпользователя
1. Примените миграции
python manage.py migrate
2. Создайте суперпользователя
python manage.py createsuperuser
▶️ Запуск сервера
python manage.py runserver
Сервер будет доступен по адресу:
http://127.0.0.1:8000

📑 Документация API
Swagger доступен по адресу:
http://127.0.0.1:8000/api/docs/swagger/

🔐 Авторизация
Зарегистрируйтесь через:
POST /api/register/

Получите токен через Swagger UI (кнопка "Authorize").

Используйте токен при отправке запросов.

🧪 Запуск тестов
pytest
