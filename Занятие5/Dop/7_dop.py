# Написать функцию, которая будет создавать тестового пользователя. Можно
# использовать в дальнейшем для генерации тестовых данных.
#
# Данные пользователей должны различаться и валидироваться в зависимости от поля,
# т.е. email должен быть формата email, phone - телефон нашего региона (т.е. +7).
#
# Имя и фамилию сначала можно генерировать случайно (необязательно человеческие),
# на ваш выбор они могут быть на русском или на английском.
#
# Дополнительно:
#
# * посмотреть библиотеки, которые могут генерировать человеческие :) имена и
#   фамилии, попробовать поработать с ними для генерации name и surname
# * продумать какие поля ещё можно добавить или добавить функционал для генерации
#   только тех полей, которые будут указаны в параметрах
# * сгенерировать n-пользователей и добавить в файл (можно формата json)

import json
import random
from transliterate import slugify
from typing import Iterator
from faker import Faker

fake_ru = Faker(locale="ru_RU")


def main():
    num_peoples = int(input("Введите количество людей: "))
    list_people = []
    people_gen = people()
    for i in range(num_peoples):
        list_people.append(next(people_gen))
    with open("output.txt", "w", encoding="utf-8") as f:
        json.dump(list_people, f, ensure_ascii=False, indent=4)


def male() -> str:
    list_male = ['male', 'female']
    return random.choice(list_male)


def name(male: str) -> str:
    if male == 'male':
        return fake_ru.first_name_male()
    else:
        return fake_ru.first_name_female()


def surname(male: str) -> str:
    if male == 'male':
        return fake_ru.last_name_male()
    else:
        return fake_ru.last_name_female()


def email(email_name: str, email_female: str) -> str:
    return f'{slugify(email_name)}{slugify(email_female)}@{fake_ru.free_email_domain()}'


def phone() -> str:
    return fake_ru.phone_number()


def address() -> str:
    return fake_ru.address()


def date_of_birth() -> str:
    return fake_ru.date()


def people() -> Iterator[dict]:
    while True:
        people_male = male()
        people_name = name(people_male)
        people_surname = surname(people_male)
        people_dict = {
            'Имя': people_name,
            'Фамилия': people_surname,
            'E-mail': email(people_name, people_surname),
            'Телефон': phone(),
            'Адресс': address(),
            'Дата рождения': date_of_birth()
        }
        yield people_dict


if __name__ == "__main__":
    main()
