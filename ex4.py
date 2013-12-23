#assigning variable cars to integer value 100
cars = 100
#assigning variable space_in_a_car to floating value 4.0
space_in_a_car = 4.0
#assigning variable drivers to integer value 30
drivers = 30
#assigning variable passengers to integer value 90
passengers = 90
#subtracting drivers from cars and saving in cars_not_driven
cars_not_driven = cars - drivers
#assigning variable cars_driven with variable drivers
cars_driven = drivers
#multiplying cars_driven with space_in_a_car and saving in carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#dividing passengers with cars_driven and saving in average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

#printing all the variables accordingly
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


#Traceback (most recent call last):
#     File "ex4.py", line 8, in <module>
#       average_passengers_per_car = car_pool_capacity / passenger
#    NameError: name 'car_pool_capacity' is not defined

#because the variable defined was 'carpool_capacity' not 'car_pool_capacity'

#if we use 4.0 it takes the number as float but when used 4 it takes it as integer