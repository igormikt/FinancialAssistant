📘 FinancialAssistant — Telegram‑бот для управления личными финансами

🚀 Описание проекта
FinancialAssistant — это асинхронный Telegram‑бот на базе Aiogram 3, который помогает пользователю:
регистрироваться в системе;
получать актуальный курс валют;
получать советы по экономии;
вести учёт личных расходов по категориям;
сохранять данные в локальную базу SQLite.

Бот использует FSM‑машину состояний, работает через внешнее API курсов валют и хранит данные в локальной базе user.db.

✨ Основные функции

📌 Регистрация пользователя

💱 Курс валют (USD/EUR → RUB)
💡 Советы по экономии
🧾 Учёт личных расходов (3 категории)
🧠 FSM‑машина состояний
🗄️ SQLite база данных
🔐 Переменные окружения через dotenv

🏗️ Структура проекта

FinancialAssistant/
│
├── main.py                # Основная логика Telegram-бота
├── config.py              # Загрузка переменных окружения
├── check_secrets.py       # Проверка обязательных переменных окружения
├── requirements.txt       # Зависимости проекта
├── user.db                # SQLite база данных (создаётся автоматически)
└── README.md              # Документация проекта

⚙️ Установка и запуск
1. Клонирование репозитория
bash
git clone https://github.com/igormikt/FinancialAssistant.git
cd FinancialAssistant
2. Установка зависимостей
bash
pip install -r requirements.txt
3. Настройка переменных окружения
Создай файл .env:

Код
BOT_TOKEN=твой_токен_бота
EXCHANGE_RATE_API_URL=https://v6.exchangerate-api.com/v6
EXCHANGE_RATE_API_KEY=ключ_от_API
Проверка переменных:

bash
python check_secrets.py
4. Запуск бота
bash
python main.py
📡 Команды и функциональность
🟦 /start
Отправляет приветствие и показывает меню:

Регистрация в телеграм боте

Курс валют

Советы по экономии

Личные финансы

💱 Курс валют
Бот делает запрос:

Код
{EXCHANGE_RATE_API_URL}/{EXCHANGE_RATE_API_KEY}/latest/USD
И выводит:

1 USD → RUB

1 EUR → RUB (пересчёт через USD)

💡 Советы по экономии
Случайный выбор из списка:

Ведите бюджет

Откладывайте часть доходов

Покупайте товары по скидкам

🧾 Учёт личных расходов (FSM)
Пользователь вводит:
Категория 1 → сумма
Категория 2 → сумма
Категория 3 → сумма

После ввода всех данных бот сохраняет их в SQLite:
Код
category1, expenses1
category2, expenses2
category3, expenses3
🗄️ Структура таблицы users
sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    telegram_id INTEGER UNIQUE,
    name TEXT,
    category1 TEXT,
    category2 TEXT,
    category3 TEXT,
    expenses1 REAL,
    expenses2 REAL,
    expenses3 REAL
);
🔐 Работа с конфигурацией
config.py
Загружает переменные окружения через python-dotenv:

python
BOT_TOKEN = os.getenv('BOT_TOKEN')
EXCHANGE_RATE_API_URL = os.getenv('EXCHANGE_RATE_API_URL')
EXCHANGE_RATE_API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
check_secrets.py
Проверяет наличие всех обязательных переменных.

📦 Зависимости (requirements.txt)
aiogram==3.17.0
aiohttp==3.9.5
python-dotenv==1.0.1




