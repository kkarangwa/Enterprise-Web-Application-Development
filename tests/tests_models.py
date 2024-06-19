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
        db.session.commit()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.role, 'user')

    def test_waste_collection_model(self):
        user = User(username='testuser', email='test@example.com', role='user')
        db.session.add(user)
        db.session.commit()
        collection = WasteCollection(user_id=user.id, scheduled_date='2023-06-15', status='Pending')
        db.session.add(collection)
        db.session.commit()
        self.assertEqual(collection.user_id, user.id)
        self.assertEqual(collection.scheduled_date, '2023-06-15')
        self.assertEqual(collection.status, 'Pending')

if __name__ == '__main__':
    unittest.main()
