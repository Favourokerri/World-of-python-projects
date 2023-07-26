import unittest
from models.base_model import BaseModel
from unittest.mock import patch
from models.register import Register

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        self.register = Register()

    def test_get_first_name(self):
        with patch('builtins.input', side_effect=['John']):
            first_name = self.register.get_first_name()
            self.assertEqual(first_name, 'John')

    def test_get_last_name(self):
        with patch('builtins.input', side_effect=['Doe']):
            last_name = self.register.get_last_name()
            self.assertEqual(last_name, 'Doe')

    def test_get_age(self):
        with patch('builtins.input', side_effect=['25']):
            age = self.register.get_age()
            self.assertEqual(age, 25)

    def test_get_sex(self):
        with patch('builtins.input', side_effect=['male']):
            sex = self.register.get_sex()
            self.assertEqual(sex, 'male')

    def test_get_phone_number(self):
        with patch('builtins.input', side_effect=['15234567890']):
            phone_number = self.register.get_phone_number()
            self.assertEqual(phone_number, '15234567890')

    def test_get_email(self):
        with patch('builtins.input', side_effect=['favour767@gmail.com']):
            email = self.register.get_email()
            self.assertEqual(email, 'favour767@gmail.com')

    def test_get_password(self):
        with patch('builtins.input', side_effect=['password123']):
            password = self.register.get_password()
            self.assertEqual(password, 'password123')


if __name__ == '__main__':
    unittest.main()

