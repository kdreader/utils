# encoding: utf8

from django.core.validators import RegexValidator


def phone_validator(phone):
    phone_reg = r'^1\d{10}$'
    return RegexValidator(phone_reg)(phone)
