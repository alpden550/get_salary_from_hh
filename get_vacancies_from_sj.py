import os
from dotenv import load_dotenv
import requests


load_dotenv()

SJ_KEY = os.getenv('sj_secret_key')
SJ_TOWNS = {
    'Москва': 4,
}
SJ_URL = 'https://api.superjob.ru/2.0/vacancies/'
HEADERS = {
    'X-Api-App-Id': SJ_KEY,
}
LANGUAGES = ['JavaScript', 'Java', 'Python', 'Ruby',
             'PHP', 'C++', 'C#', 'C', 'Go', 'Objective-C']


def fetch_sj_api(search=''):
    page, page_number = 0, 1
    raw_data = []
    parameters = {
        'keyword': f'{search}',
        'town': SJ_TOWNS['Москва'],
        'page': page,
    }

    while page < page_number:
        page_data = requests.get(SJ_URL, headers=HEADERS, params=parameters)
        if page_data.ok:
            page_number = page_data.json().get('total') / 20
            raw_data.extend(page_data.json().get('objects'))
            page += 1

    return raw_data


def predict_rub_salary_for_SuperJob(payment_from, payment_to):
    if payment_from and payment_to:
        result = int((payment_from + payment_to) / 2)
    elif payment_from and not payment_to:
        result = int(payment_from * 1.2)
    elif payment_to and not payment_from:
        result = int(payment_to * 0.8)
    else:
        result = None
    return result


def process_vacancies(vacancies):
    result = []

    for vacancy in vacancies:
        currency = vacancy.get('currency')
        profession = vacancy.get('profession')
        town = vacancy.get('town').get('title')
        salary = predict_rub_salary_for_SuperJob(vacancy.get('payment_from'),
                                                 vacancy.get('payment_to'))

        if currency != 'rub':
            continue
        result.append([profession, town, salary])
    return result


def get_salary_for_language(language):
    all_vacancies = fetch_sj_api(language)
    processed_vacancies = process_vacancies(all_vacancies)
    filtered_vacancies = list(
        filter(lambda x: x[2] is not None, processed_vacancies))
    all_salary = [vacancy[2] for vacancy in filtered_vacancies]
    try:
        average_salary = int(sum(all_salary) / len(all_salary))
    except ZeroDivisionError:
        average_salary = 0

    vacancies_found = len(processed_vacancies)
    vacancies_processed = len(filtered_vacancies)

    return (language, vacancies_found, vacancies_processed, average_salary)


def process_all_languages_from_sj(languages=LANGUAGES):
    result = []
    for language in languages:
        result.append(get_salary_for_language(language))
    return result


if __name__ == "__main__":
    print(*process_all_languages_from_sj())
