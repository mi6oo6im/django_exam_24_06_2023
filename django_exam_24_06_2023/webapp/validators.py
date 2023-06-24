# Custom validators here
from django.core.exceptions import ValidationError


def validate_first_char_is_letter(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def validate_letters_only(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')
