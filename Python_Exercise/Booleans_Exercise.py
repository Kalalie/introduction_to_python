#Booleans
#Q1

is_moths_in_house = False

if is_moths_in_house is True:
    print("Get the moths!" )

if is_moths_in_house is False:
    print("No threats detected")

    print()

#Q2

is_moths_in_house = True
is_mitch_is_home = False

if is_moths_in_house and is_mitch_is_home:
    print("Hooman! Help me get the moths!")
elif is_moths_in_house and not is_mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
elif not is_moths_in_house and is_mitch_is_home:
    print("Climb on Mitch.")   
else:
    if not is_mitch_is_home and not is_mitch_is_home:
        print("No threats detected.")

#Q3

light_color = "red"
is_car_detected = True

if light_color == "red" and is_car_detected is True:
    print("Flash!")
else:
    print("Do nothing.")    

#Q4

height = f"How tall are you? "
height = int(input(height))

if height >= 120:
    print("Hop on!")
else:
    print("Sorry, not today :(")   


 
