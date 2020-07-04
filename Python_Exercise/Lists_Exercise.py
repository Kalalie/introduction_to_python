#Q1

foods = [
    "orange","apple","banana","strawberry","grape","blueberry",["carrot","cauliflower","pumpkin"],"passionfruit","mango","kiwifruit",
]
print(foods)

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print()

print(foods[6][-1])

print()

#Q2
mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]

for item in mailing_list:
        print(f"{item[0]:<3}: {item[1]}")

#Q3

my_name = input("Give me three names? ")
list_name = my_name.split()
Output_name = list(list_name)
print(Output_name)

# name = input("Give me three names? ")
# print(f"{name}")

# #Q4
my_string = input("Type this is a string ")
string = my_string.split()
list_string = list(string)
print(len(string), list_string)
sentence = my_string.split()
list_string = list(my_string)
print(len(my_string), list_string)



