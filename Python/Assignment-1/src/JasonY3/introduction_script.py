def get_user_input():
    """
    Prompts the user to enter their name, age, and city.

    Returns:
        dict: A dictionary containing the user's name, age, and city.
    """
    Name = input("Enter your name:")
    Age = int(input("Enter your age:"))
    City = input("Enter your city:")
    return {"Name" : Name, "Age" : Age, "City" : City}


    

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
    intro1 = "Hello! My name is %s, I am %i years old and I live in %s." % (user_info.get("Name"), user_info["Age"], user_info.get("City"))
    intro2 = f"Hi! I'm {user_info.get('Name')}, a {user_info.get('Age')}-year-old living in {user_info.get('City')}."
    return intro1, intro2

def main():
    """
    Main function to run the introduction script.

    This function should call the get_user_input() and format_introduction()
    functions and print the formatted introduction strings.
    """
    user_input = get_user_input()
    introductions = format_introduction(user_input)
    for introduction in introductions:
        print(introduction)

if __name__ == "__main__":
    main()
