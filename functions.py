# def calculate_mean(num1, num2):
#     mean = (num1 + num2)/2
#     return mean

# avg = calculate_mean(30, 20)
# print(f"The average of 30 and 20 is: {avg}")

# avg = calculate_mean(100, 20)
# print(f"The average of 100 and 20 is: {avg}")

# def greeting_function(some_name):
#     print(f"Hi {some_name}, it's great to see you!")

# greeting_function("Nis")

# mysterious_value = greeting_function("Nis")

# print(mysterious_value)

# print(greeting_function("Nis"))

# def get_int():
#     the_int = int(input("Give me an integer, please."))
#     return the_int

# user_input = get_int()

# -----------------------

#Global variables
# global_value = 3

# print(f"Outside of the function, global_value = {global_value}.")

# def my_function():
#     print(f"Inside of the function, global_value = {global_value}.") 

# # Have to execute the function or the code inside it won't run!
# my_function()

# print(f"After the function, global_value = {global_value}.")

# -----------------------

#local variable
# def my_function():
#     local_value = 23
#     print(f"Inside of the function, local_value = {local_value}.")

# my_function()

# print(f"Outside of the function, local_value = {local_value}.")

# -----------------------

#global vs local
# the_value = 0

# print(f"Before the function, the_value = {the_value}.") #0

# def another_function():
#     the_value = 999
#     print(f"Inside the function, the_value = {the_value}.") #999

# another_function()

# print(f"After the function, the_value = {the_value}.") #0

# -----------------------

#modifying gloabl variable using return in function -- RIGHT WAY

# my_value = 50

# print(f"before the function, my_value = {my_value}")

# # We tell our function to expect a parameter
# def generate_new_value(val_to_mod): 
#     # We modify the parameter and return the new value
#     return val_to_mod + 8951

# # We assign the result of our function as the new value for our global variable
# my_value = generate_new_value(my_value)

# print(f"after the function, my_value = {my_value}")

# -----------------------

#modifying gloabl variable using return in function -- WRONG WAY - For real, don't do this unless you absolutely have to.

my_value = 50

print(f"before the function, my_value = {my_value}")

def modifies_a_global():
    # This pulls the global variable into the local namespace
    global my_value 
    
    # 🤢🤮 why tho... 🥺?
    my_value = -1

# When executed, our function invisibly modifies the global.
# Gross.
modifies_a_global()

print(f"before the function, my_value = {my_value}")

