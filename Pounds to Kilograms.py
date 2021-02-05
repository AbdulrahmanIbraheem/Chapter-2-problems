
# 3. Pounds to Kilograms
# One pound is equivalent to 0.454 kilograms. Write a program that asks the user to enter
# the mass of an object in pounds and then calculates and displays the mass of the object in
# kilograms.


# the amount of one Pound into Kg
one_pound_to_kg = 0.454

# tis the mass object in pounds entered by the user
mass_object_in_pounds = float( input('enter the object\'s mass in pounds '.title()).strip())

# converting the mass object into KG
mass_object_in_kg = mass_object_in_pounds * one_pound_to_kg

# the output value
print(f'the mass of object \"{mass_object_in_pounds:.2f}\" is pounds is equl to \"{mass_object_in_kg:.2f}\" in kg'.title())
