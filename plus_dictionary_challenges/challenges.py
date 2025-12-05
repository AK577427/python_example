import csv

def grocery_calculator(groceries: dict):
    """A function to add up grocery bills.

    Arguments:
        - groceries: a dict which has the names of grocery bill items as its 
        keys, and the cost of the items as its values.

    Returns: a float representing the total cost of the grocery bill.

    Example input: {
        "Baby Spinach 100g bag": 2.78,
        "Hot Chocolate 300g": 3.70,
        "Crackers 250g packet": 2.10,
        "Coffee 500g": 9.00,
        "Carrots 1kg bag": 0.56,
        "Oranges 1kg bag": 3.08
    }

    Example output: 21.22
    """
    # value = sum(groceries.values)
    list_value = groceries.values()
    total_value = 0
    for v in list_value:
        total_value = total_value + v
    return round(total_value,2)

# one way to pass dict, 
# groceries={"Baby Spinach 100g bag": 2.78,"Hot Chocolate 300g": 3.70} 
# print(grocery_calculator(groceries))

#2nd way, without assigning 
# print(grocery_calculator({"Baby Spinach 100g bag": 2.78,"Hot Chocolate 300g": 3.70}))

############################################

def word_counter(word_list: list):
    """A function to count the occurrences of each word in a word list.

    Arguments: 
        - word_list: a list of strings

    Returns: a dictionary containing the number of occurrences of each word in
    word_list.

    Example input: ["apple", "banana", "apple", "cherry", "apple", "banana"]

    Example output: {"apple": 3, "banana": 2, "cherry": 1}
    """
    print(word_list)
    unique_key = list(set(word_list)) # using set 
    print(unique_key)

    new_dict = {} # creating a new dictionary 
    #also can be done like below:
    # new_dict = dict()
    # for unique in word_list:
    #     if

    for name in unique_key:
        count = 0
        for i in word_list:
            if(i == name):
                count = count + 1
                new_dict.update({name:count})
    
    return new_dict

    #different logic
    # word_count_dic = {}
    # for word in word_list:
    #     if word in word_count_dic:
    #         word_count_dic[word] += 1
    #     else:
    #         word_count_dic[word] = 1
    # return word_count_dic

# word_list = ["apple", "banana", "apple", "cherry", "apple", "banana"]
# print(word_counter(word_list))


def create_colour_dict(file_path: str):
    """A function that accesses an indicated csv file of colour values and 
    converts it into a dictionary.
    
    Arguments:
        - file_path: a string representing the location of a .csv file
        
    Returns: a dictionary whose keys are the plain English names of the colours
    described in the .csv file, and whose values are the hex codes of those 
    colours.
    
    Example input: "./data/colours_3_very_simple.csv"
    Example output: {"White": "#FFFFFF", "Black": "#000000", "Red": "#FF0000"}
                    {'White': '#FFFFFF', 'Black': '#000000', 'Red': '#FF0000'}
    """
    color_dict = {}
    import csv
    with open(file_path, encoding="utf-8") as my_file:
        # color_file = my_file.read()
        color_file = csv.reader(my_file)
        color_file.__next__()
        for i in color_file:
            # print(i)
            color_dict.update({i[2]:i[1]})
            # print(color_dict)
            # color_dict.keys = i[2]
            # color_dict.values = i[1]
        # for i in color_file:
        # print(color_dict)
        return color_dict
# file_path = "plus_dictionary_challenges\data\colours_3_very_simp.csv" #colours_3_very_simple.csv #plus_dictionary_challenges\
# print(create_colour_dict(file_path))


        