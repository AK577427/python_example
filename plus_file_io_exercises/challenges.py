import csv

def count_mentions(some_colour_word: str):
    """The "colours_20_simple.csv" is a .csv file with a header. It lists facts 
    about 20 different colours, including their RGB values, hexadecimal 
    representation, and english name. 
    
    This function counts the number of times a given colour descriptor is 
    mentioned in the "English" column of the "colours_20_simple.csv" file.

    Arguments: 
        - some_colour_word: a string that describes a colour
    
    Returns: an integer representing the count of times that the 
    some_colour_word string appears in the "English" column of the 
    "colours_20_simple.csv" file. 

    Example: the input "beige" would return a result of 4, since there are 4 
    colours whose name includes the word beige. 
    """
    # hint - the .lower() method will convert a Python string to lowercase.
    # https://www.w3schools.com/python/ref_string_lower.asp

    colour = some_colour_word.lower()
    count = 0

    with open("data\colours_20_simple.csv", encoding="utf-8") as color_file:
        reader = csv.reader(color_file)
        for x in reader:
            english_value =  x[2].strip().lower()
            if colour in english_value:
                count =count + 1
    return count    

# some_colour_word = "Air Force Blue (Raf)"
# print(count_mentions(some_colour_word))

def generate_coloured_text(colour_name: str):
    """The "colours865.csv" file is a .csv file with a header. It lists facts 
    about 865 different colours, including their RGB values, hexadecimal 
    representation, and english name. 
    
    This function generates an html element to demonstrate a named colour from 
    the file.

    Arguments:
        - colour_name: a string representing a named colour from the 
        "colours_865.csv" file.
    
    Returns: a string representing an html <p> element that contains the 
    colour_name string as its text content, with inline css setting the "color" 
    property to that color.

    Example: supplying the argument "Alizarin Crimson" would result in a return 
    value of '<p style="color:#e32636;">Alizarin Crimson</p>'
    """
    colour_name_lower = colour_name.casefold()
    with open("data\colours_865.csv", encoding = "utf-8") as f: #plus_file_io_exercises\
        reader = csv.reader(f)
        html = ''
        for i in reader:
            english_value =  i[2].strip().casefold()
            # print(english_value)
            if(colour_name_lower == english_value):
                color_value = i[1]
                html = f'<p style="color:{color_value};">{colour_name}</p>'
                # print(type(html))
                # print('working')
                break
    return html

# colour_name = "Air Force Blue (Usaf)"
# print(generate_coloured_text(colour_name))


def galactic_speed_percentile(galactic_speed: float):
    """The "galaxies.csv" file is a .csv file WITHOUT a header. It describes
    the speed of 82 different galaxies (identified by numbers). The first column
    in the .csv lists the number of a galaxy, and the second column lists that
    galaxy's speed in km/sec. For instance, galaxy number 1 is traveling at 
    9172km/sec relative to our sun.
    
    This function calculates the percentage of listed galaxies that are 
    travelling faster than a given speed.

    Arguments:
        - galactic_speed: a float representing a speed in km/sec

    Returns: a float representing the number of galaxies travelling faster 
    than that speed.

    Examples:
        - an input of 50.0 would result in a return value of 100.00, because
        100% of the listed galaxies are travelling faster than 50km/sec
        - an input of 20830.0 would result in a return value of 50.0, because
        50% of the listed galaxies are travelling faster than 20830km/sec
        - an input of 999999.0 would result in a return value of 0.0, because
        0% of the listed galaxies are travelling faster than 999999km/sec 
    """
    count = 0

    with open("data\galaxies.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        max_rows = sum(1 for _ in reader)
    
    with open("data\galaxies.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for num in reader:
            value = int(num[1])
            if(value >= galactic_speed):
                count=count + 1
        percentage = (count/max_rows)*100

    return percentage

# speed = 32000
# print(galactic_speed_percentile(speed))
