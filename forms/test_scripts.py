import requests
from bs4 import BeautifulSoup


BASE_URL = 'http://127.0.0.1:8000'


def test_get_form():
    response = requests.get(f"{BASE_URL}/get_form/")
    if response.status_code == 200:
        print("GET /get_form: Success")
        print("Response:", response.text)
        return response.text  # Возвращаем текст ответа для дальнейшего использования
    else:
        print("GET /get_form: Failed with status code", response.status_code)
        return None


def test_form_answer(csrf_token, valid=True):
    if valid:
        data = {
            'request': {
                'user_email=email@mail.ru&user_phone=+7 900 000 00 00&registration_date=11.11.2011'
            },
            'csrfmiddlewaretoken': csrf_token  # Добавляем CSRF-токен
        }
    else:
        data = {
            'request': {
                'registration_date=value1'
            },
            'csrfmiddlewaretoken': csrf_token  # Добавляем CSRF-токен
        }

    response = requests.post(f"{BASE_URL}/get_form/form_answer/", data=data)
    print(response)
    if response.status_code == 200:
        print("POST /form_answer: Success")
        print("Response:", response.json())
    else:
        print("POST /form_answer: Failed with status code", response.status_code)


if __name__ == "__main__":
    html_response = test_get_form()
    if html_response:
        soup = BeautifulSoup(html_response, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

        test_form_answer(csrf_token, valid=True)  # Тест с корректными данными
        test_form_answer(csrf_token, valid=False)  # Тест с некорректными данными


