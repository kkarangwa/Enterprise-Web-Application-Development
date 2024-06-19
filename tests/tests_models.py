import unittest
from app import app, db
from app.models import User, WasteCollection

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_model(self):
        user = User(username='testuser', email='test@example.com', role='user')
        db.session.add(user)
        db.session.
import unittest
from app import app, db
from app.models import User, WasteCollection

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_model(self):
        user = User(username='testuser', email='test@example.com', role='user')
        db.session.add(user)
        db.session.
