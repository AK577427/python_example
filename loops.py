# for i in range(0,10,2): #start, end, step
#     print(i)


# numlist = [1, 9001, -3, 0]
# for each_number in numlist:
#     print(each_number*each_number)

# list = [1, 2,3, 4,5]

# # for i in list[:-1]: #1st elementto 2nd last element
# #     print(i)

# len_list = len(list)
# for i in range(len_list): # also can use range(len(list)) directly
#     print(i) # prints the index
    # print(list[i]) # prints the element at that index 

#range function
# Create a range
my_range = range(0, 20, 2) # my_range stores 0...18 but it is not a list

# Convert the range to a list
my_list = list(my_range) # list is key word here

# Print the list
print(my_range) # prints  just the range
print(my_list) # prints the list created from the range

#enumerate function
alphabet = ["a", "b", "c", "d", "e"]

# nums = [10, 20, 30, 40, 50]

for i, l in enumerate(alphabet): # i is index, l is element at that index - i & l not keywords. 1st variable is index, 2nd variable is element at that index
    print(f"{l} is at position {i} in the alphabet!")

# Nested loops

iterations = ["first", "second", "third"]

print("Starting the outer loop!")

for outer_number in iterations: # outer loop
    print("Starting the inner loop!")

    for inner_number in iterations: # inner loop
        print(f"The outer loop is on its {outer_number} iteration, while the inner loop is on its {inner_number} iteration.")
    
    print("Inner loop complete!")

print("Outer loop complete!")


