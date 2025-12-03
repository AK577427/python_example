class Cow():
    species_name = "Bos Taurus" # species_name & diet are common across all objects of this class
    diet = "grass"              # these variables can be changed  - bessie.diet = "hay"

    def __init__(self, instance_name, instance_colour): # __init__ is a special method
        self.name = instance_name
        self.colour = instance_colour
    
    def __str__(self):                                  # __str__ is a special method
        return f"<A cow named {self.name}>"

    def speak(self): #self is not a key word. U can provide anything like a 
        print(self)
        print("MOO!")
    
    def dye_hair(self, new_colour):
        self.colour = new_colour

# bessie = Cow()

# print(bessie.species_name)
# print(f"Bessie the cow eats {bessie.diet}")
# print("Say something Bessie!")
# bessie.speak()

# bessie = Cow("Bessie", "Brown")
# print(f"This cow's name is {bessie.name}.")
# print(f"{bessie.name} is {bessie.colour}")

# cow1 = Cow("Daisy", "Black")
# cow2 = Cow("Nellie", "White")

# print(f"This cow's name is {cow1.name}.")
# print(f"{cow1.name} is {cow1.colour}")
# print(f"{cow1.name} eats {cow1.diet}")
 
# print(f"This cow's name is {cow2.name}.")
# print(f"{cow2.name} is {cow2.colour}")
# print(f"{cow2.name} eats {cow2.diet}")


bessie = Cow("Bessie", "Brown")
print(f"{bessie.name} is {bessie.colour}")
print("Dyeing Bessie's hair...")
# bessie.colour = "Blue"
bessie.dye_hair("Rainbow")
print(f"{bessie.name} is {bessie.colour}")

print(bessie)