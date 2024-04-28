# Assignment: Classes and Methods in Python

## Objective

Create a Python script that defines a class with instance variables, class variables, class methods, and static methods. This exercise will test your understanding of these concepts.

## Requirements

- Define a class named `Library`.
- Include the following components:
  - **Class Variable:** `total_books` - an integer tracking the total number of books in all library instances.
  - **Instance Variables:** `name` (the name of the library) and `books` (a list of book titles available in the library).
  - **Constructor:** Initializes the library with a name and an initial list of books. It should also update the `total_books` class variable.
  - **Class Method:** `display_total_books` - prints the total number of books available across all libraries.
  - **Static Method:** `info` - prints a static message about what a library is.
  - **Instance Method:** `add_book` - adds a new book to the library's `books` list and updates `total_books`.

## Example Usage

```python
# Create instances of Library
lib1 = Library("Downtown", ["1984", "To Kill a Mockingbird"])
lib2 = Library("Uptown", ["The Great Gatsby"])

# Add a book to lib1
lib1.add_book("Pride and Prejudice")

# Display the total number of books in all libraries
Library.display_total_books()

# Print library info
Library.info()

# Expected Output:
# Total books in all libraries: 4
# A library is a collection of books and resources in digital or printed formats that is organized for use and maintained by a public body, an institution, or a private individual.
```

## Instructions

1. Write your script in the `src/library.py` file.
2. Ensure your script runs without errors and reflects the expected functionality described above.
3. (Optional) Use the `test/test_library.py` file to write tests for your class methods.

## Submission

Submit your assignment by committing your changes to the `src/library.py` file and creating a pull request to the main branch.

Good luck!