# Form Validator Web Application

## Описание
Это веб-приложение для определения заполненных форм на основе шаблонов, хранящихся в базе данных.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <repository-url>
   cd form_validator
   ```

2. Создайте виртуальное окружение и активируйте его:
```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows 
   ```
3. Установите зависимости:
```bash
   pip install -r requrements.txt
   ```
4. Запустите сервер:
```bash
   python manage.py runserver
   ```
5. Использование   
Отправьте POST запрос на http://127.0.0.1:8000/forms/get_form/ с данными формы в формате f_name1=value1&f_name2=value2.

Пример запроса
```bash
curl -X POST -d "user_email=test@example.com&user_phone=+7 123 456 78 90&registration_date=01.01.2022" http://127.0.0.1:8000/forms/get_form/
```
Ответ   
Если форма найдена, вы получите:
```bash
{"form_name": "User  Registration"}
```
Если форма не найдена, вы получите:
```bash
{
    "user_email": "email",
    "user_phone": "phone",
    "registration_date": "date"
}
```