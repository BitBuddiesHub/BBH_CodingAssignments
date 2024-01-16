# Assignment 2: Exploring Python Dictionaries

## Objective
In this assignment, you will explore the functionality and flexibility of Python dictionaries. You will create a Python script that demonstrates various operations on dictionaries such as adding, updating, accessing, and deleting elements. This assignment aims to deepen your understanding of dictionary handling in Python.

## Task Description
Your task is to write a Python script that performs the following operations on dictionaries:

1. **Create a Dictionary**: Define a dictionary with at least five key-value pairs. The keys should be of different types (e.g., string, number, tuple).

2. **Access Elements**: Access at least three different elements in the dictionary and print them.

3. **Update Dictionary**: 
   - Add a new key-value pair to the dictionary.
   - Update the value of an existing key.
   - Print the updated dictionary.

4. **Delete Elements**: 
   - Delete a specific element from the dictionary.
   - Clear all elements from the dictionary.
   - Print the dictionary after each deletion step.

5. **Dictionary Methods**: Demonstrate the use of at least three dictionary methods (such as `get()`, `keys()`, `values()`, `items()`, `pop()`, etc.) and explain their functionality in comments.

6. **Error Handling**: Attempt to access a non-existent key and handle the resulting `KeyError` using a try-except block.

## Requirements
- The script should be well-commented to explain the purpose and usage of each operation.
- Include error handling where necessary.
- Ensure your code adheres to the PEP 8 style guide.

## Example Output
Your script should produce an output similar to the following (this is just an example, your actual output will depend on your dictionary and operations):

```
Original Dictionary: {'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer', 'ID': 1234, (1, 2): 'Tuple Key'}
Accessed Element: Alice
Accessed Element: Engineer
Accessed Element: Tuple Key
Updated Dictionary: {'Name': 'Alice', 'Age': 31, 'Occupation': 'Engineer', 'ID': 1234, (1, 2): 'Tuple Key', 'Hobby': 'Painting'}
Deleted Element: {'Age': 31}
Cleared Dictionary: {}

KeyError: 'NonExistentKey'
```

## Submission
Submit your Python script file with the name `dictionary_operations.py`. Make sure to test your script thoroughly before submission.

---

Good luck, and enjoy working with Python dictionaries! 🐍📘