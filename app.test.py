import unittest
from app import app, db, Transaction
from flask_testing import TestCase

class FinanceTrackerTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_income(self):
        transaction = Transaction(user_id=1, description='Test income', amount=100, transaction_type='income')
        db.session.add(transaction)
        db.session.commit()
        income_transaction = Transaction.query.filter_by(description='Test income').first()
        self.assertIsNotNone(income_transaction)
        self.assertEqual(income_transaction.amount, 100)
        self.assertEqual(income_transaction.transaction_type, 'income')

    def test_add_expense(self):
        transaction = Transaction(user_id=1, description='Test expense', amount=50, transaction_type='expense')
        db.session.add(transaction)
        db.session.commit()
        expense_transaction = Transaction.query.filter_by(description='Test expense').first()
        self.assertIsNotNone(expense_transaction)
        self.assertEqual(expense_transaction.amount, 50)
        self.assertEqual(expense_transaction.transaction_type, 'expense')

if __name__ == '__main__':
    unittest.main()
