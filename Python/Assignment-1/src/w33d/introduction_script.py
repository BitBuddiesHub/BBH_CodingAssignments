def get_user_input():
    """
    Prompts the user to enter their name, age, and city.

    Returns:
        dict: A dictionary containing the user's name, age, and city.
    """
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    
    return {'name': name, 'age': age, 'city': city}

def format_introduction(user_info):
    """
    Formats a self-introduction string based on the user's information.

    This function should use at least two different string formatting methods
    to create two different introduction strings.

    Args:
        user_info (dict): A dictionary containing the user's name, age, and city.

    Returns:
        tuple: A tuple containing two different introduction strings.
    """
    # Using the string % format method
    intro1 = "Hello! My name is %s, I am %s years old and I live in %s." % (user_info['name'], user_info['age'], user_info['city'])

    # Using an f-string (only for Python 3.6+)
    intro2 = f"Hi! I'm {user_info['name']}, a {user_info['age']}-year-old living in {user_info['city']}."

    return intro1, intro2

def main():
    """
    Main function to run the introduction script.

    This function should call the get_user_input() and format_introduction()
    functions and print the formatted introduction strings.
    """
    user_info = get_user_input()
    introductions = format_introduction(user_info)
    for intro in introductions:
        print(intro)

if __name__ == "__main__":
    main()
