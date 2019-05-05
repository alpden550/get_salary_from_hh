from get_vacancies_from_sj import process_all_languages_from_sj
from get_vacancies_from_hh import process_all_languages_from_hh
from terminaltables import AsciiTable


def print_salaries_sj(salaries_list):
    title = 'SuperJob Moscow'
    table_data = [
        ('Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'),
    ]
    for salary in salaries_list:
        table_data.append(salary)
    table_instance = AsciiTable(table_data, title)
    print(table_instance.table)


def print_salaries_hh(salaries_list):
    title = 'HeadHunter Moscow'
    table_data = [
        ('Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'),
    ]
    for salary in salaries_list:
        table_data.append(salary)
    table_instance = AsciiTable(table_data, title)
    print(table_instance.table)


if __name__ == "__main__":
    print('Processing vacancies from SuperJob..')
    sj_salaries = process_all_languages_from_sj()
    print()
    print_salaries_sj(sj_salaries)
    print()
    print('Processing vacancies from HeadHunter..')
    hh_salaries = process_all_languages_from_hh()
    print()
    print_salaries_hh(hh_salaries)
