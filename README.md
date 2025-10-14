# Skystore


Skystore — это веб-приложение на Django для хранения и продажи цифровых продуктов, плагинов и примеров кода.

## 📝 Описание проекта

- Каталог продуктов с категориями
- Возможность загрузки изображений продуктов
- Просмотр последних добавленных продуктов на главной странице
- Контактная форма для обратной связи с администрацией
- Администрирование через Django Admin
- Возможность загрузки тестовых данных через фикстуры или кастомную команду

---
### ⚙️ Установка

1. Клонируйте репозиторий:

```bash
git clone <URL_репозитория>
cd <папка_проекта>
```
2. Создайте виртуальное окружение и активируйте его:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. Установите зависимости из [pyproject.toml](pyproject.toml)


4. Выполните миграции базы данных:

```bash
python manage.py makemigrations
python manage.py migrate
```
5. Создайте суперпользователя:

```bash
python manage.py createsuperuser
```



### 📦 Загрузка тестовых данных

1. Через фикстуры:

```bash
python manage.py loaddata catalog.json
```
2. Через кастомную команду:

```bash
python manage.py add_products
```



### 🚀 Запуск проекта

```bash
python manage.py runserver
```
- Главная страница: http://127.0.0.1:8000/
- Контакты: http://127.0.0.1:8000/contacts/
- Админка: http://127.0.0.1:8000/admin/


### 📂 Структура приложения

```bash
catalog/
├─ management/commands/
│  └─ add_products.py
├─ migrations/
├─ templates/
│  └─ catalog/
│     ├─ contacts.html
│     └─ home.html
├─ admin.py
├─ apps.py
├─ models.py
├─ tests.py
├─ urls.py
├─ views.py
```

### ⚡ Функционал

1. Главная страница

- Отображение последних 5 добавленных продуктов
- Категории продуктов

2. Контакты

- Отправка сообщений через форму
- Сохранение сообщений в базу данных

3. Админка

- Управление продуктами и категориями
- Просмотр и поиск сообщений из формы контактов


### 📌 Технологии

- Python 3.11+
- Django 4.x
- SQLite (по умолчанию, можно заменить на PostgreSQL)
- Bootstrap 5 (для фронтенда)


### 🛠️ Настройка

- Шаблоны лежат в templates/catalog/
- Статические файлы лежат в static/
- Для добавления изображений продуктов — папка media/products/
---

### Шаблоны проекта:
[home.html](catalog%2Ftemplates%2Fcatalog%2Fhome.html) 

[contacts.html](catalog%2Ftemplates%2Fcatalog%2Fcontacts.html)

В контроллере для страницы [contacts.html](catalog%2Ftemplates%2Fcatalog%2Fcontacts.html)
реализована форма обратной связи, которая отображает сообщение об успешной отправке данных.


--- 
###### Автор
Svetlana Kolesnikova