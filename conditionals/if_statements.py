# is_raining = True
# is_cold = True

# if is_raining is True:
#     print("You will need an umbrella today!" )

# if is_cold:
#     print("You will need a jumper today")


# temperature = 11  
# if temperature <12:
#     print("OMG it is actually slightly cool in Perth")
# else:
#     print("ugh when can I wear my jeans?!?!?")

temperature = 20
windchill = 4
is_cold = (temperature - windchill) <16
is_raining = True
print(is_cold)

# if is_cold:
#     print("You will need a jumper today")
# else:
#     print("No need for a jumper today!")

if is_cold and is_raining:
    print("Just stay home.")
else:
    if is_raining:
        print("You will need an umbrella today!" )
    if is_cold:
        print("You will need a jumper today")