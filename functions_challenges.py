
#############################################################################################################
# Challenge 1 -> A Function to get a float from the user

def get_float(prompt_string: str):
    """A function that gets a float from the user and returns it.

    Arguments:
        - prompt_string: A string that will be shown to the user when they are
          prompted to input the number.

    Returns:
        - A float converted from the user's input
    """
    # user_input = input(f"Enter a number: {prompt_string}")
    str_float = float(prompt_string)
    return str_float

user_input = input("enter the number:")
print(get_float(user_input))


# #############################################################################################################
# Challenge 2 -> A Function to convert miles to km
# NOTE: 1 mile is 1.60934km

def miles_to_km(distance_in_miles: float):
    """A function to convert distance from miles to km

    Arguments:
        - distance_in_miles: A float representing a distance in miles

    Returns
        - a float representing the distance in kilometers
    """
    # distance_in_miles = float(distance_in_miles)
    distance_in_km = distance_in_miles * 1.60934

    return distance_in_km

distance_in_miles = input("Enter distance in miles: ")
print(miles_to_km(float(distance_in_miles)))

# # #############################################################################################################
# # Challenge 3 -> A function to calculate the total distance run in a relay

def relay_distance(distance_per_runner: float, number_of_runners: float):
    """A function to calculate the total distance run by a team of runners
    in a relay race.

    Arguments:
        - distance_per_runner: a float representing the amount each runner runs
            (in a relay race, all runners run the same distance!)
        - number_of_runners: a float representing the number of runners in a team

    Returns:
        - A float representing the total distance run.
    """
    total_distance = distance_per_runner * number_of_runners
    return total_distance

distance_per_runner = float(input("Enter distance per runner "))
number_of_runners = float(input("Enter number of runners "))
print(relay_distance(distance_per_runner, number_of_runners))

# # #############################################################################################################
# # Challenge 4 (extra tricky)
# #
# # See if you can write a single function that USES all three of the functions
# # you wrote for the above challenges.

def relay_distance_input(number_of_runners: float, distance_each_runner_miles: float):
    """A function that asks for a user's inputs for the number of runners and the distance each runner
    will run in a relay race in miles, and then calculate and return the total distance (in km) ran by
    all the runners.

    Arguments: None
        
    Returns:
        - A float representing the total distance run.
    """
    number_of_runners = get_float(number_of_runners)
    print(f"Number of runners: {number_of_runners}")

    distance_each_runner_miles = get_float(distance_each_runner_miles)
    print(f"Distance each runner will run in miles: {distance_each_runner_miles}")

    total_distance_miles = relay_distance(distance_each_runner_miles, number_of_runners)
    print(f"The total distance run by the team is {total_distance_miles} miles.")
    total_distance_km = miles_to_km(total_distance_miles)
    print(f"The total distance run by the team is {total_distance_km} kilometers.")
    return total_distance_km

number_of_runners = input("Enter number of runners: ")
distance_each_runner_miles = input("Enter distance each runner will run in miles: ")   
relay_distance_input(number_of_runners, distance_each_runner_miles)

# def say_hello(name_string: str):
#     """A function that returns a greeting to the user. 
      
#     If the user's name is "Oliver", then the function should return "Hello, Oliver!"

#     Arguments: 
#         - name_string: A string containing the user's name
      
#     Returns:
#         - A string containing a greeting to the user
#     """
    
#     return f"Hello, {name_string}!"

# print(say_hello("Oliver"))
