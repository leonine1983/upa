
from django.core.exceptions import ValidationError
import re


def strong_password(password):
       # regexMi = re.compile(r'^(?=.*[a-z])')
       # regexMa = re.compile(r'(?=.*[A-Z])')
       # regexNu = re.compile(r'(?=.*[0-9])')

        regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

        if not regex.match(password):
            raise ValidationError((

                'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'

            ),
            code = 'Invalid'
            )


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)