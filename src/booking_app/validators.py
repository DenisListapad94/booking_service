from django.core.exceptions import ValidationError

def validate_hotel_stars(value):
    if int(value) < 1 or int(value) > 5:
        raise ValidationError(
            f"value {value} must be more than 1 and less then 6",
        )
