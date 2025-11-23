# is_raining = False
# is_cold = True

# print(type(is_raining))
# print(type(is_cold))

# just_the_word_true = "True"
# print(type(just_the_word_true))

# print(is_raining)
# print(not is_raining)

# is_warm = False
# is_dry = True

# print(is_raining or is_warm) # False
# print(is_raining or is_cold)  #True
# print(is_cold or is_dry) # True

# print(is_raining and is_warm) # False
# print(is_raining and is_cold) # False
# print(is_cold and is_dry) # True

# print(5 == 3) # False
# print(5 == "five") # False
# print(5 == "5") #False
# print(5 == 2+3) #True
# print(5 == 5.0) #True
# print("five" == f"{'fi'}{'ve'}") # True
# print(f"{'fi'}{'ve'}")

# print(5 != 3) # True
# print(5 != "five") # True
# print(5 != "5")# True
# print(5 != 2+3) #False
# print(5 !=5.0) #False
# print("five" != f"{'fi'}{'ve'}") # False

# print(3 < 3) # False
# print(4 < 3) #False
# print(3 < 3.0) #False
# print(3 < 99) #True
# print(3 < 2+2) #True
# print(3 < 4.0) #True

# print(3 > 3) # False
# print(4 > 3) #True
# print(3 > 3.0) #False
# print(3 > 99) #False
# print(3 > 2+2) #False
# print(3 > 4.0) #False

# print(3 <= 3) # True
# print(4 <= 3) #False
# print(3 <= 3.0) #True
# print(3 <= 99) #True
# print(3 <= 2+2) #True
# print(3 <= 4.0) #True

# print(3 >= 3) #True
# print(4 >= 3) #True
# print(3 >= 3.0) #True
# print(3 >= 99) #False
# print(3 >= 2+2) #False
# print(3 >= 4.0) #False

# #IF statement example
# is_raining = True
# user_name = "Anu"

# if is_raining:
#     print(f"Hey {user_name}, it's raining!") 
#     print("Better take an umbrella!")

# #IF ELSE statement example
# is_raining = False
# user_name = "Ava"

# if is_raining:
#     print(f"Hey {user_name}, it's raining!") 
#     print("Better take an umbrella!")
# else:
#     print(f"Hey {user_name}, it's sunny!") 
#     print("Better wear sunscreen!")

# #IF, ELIF, ELSE statement example
# temperature = float(input("What temperature is it?: "))
# user_name = input("What is your name?: ")

# if temperature<15:
#     print(f"Hey {user_name}, it's cold!") 
#     print("Better take a coat!")
# elif temperature>20:
#     print(f"Hey {user_name}, it's hot!") 
#     print("Better take a water bottle!")
# else:
#     print("Its April 25th. Not too hot, not too cold. All you need is a light jacket!")

# truthiness & Falasiness
user_name = input("What is your name?: ")

if not user_name:
    user_name = input("Wait... you just hit enter without typing anything. Really, what is your name?: ")
