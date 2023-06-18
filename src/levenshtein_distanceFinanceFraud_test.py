import unittest
from levenshtein_distanceFinanceFraud import is_fraudulent


class TestFraudDetection(unittest.TestCase):
    database = [
        {'name': 'John Doe', 
         'address': '123 Main St, Anytown USA', 
         'income': 50000, 
         'employment': 'Full-time'},

        {'name': 'Jane Smith', 
         'address': '456 Oak St, Othertown USA', 
         'income': 75000, 
         'employment': 'Full-time'},

        {'name': 'Bob Johnson', 
         'address': '789 Elm St, Somewhere USA', 
         'income': 60000, 
         'employment': 'Part-time'}
    ]

    def test_database_empty(self):
        _database = []
        application = {'name': 'John Smith', 
                       'address': '456 Oak St, Anytown USA', 
                       'income': 80000, 
                       'employment': 'Self-employed'}
        self.assertTrue(is_fraudulent(application, _database))

    def test_identical_application(self):
        application = {'name': 'John Doe', 
                       'address': '123 Main St, Anytown USA', 
                       'income': 100000, 
                       'employment': 'Full-time'}
        self.assertFalse(is_fraudulent(application, self.database))

    def test_similar_application(self):       
        application = {'name': 'Jon Smith', 
                       'address': '456 Oak St, Anytown USA', 
                       'income': 100000, 
                        'employment': 'Self-employed'}
        self.assertTrue(is_fraudulent(application, self.database))

    def test_threshold_exceeded(self):
        application = {'name': 'John Smith', 
                       'address': '123 Main St, Anytown USA', 
                       'income': 80000, 
                       'employment': 'Self-employed'}
        self.assertFalse(is_fraudulent(application, self.database, threshold=5))


if __name__ == '__main__':
    unittest.main()
