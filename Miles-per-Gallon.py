# 7. Miles-per-Gallon
# A car's miles-per-gallon (MPG) can be calculated with the following formula

# MPG = Miles driven / Gallons of gas used

# Write a program that asks the user for the number of miles driven and the gallons of gas
# used. It should calculate the car's MPG and display the result.


milesDriven = float( input('enter the number of miles will drive '.title() ).strip() )
gallonOfGas = float( input('enter the amount of gas has , in gallon '.title() ).strip() )


# caculating the amount of gas per gallon the car need to travel 
milesPerGallon = milesDriven / gallonOfGas

print(f'with one Gallon of gas the car can travel {milesPerGallon} miles'.title() )
