# -*- coding: utf-8 -*-
def convert_to_uppercase(input_str):
    "Функция переделана"
    return input_str.upper()

help(convert_to_uppercase)


def capitalize_first_letters(input_str):
    "Добавлена новая функия"
    return ' '.join(word.capitalize() for word in input_str.split())
help(capitalize_first_letters)

