#Q1
lst=[]
while True:
    number = input("Give me another number: ")
    if len(number) >0:
        lst.append (int(number))
    else:
        break
print(sum(lst))

# #Q2
mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]
for item in mailing_list:
        print(f"{item[0]}: {item[1]}")

# #Q3

#My initial condition
n=1
#my list
name=[]
# if n is inferior to 3 it will ask for a name and append in to the list.
while n <= 3:
    names = input("Give me a name? ")
    name.append (names)
#each time user input a name it removes 1 to initial condition. After 3 condition is not met and break
    n= n + 1
#print list
print(name)

#Q4
groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

total = 0
for item in groceries:
    quantity = input(f"What quantity of {item[0]} would you like? ")
    item[1] = item[1] * int(quantity)
    total += item[1]
total = f"${total:.2f}"
print("=======Izzy Emporium========")
for item in groceries:
    print(f"{item[0]:<20} ${item[1]: .2f}")
print("============================")
print(f"{total:>27}")
