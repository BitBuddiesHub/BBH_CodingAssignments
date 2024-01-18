def create_dictionary():
    """
    Creates and returns a dictionary with various key-value pairs.

    The dictionary should have at least five key-value pairs with keys
    of different types (e.g., string, number, tuple).

    Returns:
        dict: A dictionary with various key-value pairs.
    """
    seq = ('Name', 'Age', 'Occupation', 'ID', (1,2))
    dict1 = dict.fromkeys(seq)
    dict1['Name'] = "Alice"
    dict1['Age'] = 30
    dict1['Occupation'] = "Engineer"
    dict1['ID'] = 1234
    dict1[(1,2)] = "Tuple Key"
    return dict1

def access_elements(sample_dict):
    """
    Accesses and prints elements from the provided dictionary.

    Args:
        sample_dict (dict): The dictionary from which elements are accessed.

    Returns:
        None
    """
    
    Name = sample_dict.get('Name')
    Occupation = sample_dict.get('Occupation')
    Tuple = sample_dict.get((1,2))
    
    return (Name,Occupation,Tuple)
    

def update_dictionary(sample_dict):
    """
    Updates the provided dictionary by performing various operations.

    - Adds a new key-value pair.
    - Updates the value of an existing key.
    - Prints the updated dictionary.

    Args:
        sample_dict (dict): The dictionary to update.

    Returns:
        None
    """
    
    sample_dict['Hobby'] = "Painting"
    sample_dict['Age'] = 31
    
    return sample_dict
    

def delete_elements(sample_dict):
    """
    Deletes elements from the provided dictionary.

    - Deletes a specific element.
    - Clears all elements.
    - Prints the dictionary after each deletion step.

    Args:
        sample_dict (dict): The dictionary from which elements are deleted.

    Returns:
        None
    """
    deleted_item = sample_dict.pop('Age')
    deleted = {'Age': deleted_item}
    return deleted

def demonstrate_dictionary_methods(sample_dict):
    """
    Demonstrates the use of at least three dictionary methods.

    Explain the functionality of each method in comments.

    Args:
        sample_dict (dict): The dictionary to use for demonstrating methods.

    Returns:
        None
    """
    # TODO: Implement this function to demonstrate dictionary methods.
    pass

def handle_key_error(sample_dict):
    """
    Attempts to access a non-existent key in the dictionary and handles KeyError.

    Use a try-except block to handle the error.

    Args:
        sample_dict (dict): The dictionary to use for the key access attempt.

    Returns:
        None
    """
    try:
        return sample_dict['Birth_place']
    except KeyError:
        return "NonExistentKey"

def main():
    """
    Main function to run the dictionary operations script.
    """
    
    print("Original Dictionary:",create_dictionary())
    
    for element in access_elements(create_dictionary()):
        print("Accessed Element:",element)
        
    print("Updated Dictionary:",update_dictionary(create_dictionary()))
    print(delete_elements(update_dictionary(create_dictionary())))
    print("KeyError:'%s'"% handle_key_error(create_dictionary()))
    
    
    
    
    
if __name__ == "__main__":
    main()