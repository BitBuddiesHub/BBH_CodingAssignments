import unittest
from dictionary_operations import create_dictionary, access_elements, update_dictionary, delete_elements, demonstrate_dictionary_methods, handle_key_error

class TestDictionaryOperations(unittest.TestCase):

    def test_create_dictionary(self):
        """
        Test if the create_dictionary function returns a dictionary with at least five key-value pairs.
        """
        result = create_dictionary()
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result) >= 5, "Dictionary should have at least five key-value pairs.")

    def test_access_elements(self):
        """
        Test if the access_elements function correctly accesses dictionary elements.
        """
        test_dict = {'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer', 'ID': 1234, (1, 2): 'Tuple Key'}
        # This test might need to be adjusted based on how students implement the access_elements function.
        # Since we can't directly test the output to the console, this test may remain quite basic.
        # Alternatively, students could modify the function to return the accessed values for better testability.
        access_elements(test_dict)  # Assuming this function prints values and does not return anything.

    def test_update_dictionary(self):
        """
        Test if the update_dictionary function correctly updates the dictionary.
        """
        test_dict = {'Name': 'Alice', 'Age': 30}
        update_dictionary(test_dict)
        # Check if the dictionary is updated with at least one new key and one updated key.
        # This is a basic test and might need adjustment based on the assignment requirements.
        self.assertTrue(len(test_dict) > 2, "New key-value pair should be added.")
        # Further checks can be added based on expected updates in the function.

    def test_delete_elements(self):
        """
        Test if the delete_elements function correctly deletes elements from the dictionary.
        """
        test_dict = {'Name': 'Alice', 'Age': 30}
        delete_elements(test_dict)
        # Assuming the function clears the dictionary.
        self.assertEqual(len(test_dict), 0, "Dictionary should be empty after deletion.")

    def test_demonstrate_dictionary_methods(self):
        """
        Test the demonstrate_dictionary_methods function.
        """
        test_dict = {'Name': 'Alice', 'Age': 30}
        # This test is largely symbolic as the real demonstration depends on the implementation.
        # Students could modify the function to return results for better testability.
        demonstrate_dictionary_methods(test_dict)

    def test_handle_key_error(self):
        """
        Test if the handle_key_error function correctly handles a KeyError.
        """
        test_dict = {'Name': 'Alice', 'Age': 30}
        # Test to ensure no exception is raised by the function.
        try:
            handle_key_error(test_dict)
        except KeyError:
            self.fail("handle_key_error should not raise a KeyError.")

if __name__ == '__main__':
    unittest.main()
