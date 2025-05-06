Описание (RUS)

Проект "Оскар" — Консольное приложение для поиска фильмов

Цель проекта
Создать консольное приложение на Python, работающее с базой данных sakila, которое позволяет:
•	искать фильмы по ключевому слову;
•	искать фильмы по жанру и году;
•	сохранять поисковые запросы в лог;
•	выводить список самых популярных запросов;
•	просматривать подробную карточку фильма.

Установка
1.	Клонируйте проект или скачайте ZIP.
2.	Установите зависимости:
pip install -r requirements.txt
3.	Убедитесь, что у вас есть доступ к базе данных sakila и ваша персональная база логов.

Запуск
python -m project_Oscar_de.main
Следуйте подсказкам в консоли. Вы можете искать фильмы и просматривать результаты.

Структура проекта

project_Oscar_de/
│
├── main.py                  # Точка входа: запуск приложения
│
├── db/                      # Работа с базой данных
│   ├── __init__.py
│   ├── connector.py         # Подключение к БД
│   └── queries.py           # SQL-запросы
│
├── logic/                   # Логика обработки данных
│   ├── __init__.py
│   ├── search.py            # Поиск фильмов и логирование
│   ├── analytics.py         # Анализ популярных запросов
│   ├── details.py           # Формирование карточки фильма
│   └── logger.py            # Запись ошибок в лог
│
├── ui/                      # Пользовательский интерфейс
│   ├── __init__.py
│   ├── console.py           # Консольное меню и взаимодействие
│   └── locale.py            # Словарь переводов
│
├── tests/                   # Тестовые данные
│   ├── __init__.py
│   └── test_checklist.json  # Чек-лист тестирования
│
├── logs/                    # Логирование
│   └── errors.log           # Файл ошибок
│
├── .env                     # Переменные окружения (доступ к БД)
├── requirements.txt         # Зависимости проекта
└── README.md                # Документация

Тестирование
Все тесты выполняются вручную по заранее составленному чек-листу test_checklist.json:
•	Тестируются основные функции приложения;
•	Прописаны входные данные и ожидаемый результат для каждого шага;
•	Указан статус выполнения (pass).

Зависимости
•	mysql-connector-python
•	tabulate
•	dotenv


Автор
Александр Голубенко — 2025


Description (English)

Oscar Project — Console-Based Movie Search App

Bilingual: Russian / German

Oscar is a console application built in Python that works with the Sakila MySQL database and allows users to:

Search movies by keyword
Search movies by genre and year
Log and count all search queries
Display most popular queries
Show full movie details (description, genre, actors, etc.)
At launch, the app lets the user choose the interface language: Russian or German.


Installation

Clone this repository or download the ZIP.

Install dependencies:
pip install -r requirements.txt

Make sure you have access to the Sakila database and your own logging database.


Launch

python -m project_Oscar.de.main

Follow the prompts to search movies or view statistics.


Project Structure

project_Oscar_de/
│
├── main.py                  # Entry point
│
├── db/                      # Database access
│   ├── __init__.py
│   ├── connector.py         # DB connection logic
│   └── queries.py           # SQL statements
│
├── logic/                   # Data processing logic
│   ├── __init__.py
│   ├── search.py            # Search and logging
│   ├── analytics.py         # Top queries
│   ├── details.py           # Movie card formatting
│   └── logger.py            # Error logging
│
├── ui/                      # User interface
│   ├── __init__.py
│   ├── console.py           # Console interface
│   └── locale.py            # Translations (language dictionary)
│
├── tests/                   # Test data
│   ├── __init__.py
│   └── test_checklist.json  # Manual test cases
│
├── logs/                    # Logging
│   └── errors.log           # Log file
│
├── .env                     # DB credentials
├── requirements.txt         # Dependencies
└── README.md                # This file

Testing

Tests are done manually via test_checklist.json. Each case includes:

Feature description

Input and expected output

Pass status


Dependencies

mysql-connector-python

tabulate

dotenv



Author

Alexander Golubenko — 2025




Beschreibung (Deutsch)

Projekt "Oscar" — Konsolenanwendung zur Filmsuche

Zweisprachig: Russisch / Deutsch


Oscar ist eine Python-Konsolenanwendung, die mit der MySQL-Datenbank Sakila arbeitet und folgende Funktionen bietet:

Filmsuche nach Stichwort

Filmsuche nach Genre und Erscheinungsjahr

Protokollierung und Zählung aller Suchanfragen

Anzeige der beliebtesten Suchbegriffe

Detaillierte Filmkarte mit Beschreibung, Genre, Schauspielern usw.

Beim Start der Anwendung wählt der Benutzer die Sprache: Russisch oder Deutsch.


Installation

Projekt klonen oder ZIP-Datei herunterladen.

Abhängigkeiten installieren:
pip install -r requirements.txt

Zugriff auf die Datenbank Sakila und eine eigene Log-Datenbank sicherstellen.


Start

python -m project_Oscar.main

Folgen Sie den Anweisungen in der Konsole zur Filmsuche oder Statistikanzeige.


Projektstruktur

project_Oscar_de/
│
├── main.py                  # Einstiegspunkt
│
├── db/                      # Datenbankzugriff
│   ├── __init__.py
│   ├── connector.py         # Verbindung zur Datenbank
│   └── queries.py           # SQL-Abfragen
│
├── logic/                   # Datenverarbeitung
│   ├── __init__.py
│   ├── search.py            # Suche und Logging
│   ├── analytics.py         # Beliebte Suchbegriffe
│   ├── details.py           # Formatierung der Filmkarte
│   └── logger.py            # Fehlerprotokollierung
│
├── ui/                      # Benutzeroberfläche
│   ├── __init__.py
│   ├── console.py           # Konsoleninterface
│   └── locale.py            # Übersetzungen (Sprachwörterbuch)
│
├── tests/                   # Testdaten
│   ├── __init__.py
│   └── test_checklist.json  # Testfälle
│
├── logs/                    # Logging
│   └── errors.log           # Fehlerprotokoll
│
├── .env                     # Zugangsdaten zur DB
├── requirements.txt         # Abhängigkeiten
└── README.md                # Diese Datei


Tests

Die Tests werden manuell über test_checklist.json durchgeführt. Jeder Testfall enthält:

Beschreibung der Funktion

Eingaben und erwartete Ergebnisse

Status (bestanden/nicht bestanden)


Abhängigkeiten

mysql-connector-python

tabulate

dotenv


Autor

Alexander Golubenko — 2025


