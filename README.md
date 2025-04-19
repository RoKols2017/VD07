# Flask Auth App 🔐

Это веб-приложение на Flask с регистрацией, входом, редактированием профиля и защищёнными страницами.

## 🚀 Возможности

- Регистрация и вход с хэшированием пароля (bcrypt)
- Защищённые маршруты (Flask-Login)
- Редактирование имени, email и пароля
- Формы с валидацией (Flask-WTF)
- UI на Bootstrap 5
- Blueprint структура
- Поддержка переменных окружения через `.env`

## 📁 Структура проекта

```text
project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── routes.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── login.html
│       ├── register.html
│       ├── account.html
│       └── edit_profile.html
├── config.py
├── main.py
├── .env
├── requirements.txt
└── instance/
    └── create_db.py (опционально)
```

## 🛠️ Установка и запуск

1. Клонируй проект и перейди в директорию:

```bash
git clone <url>
cd project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Создай `.env` файл:

```env
SECRET_KEY=ТВОЙ_СЕКРЕТ
DATABASE_URL=sqlite:///site.db
FLASK_ENV=development
```

3. Инициализируй базу данных:

```python
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
```

4. Запусти сервер:

```bash
python main.py
```

## 🔐 Зависимости

Все зависимости указаны в `requirements.txt`:

- Flask
- Flask-WTF
- Flask-Bcrypt
- Flask-Login
- Flask-SQLAlchemy
- python-dotenv

## 📢 Автор

Разработано RoKols2017@gmail.com

Наслаждайся Flask-вселенной и кастомизируй как хочешь.
