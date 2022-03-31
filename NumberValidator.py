from prompt_toolkit.validation import ValidationError, Validator
import re


class NumberValidator(Validator):
    def validate(self, document):
        text = document.text

        if text and not text.isdigit():
            i = 0

            for i, c in enumerate(text):
                if not c.isdigit():
                    break

            raise ValidationError(message='Введённое значение не является числом',
                                  cursor_position=i)


class FloatValidator(Validator):
    def validate(self, document):
        text = document.text
        reg = r'^(?:-|)\d+(?:\.\d+|)$'

        if text and len(re.findall(reg, text)) == 0:
            raise ValidationError(message='Введённое значение не является числом')
