import unittest
from unittest.mock import patch
from introduction_script import get_user_input, format_introduction

class TestIntroductionScript(unittest.TestCase):

    @patch('builtins.input', side_effect=['Alice', '25', 'New York'])
    def test_get_user_input(self, mock_input):
        """
        Test the get_user_input function to ensure it returns the correct dictionary.
        """
        result = get_user_input()
        self.assertEqual(result, {'name': 'Alice', 'age': '25', 'city': 'New York'})

    def test_format_introduction(self):
        """
        Test the format_introduction function with a sample dictionary input.
        """
        user_info = {'name': 'Alice', 'age': '25', 'city': 'New York'}
        intro1, intro2 = format_introduction(user_info)
        
        # Check if both introductions are strings
        self.assertIsInstance(intro1, str)
        self.assertIsInstance(intro2, str)

        # Check if the introductions contain the correct information
        self.assertIn('Alice', intro1)
        self.assertIn('25', intro1)
        self.assertIn('New York', intro1)
        self.assertIn('Alice', intro2)
        self.assertIn('25', intro2)
        self.assertIn('New York', intro2)

if __name__ == '__main__':
    unittest.main()
