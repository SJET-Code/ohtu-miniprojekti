from enum import Enum
import re

class ValidationType(Enum):
    USERNAME = 1
    PASSWORD = 2
    REFERENCE_KEY = 3
    AUTHOR = 4
    TITLE = 5
    YEAR = 6

class ValidationError(Exception):
    def __init__(self, message, route_to) -> None:
        super().__init__(message)

        self.route_to = route_to


class ValidationService:
    def __init__(self) -> None:
        pass

    def validate(self, s, validation_type):
        if validation_type == ValidationType.USERNAME:
            self.validate_username(s)
            return
        if validation_type == ValidationType.PASSWORD:
            self.validate_password(s)
            return
        if validation_type == ValidationType.REFERENCE_KEY:
            self.validate_citation_key(s)
            return
        if validation_type == ValidationType.AUTHOR:
            self.validate_author(s)
            return
        if validation_type == ValidationType.TITLE:
            self.validate_title(s)
            return
        if validation_type == ValidationType.YEAR:
            self.validate_year(s)
            return

        raise ValueError("Invalid validation type")

    def validate_username(self, s):
        if len(s) < 3:
            raise ValidationError("Username must be atleast 3 characters long", "/register")

        if len(s) > 20:
            raise ValidationError("Username must be less than 20 characters long", "/register")

    def validate_password(self, s):
        if len(s) < 8:
            raise ValidationError("Password must be atleast 8 characters long", "/register")

        if len(s) > 20:
            raise ValidationError("Password must be less than 20 characters long", "/register")

        if not re.search(r"\d", s):
            raise ValidationError("Password must contain a number", "/register")

        if not re.search("[a-z]", s):
            raise ValidationError("Password must contain a lowercase letter", "/register")

        if not re.search("[A-Z]", s):
            raise ValidationError("Password must contain a uppercase letter", "/register")

    def validate_citation_key(self, s):
        if not re.match(r"[a-zA-ZÀ-ÿ-_:\d]+$", s, re.UNICODE):
            message = 'Citation key can only contain alphanumeric, "-", "_", and ":" characters'
            raise ValidationError(message, "/")

    def validate_author(self, s):
        if not re.match(r"[a-zA-ZÀ-ÿ-,.;_\u2010\d ]+$", s, re.UNICODE):
            print(s)
            raise ValidationError("Author was invalid", "/")

    def validate_title(self, s):
        if not re.match(r"[a-zA-ZÀ-ÿ-,:'´`’.^+${}_–\u2010\d ]+$", s, re.UNICODE):
            print(s)
            raise ValidationError("Title was invalid", "/")

    def validate_year(self, s):
        try:
            int(s)
        except ValueError as e:
            raise ValidationError("Year must be a number", "/") from e
