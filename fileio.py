import csv

with open("galaxies.csv",  encoding="utf-8", mode="a") as my_file:
    # my_file_read = my_file.read()
    # print(my_file_read) #will print correct content if u use my_file.read() index 0, index 1
    my_file_read = csv.reader(my_file) #reading a file
    # for num in my_file_read:
    #     print(num) # prints everything
    #     print(num[0]) #prints everuthing from 1st line
    #     print(num[1]) #prints everuthing from 2nd line
        # print(num[3]) #index out of range
    # print(my_file_read) # not right - will print object not the file content if using cs.reader

    #writing into the file
    my_file_write = csv.writer(my_file, delimiter=",")
    my_file_write.writerow([83,12345])
with open("galaxies.csv",  encoding="utf-8") as my_file:
    my_file_read = csv.reader(my_file) #reading a file
    for num in my_file_read:
        print(num)