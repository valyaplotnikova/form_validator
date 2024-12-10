# Form Validator Web Application

## Описание
Это веб-приложение для определения заполненных форм на основе шаблонов, хранящихся в базе данных.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/valyaplotnikova/form_validator.git
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
Перейдите на http://127.0.0.1:8000/get_form/ и отправтье данные в формате f_name1=value1&f_name2=value2.

Ответ   
Если форма найдена, вы получите ответ с названием формы:
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
6. Для запуска тестовых запросов нужно набрать в терминале:
```bash
python forms/test_scripts.py
```