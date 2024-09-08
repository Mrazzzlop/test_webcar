# Тестовое задание на позицию Backend-разработчик на языке Python.



[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)

## Запуск проекта.

### Клонируйте репозиторий с проектом на свой компьютер. В терминале из рабочей директории выполните команду:
```bash
git clone https://github.com/Mrazzzlop/test_webcar

```

### Установить и активировать виртуальное окружение

```bash
source /venv/bin/activate
```

### Установить зависимости из файла requirements.txt

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
### Создать файл .env в папке проекта:
```.env
SECRET_KEY=secret_key
DEBUG=Fals
ALLOWED_HOSTS=127.0.0.1,localhost
```

### Выполните миграции:
```bash
python manage.py migrate
```
### Запустите сервер 
```bash
python manage.py runserver
```
### Основные адреса: 

| Адрес                                      | Описание                                                                                     |
|:------------------------------------------|:----------------------------------------------------------------------------------------------|
| 127.0.0.1                                | Главная страница вашего веб-приложения.                                                    |
| 127.0.0.1/admin/                        | Панель администратора для входа и управления пользователями, автомобилями и комментариями. |
| 127.0.0.1/cars/<int:pk>/                | Страница с подробной информацией о конкретном автомобиле по его уникальному идентификатору (pk). |
| 127.0.0.1/profiles/<str:username>/      | Страница профиля пользователя, где отображается информация о пользователе по его имени (username). |
| 127.0.0.1/cars/create/                  | Страница для создания нового автомобиля. Необходимо заполнить форму с данными автомобиля.  |
| 127.0.0.1/cars/<int:pk>/edit/           | Страница для редактирования информации о конкретном автомобиле по его уникальному идентификатору (pk). |
| 127.0.0.1/cars/<int:pk>/delete/         | Страница для подтверждения удаления конкретного автомобиля по его уникальному идентификатору (pk). |
| 127.0.0.1/cars/<int:car_id>/comments/   | Страница для просмотра и добавления комментариев к конкретному автомобилю по его уникальному идентификатору (car_id). |
| 127.0.0.1/cars/<int:car_id>/comments/<int:comment_id>/edit/ | Страница для редактирования конкретного комментария к автомобилю по его уникальному идентификатору (comment_id). |
| 127.0.0.1/cars/<int:car_id>/comments/<int:comment_id>/delete/ | Страница для подтверждения удаления конкретного комментария к автомобилю по его уникальному идентификатору (comment_id). |
# API Documentation

## 1. Регистрация нового пользователя

- **Метод:** `POST`
- **URL:** `http://127.0.0.1:8000/api/auth/users/`

**Запрос:**
```json
{
  "email": "user@example.com",
  "username": "string",
  "password": "string"
}
```

## 2. Авторизация пользователя (Basic Auth)

## 3. Получить список всех машин

- **Метод** `GET`
- **URL:**  `http://127.0.0.1:8000/api/cars/`

Ответ:
```json
[
  {
    "make": "Seres",
    "model": "M5 (Aito)",
    "year": 1995,
    "description": "description",
    "owner": 1
  }
]
```

## 4. Получить информацию о машине по ID
- **Метод** `GET`
- **URL** `http://127.0.0.1:8000/api/cars/<int:car_id>/`
Ответ:
```json
{
  "make": "Seres",
  "model": "M5 (Aito)",
  "year": 1995,
  "description": "description",
  "owner": 1
}
```
## 5. Создать новую машину
(Только для авторизованных пользователей)
- **Метод** `POST`
- **URL** `http://127.0.0.1:8000/api/cars/`
Запрос:
```json
{
  "make": "Seres",
  "model": "M5 (Aito)",
  "year": 1995,
  "description": "description"
}
```
## 6. Редактировать информацию о машине
(Только автору или админу)
- **Метод** `PUT`
- **URL** `http://127.0.0.1:8000/api/cars/<int:car_id>/`
Запрос:
```json
{
  "make": "Seres",
  "model": "M5 (Aito)",
  "year": 1995,
  "description": "updated description"
}
```
## 7. Удалить машину
(Только автору или админу)
- **Метод** `DELETE`
- **URL** `http://127.0.0.1:8000/api/cars/<int:car_id>/`

## 8. Получить список комментариев к машине
- **Метод** `GET`
- **URL** `http://127.0.0.1:8000/api/cars/<int:car_id>/comments/`
Ответ:
```json
[
  {
    "content": "Nice car!",
    "author": 1
  },
  {
    "content": "I love it!",
    "author": 2
  }
]
```
## 9. Создать новый комментарий к машине
(Только для авторизованных пользователей)
- **Метод** `POST`
- **URL** `http://127.0.0.1:8000/api/cars/<int:car_id>/comments/`
Запрос:
```json
{
  "content": "Great car!"
}
```
## 10. Редактировать комментарий к машине
(Только автору или админу)
- **Метод** `PUT`
- **URL** `http://127.0.0.1:8000/api/cars/<int:car_id>/comments/<int:comment_id>/edit/`
Запрос:
```json
{
  "content": "Updated comment!"
}
```
## 11. Удалить комментарий к машине
(Только автору или админу)
- **Метод** `DELETE`
- **URL** `http://127.0.0.1:8000/api/cars/<int:car_id>/comments/<int:comment_id>/delete/`
