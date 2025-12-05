def add_chocolate(shopping_list: list):
    """My housemate is a real health-nut, but I like chocolate. This function 
    adds the string "chocolate" to any list it receives, and returns the 
    modified list. That way our shopping list is always correct.

    Arguments:
        - shopping_list: a list of strings

    Returns:
        - the same list, with the string "chocolate" added to the end
    """
    shopping_list.append("chocolate")
    return shopping_list

# print(add_chocolate([1,2,3]))

def lou_bega(lyrics_list: list):
    """This function accepts a list of strings and adds the words 
    "A little bit of " to the front of each.
    
    Arguments:
        - lyrics_list: a list of strings
    
    Returns:
        - the same list, but each string now has "A little bit of " 
        prepended to it.

    Example input: 
        [
            "Monica in my life", 
            "Erica by my side", 
            "Rita's all I need"
        ]
        
    Example output: 
        [
            "A little bit of Monica in my life", 
            "A little bit of Erica by my side", 
            "A little bit of Rita's all I need"
        ]
    """
    for i in range(len(lyrics_list)):
        lyrics_list[i] = "A little bit of " + lyrics_list[i]
        print(lyrics_list)
    return lyrics_list

# print(lou_bega(["Monica in my life", 
#             "Erica by my side", 
#             "Rita's all I need"
#         ]))

def assemble_guest_list():
    """This function repeatedly prompts the user for the name of a dinner guest.
    Each string the user supplies is added to a list. If/when the user hits 
    "Enter" without typing anything, the function stops asking and 
    returns the list.
    
    Arguments: None!
    
    Returns:
        - a list of strings supplied by the user
    """
    # guest = input("Enter the name of the dinner guest: ")
    guest_list = list()
    # while (guest):
    while True:
        guest = input("Enter the name of the dinner guest: ")
        # print(guest_list)
        if not guest:
            break
        guest_list.append(guest)

    return guest_list


# print(assemble_guest_list())

def is_prime(some_number: int): # A bit trickier!
    """This function tests to see if the input is a prime number.
    Whenever a prime number is divided by an integer larger than 1 and smaller
    than itself, the result includes a remainder.

    NOTE: The lowest prime number is 2. 1 and 0 are not prime.
    
    Arguments:
        - some_number: an integer to be tested for prime-ness

    Returns:
        - a boolean representing whether or not some_number is prime
    """
    # prime = False
    if(some_number <= 1):
        print(f"{some_number}  is not a prime number")
        return False
    if(some_number == 2):
        print(f"{some_number}  is a prime number")
        return True
    if(some_number % 2 ==0):
        # print(f"{some_number} is not a prime number")
        return False
    for i in range(2,some_number):
        n = some_number%i
        if (n==0) :
            return False
        # else:
        #     return True
    return True

# some_number = 4                
# if(is_prime(some_number)):
#     print(f"{some_number} is a prime number")
# else:
#     print(f"{some_number} is not a prime number")
    
    # Hint: 
    #   int(1.5) == 1.0

