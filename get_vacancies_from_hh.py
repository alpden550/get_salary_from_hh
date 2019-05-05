import requests


HH_API = 'https://api.hh.ru/vacancies'
HH_CITIES = {
    'Москва': 1,
}
PERIOD = 30
HEADERS = {
    "User-Agent": 'HH-User-Agent',
}
LANGUAGES = ['JavaScript', 'Java', 'Python', 'Ruby',
             'PHP', 'C++', 'C#', 'C', 'Go', 'Objective-C']


def fetch_hh_api(search=''):
    page = 0
    page_number = 1
    data = {
        'text': f'программист {search}',
        'area': HH_CITIES['Москва'],
        'period': PERIOD,
        'only_with_salary': True,
        'page': page,
    }
    result = []

    while page < page_number:
        response = requests.get(HH_API, headers=HEADERS, params=data)
        if response.ok:
            result.extend(response.json().get('items'))
            page_number = response.json().get('pages')
            page += 1

    return result


def get_salaries_from_vac(all_vacancies):
    return [vacancy.get('salary') for vacancy in all_vacancies]


def predict_rub_salary(salaries_list):
    average_salaries = []

    for salary in salaries_list:
        if salary['currency'] != 'RUR':
            continue
        if salary['from'] and salary['to']:
            average_salaries.append(int((salary['from'] + salary['to']) / 2))
        elif salary['from'] and not salary['to']:
            average_salaries.append(int(salary['from'] * 1.2))
        elif salary['to'] and not salary['from']:
            average_salaries.append(int(salary['to'] * 0.8))
    return average_salaries


def process_language(language):
    all_vacancies = fetch_hh_api(language)
    salaries = get_salaries_from_vac(all_vacancies)

    vacancies_found = len(get_salaries_from_vac(salaries))
    vacancies_processed = len(predict_rub_salary(salaries))
    average_salary = int(sum(predict_rub_salary(salaries)) /
                         len(predict_rub_salary(salaries)))

    return (language, vacancies_found, vacancies_processed, average_salary)


def process_all_languages_from_hh(languages=LANGUAGES):
    result = []
    for language in languages:
        result.append(process_language(language))
    return result


if __name__ == "__main__":
    print(*process_all_languages_from_hh())
