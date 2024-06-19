from tests.test_base import BaseTestCase
from app.forms import LoginForm, RegistrationForm, ScheduleCollectionForm

class TestForms(BaseTestCase):
    def test_login_form(self):
        form = LoginForm(email='test@example.com', password='password')
        self.assertTrue(form.validate())

    def test_registration_form(self):
        form = RegistrationForm(username='testuser', email='test@example.com', password='password', confirm_password='password')
        self.assertTrue(form.validate())
from tests.test_base import BaseTestCase
from app.forms import LoginForm, RegistrationForm, ScheduleCollectionForm

class TestForms(BaseTestCase):
    def test_login_form(self):
        form = LoginForm(email='test@example.com', password='password')
        self.assertTrue(form.validate())

    def test_registration_form(self):
        form = RegistrationForm(username='testuser', email='test@example.com', password='password', confirm_password='password')
        self.assertTrue(form.validate())
