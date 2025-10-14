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

В проекте создано приложение [catalog](catalog)
### Запуск Django-проекта







В терминале PyCharm введите команду:

_python (или python3) manage.py runserver_

### Шаблоны проекта:
[home.html](catalog%2Ftemplates%2Fcatalog%2Fhome.html) 

[contacts.html](catalog%2Ftemplates%2Fcatalog%2Fcontacts.html)

В контроллере для страницы [contacts.html](catalog%2Ftemplates%2Fcatalog%2Fcontacts.html)
реализована форма обратной связи, которая отображает сообщение об успешной отправке данных.