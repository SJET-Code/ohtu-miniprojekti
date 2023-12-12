import unittest
from services.validation_service import ValidationService, ValidationType, ValidationError

class TestValidationService(unittest.TestCase):
    def setUp(self):
        self.validation_service = ValidationService()

    def test_validate_accepts_correct_username(self):
        username = "test"

        try:
            self.validation_service.validate(username, ValidationType.USERNAME)
        except ValidationError:
            self.fail(f"validate() did not accept valid username: '{username}'")

    def test_validate_does_not_accept_too_short_username(self):
        username = "a"

        self.assertRaises(ValidationError, self.validation_service.validate, username, ValidationType.USERNAME)

    def test_validate_does_not_accept_too_long_username(self):
        username = "this_string_is_more_than_20_characters_long"

        self.assertRaises(ValidationError, self.validation_service.validate, username, ValidationType.USERNAME)

    def test_validate_accepts_correct_password(self):
        password = "Test1234"

        try:
            self.validation_service.validate(password, ValidationType.PASSWORD)
        except ValidationError:
            self.fail(f"validate() did not accept valid username: '{password}'")

    def test_validate_does_not_accept_too_short_password(self):
        password = "Abc123"

        self.assertRaises(ValidationError, self.validation_service.validate, password, ValidationType.PASSWORD)

    def test_validate_does_not_accept_too_long_password(self):
        password = "This_password_is_more_than_20_characters_long"

        self.assertRaises(ValidationError, self.validation_service.validate, password, ValidationType.PASSWORD)

    def test_validate_does_not_accept_password_without_number(self):
        password = "Test_password"

        self.assertRaises(ValidationError, self.validation_service.validate, password, ValidationType.PASSWORD)

    def test_validate_does_not_accept_password_without_lowercase_letter(self):
        password = "TEST1234"

        self.assertRaises(ValidationError, self.validation_service.validate, password, ValidationType.PASSWORD)

    def test_validate_does_not_accept_password_without_uppercase_letter(self):
        password = "test1234"

        self.assertRaises(ValidationError, self.validation_service.validate, password, ValidationType.PASSWORD)

    def test_validate_accepts_correct_citation_key(self):
        key = "Knittl_Frank_2020"

        try:
            self.validation_service.validate(key, ValidationType.REFERENCE_KEY)
        except ValidationError:
            self.fail(f"validate() did not accept valid username: '{key}'")

    def test_validate_does_not_accept_key_with_invalid_characters(self):
        key = "Knittl Frank 2020!"

        self.assertRaises(ValidationError, self.validation_service.validate, key, ValidationType.REFERENCE_KEY)

    def test_validate_accepts_correct_author(self):
        author = "Christian and Saridakis, Iakovos and Stephens"

        try:
            self.validation_service.validate(author, ValidationType.AUTHOR)
        except ValidationError:
            self.fail(f"validate() did not accept valid username: '{author}'")

    def test_validate_does_not_accept_author_with_invalid_characters(self):
        author = "Knittl-Frank2, Christian? and Saridakis:"

        self.assertRaises(ValidationError, self.validation_service.validate, author, ValidationType.AUTHOR)

    def test_validate_accepts_correct_title(self):
        title = "Gold-Catalyzed Cycloisomerization of Sulfur Ylides to Dihydrobenzothiepines"

        try:
            self.validation_service.validate(title, ValidationType.TITLE)
        except ValidationError:
            self.fail(f"validate() did not accept valid username: '{title}'")

    def test_validate_does_not_accept_title_with_invalid_characters(self):
        title = "Gold-Catalyzed Cycloisomerization of Sulfur Ylides to Dihydrobenzothiepines!?"

        self.assertRaises(ValidationError, self.validation_service.validate, title, ValidationType.TITLE)

    def test_validate_accepts_correct_year(self):
        year = "2023"

        try:
            self.validation_service.validate(year, ValidationType.YEAR)
        except ValidationError:
            self.fail(f"validate() did not accept valid username: '{year}'")

    def test_validate_does_not_accept_title_with_non_numeric_characters(self):
        title = "k2023k"

        self.assertRaises(ValidationError, self.validation_service.validate, title, ValidationType.YEAR)

    def test_validate_raises_value_error_if_given_invalid_type(self):
        self.assertRaises(ValueError, self.validation_service.validate, "", None)
