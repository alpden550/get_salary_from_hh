# Get averages salaries from HH and SJ

This script can print average salaries for the most popular languages from HeadHunter and SuperJob.

Also, you can get salaries only for one, headhunter or superjob.

## How to install

You have to create SJ's account and get secret key [API SJ](https://api.superjob.ru)

Create file .env in the root and write in it:

```.env
sj_secret_key=your key
```

Python3 must be already installed.

Should use virtual env for project isolation.

Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

## How to use

Run scripts in terminal

For print average salaries:

```bash
python get_average_salaries.py
```

For get salaries only from HH:

```bash
python get_vacancies_from_hh.py
```

For get salaries only from SJ:

```bash
python get_vacancies_from_sj.py
```

### Examples

```bash
Processing vacancies from HeadHunter..

+HeadHunter Moscow------+------------------+---------------------+------------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| JavaScript            | 940              | 893                 | 165824           |
| Java                  | 440              | 440                 | 172750           |
| Python                | 340              | 306                 | 156083           |
| Ruby                  | 80               | 72                  | 152388           |
| PHP                   | 500              | 425                 | 121764           |
| C++                   | 100              | 100                 | 142550           |
| C#                    | 340              | 323                 | 150894           |
| C                     | 200              | 200                 | 136450           |
| Go                    | 80               | 80                  | 165550           |
| Objective-C           | 40               | 40                  | 173249           |
+-----------------------+------------------+---------------------+------------------+
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
