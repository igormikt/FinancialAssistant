<h1 align="center" style="font-size:42px;">💰 FinancialAssistant</h1>
<p align="center" style="font-size:22px;">
Асинхронный Telegram‑бот для управления личными финансами.<br>
Aiogram 3 • SQLite • Aiohttp • FSM • ExchangeRate API
</p>

<hr>

<h2 style="font-size:32px;">🚀 Описание проекта</h2>
<p style="font-size:20px;">
FinancialAssistant — это умный Telegram‑бот, который помогает пользователю вести личные финансы, получать курс валют, регистрироваться в системе и сохранять расходы в базе данных.
</p>

<hr>

<h2 style="font-size:32px;">✨ Основные возможности</h2>
<ul style="font-size:20px;">
  <li>📌 Регистрация пользователя</li>
  <li>💱 Получение курса валют (USD/EUR → RUB)</li>
  <li>💡 Советы по экономии</li>
  <li>🧾 Учёт личных расходов (3 категории)</li>
  <li>🧠 FSM‑машина состояний</li>
  <li>🗄️ SQLite база данных</li>
  <li>🔐 Переменные окружения через dotenv</li>
</ul>

<hr>

<h2 style="font-size:32px;">📦 Установка и запуск</h2>

<h3 style="font-size:26px;">1. Клонирование репозитория</h3>
<pre style="font-size:18px;">
git clone https://github.com/igormikt/FinancialAssistant.git
cd FinancialAssistant
</pre>

<h3 style="font-size:26px;">2. Установка зависимостей</h3>
<pre style="font-size:18px;">
pip install -r requirements.txt
</pre>

<h3 style="font-size:26px;">3. Настройка переменных окружения</h3>
<pre style="font-size:18px;">
BOT_TOKEN=твой_токен_бота
EXCHANGE_RATE_API_URL=https://v6.exchangerate-api.com/v6
EXCHANGE_RATE_API_KEY=ключ_от_API
</pre>

<h3 style="font-size:26px;">4. Запуск бота</h3>
<pre style="font-size:18px;">
python main.py
</pre>

<hr>

<h2 style="font-size:32px;">📡 Функциональность</h2>

<h3 style="font-size:26px;">🟦 /start</h3>
<p style="font-size:20px;">
Показывает меню с кнопками: регистрация, курс валют, советы, личные финансы.
</p>

<h3 style="font-size:26px;">💱 Курс валют</h3>
<p style="font-size:20px;">
Бот получает курс USD и EUR через ExchangeRate API и выводит пересчёт в RUB.
</p>

<h3 style="font-size:26px;">💡 Советы по экономии</h3>
<p style="font-size:20px;">
Случайный совет из списка.
</p>

<h3 style="font-size:26px;">🧾 Учёт расходов (FSM)</h3>
<p style="font-size:20px;">
Пользователь вводит 3 категории и суммы расходов.  
Данные сохраняются в SQLite.
</p>

<hr>

<h2 style="font-size:32px;">🗄️ Структура таблицы users</h2>

<pre style="font-size:18px;">
id INTEGER PRIMARY KEY
telegram_id INTEGER UNIQUE
name TEXT
category1 TEXT
category2 TEXT
category3 TEXT
expenses1 REAL
expenses2 REAL
expenses3 REAL
</pre>

<hr>

<h2 style="font-size:32px;">📦 Зависимости</h2>
<pre style="font-size:18px;">
aiogram==3.17.0
aiohttp==3.9.5
python-dotenv==1.0.1
</pre>

<hr>

<h2 style="font-size:32px;">📈 Roadmap</h2>
<ul style="font-size:20px;">
  <li>Добавить графики расходов</li>
  <li>Добавить экспорт данных в Excel</li>
  <li>Добавить рекомендации по расходам</li>
  <li>Добавить Telegram WebApp</li>
  <li>Добавить категории по умолчанию</li>
</ul>

<hr>

