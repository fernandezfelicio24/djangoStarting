# Input Exceptions Here
from django.core.exceptions import ValidationError


def validate_title(value):
    title_input = value
    if title_input == "pornhub":
        message = "sorry," + title_input + "is not allowed"
        raise ValidationError(message)


def validate_category(value):
    category_input = value
    if category_input == "pornhub":
        message = "sorry," + category_input + "is not allowed"
        raise ValidationError(message)
