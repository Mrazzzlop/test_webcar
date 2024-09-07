from django.core.exceptions import ValidationError
from datetime import datetime


def validate_year(value):
    current_year = datetime.now().year
    first_auto = 1885
    if value > current_year:
        raise ValidationError(
            f"Год выпуска не может быть больше текущего года.({current_year})."
        )
    if value < first_auto:
        raise ValidationError(
            f"Год выпуска не может быть меньше {first_auto} года."
        )
