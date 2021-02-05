# problem 5
      
# 5. Distance Traveled
# Assuming there are no accidents or delays, the distance that a car travels down the interstate can be calculated # with the following formula:

# Distance = Speed *Time

# A car is traveling at 70 miles per hour. Write a program that displays the following:
# š The distance the car will travel in 6 hours
# š The distance the car will travel in 10 hours
# š The distance the car will travel in 15 hours




speed_per_hours = 70 # this is speed the car is traveling per houe
time_travel1 = 6 # this is the time 1 the car will travel
time_travel2 = 10 # this is the time 2 the car will travel
time_travel3 = 15 # this is the time 3 the car will travel

# caculating the distane the car will trvel in 6 hours
distace_car_travels_in_6hours = speed_per_hours * time_travel1

# caculating the distane the car will trvel in 10 hours
distace_car_travels_in_10hours = speed_per_hours * time_travel2

# caculating the distane the car will trvel in 15 hours
distace_car_travels_in_15hours = speed_per_hours * time_travel3

print(f'in {time_travel1} hours the car can travels {distace_car_travels_in_6hours} miles\nin {time_travel2} houra \
      the car can travel {distace_car_travels_in_10hours} miles\nin {time_travel3} hours the car can travels \
      {distace_car_travels_in_15hours} miles'.title())

