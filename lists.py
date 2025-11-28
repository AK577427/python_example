my_list = ['Asli', "Ashwini", "Ling", "Reece", "Camila","34", 45]
print(my_list)
print(my_list[6])
my_list.append("Ava")
print(my_list)

new_list = ["Asli", 576, 3.1415, False, None]
print(new_list)

new_list.append(["Ashwini", "Ling", "Reece", "Camila"])
print(new_list)

new_list = ["Asli", 576, 3.1415, False, None]
print(new_list[2])
new_list[2] = "banana"
print(new_list)

new_list = ["Asli", 576, 3.1415, False, None]
print(new_list[-5])

alphabet = ["a", "b", "c", "d", "e", "f", "g"]
print(alphabet[1:4]) #prints from index 1 to index 3
print(alphabet[:3]) #prints from start to index 2
print(alphabet[2:]) #prints from index 2 to end
print(alphabet[0:4:2]) #prints from index 0 to index 3, skipping every second element
print(alphabet[0:4:1]) # is same as print(alphabet[0:4])

# nested list

new_list = ["Asli", 576, 3.1415, False, None, ["Ashwini", "Ling", "Reece", "Camila"]]
print(new_list[5][1])

# IN operator
alphabet = ["a", "b", "c", "d", "e", "f", "g"]

if "z" in alphabet:
    print("Yep, that's the alphabet alright.")
else:
    print("I think you missed a letter or two there, Oliver...")

# len function
# new_list = ["Asli", 576, 3.1415, False, None]
# new_list.extend(["Ashwini", "Ling", "Reece", "Camila"])
new_list = ["Asli", 576, 3.1415, False, None, ["Ashwini", "Ling", "Reece", "Camila"]]
new_list_length = len(new_list)
print(new_list)
print(new_list_length)

a = [1, [1,2,3], [4,5,6], 6]
print(a[0])      # prints 1
print(a[1])      # prints [1,2,3]   
print(a[2][0])   # prints 4

