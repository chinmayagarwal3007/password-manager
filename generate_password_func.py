import random


def generate_password_func():

    letters = ["a", "b", "c", "d", "e", "f", "g", "h" ,"i" , "j" ,"k" ,"l" , "m" ,"n" ,"o" ,"p" ,"q", "r", "s", "t" , "u","v" , "w", "x", "y", "z"]


    numbers = [
        "0","1","2","3","4","5","6","7","8","9"
    ]

    symbols = ["!", "#", "$", "%", "&", "(", ")", "+"]

    # Generate random number of each character type
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Create the password list
    password_list = []

    # Add random letters
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    # Add random symbols
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    # Add random numbers
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    # Shuffle the password list to randomize the order
    random.shuffle(password_list)

    # Join the list into a single string for the final password
    password = "".join(password_list)

    return password