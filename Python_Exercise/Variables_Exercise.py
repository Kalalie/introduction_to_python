#Q1 
# Intergers

First_Int = 3
Second_Int = 9

result = First_Int + Second_Int
print(result)

First_Int = -3
Second_Int = 9

result = First_Int + Second_Int
print(result)

# Intergers AND Floats

First_Float = 3.0
First_Int = -9

result = First_Float + First_Int
print (result)

print()

#Q2 
# Intergers

First_Int = 3
Second_Int = 9

result = First_Int * Second_Int
print(First_Int, '*', Second_Int, '=', result)

First_Int = -3
Second_Int = 9

result = First_Int * Second_Int
print(First_Int, '*', Second_Int, '=', result)

# Intergers AND Floats
First_Float = 3.0
First_Int = -9

result = First_Float * First_Int
print(First_Float, '*', First_Int, '=', result)

print()

#Q3 
First_Int = 10

result = First_Int * 1000
print(First_Int,'km =', result, 'm')

First_Int = 10

result = First_Int * 100000
print(First_Int,'km =', result, 'cm')

First_Float = 5.4

result = round(First_Float * 1000)
print(First_Float,'km =', result, 'm')

First_Float = 5.4
result = round(First_Float * 100000)
print(First_Float,'km =', result, 'cm')

#Q3 
name = input("What is your name?" )

height = f"Hi {name}, How tall are you? "
height = input(height)

if name == "William":
    print(name, 'is', height, 'cm tall') 
elif name == "Roary":
    print(name, 'is', height, 'cm tall')    
else:
    print(f"Hi, {name}!")