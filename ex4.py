#tells number of cars
cars = 100
#tells the amount of people a car can hold
space_in_a_car = 4.0
#tells the number of people to drive the cars
drivers = 30
#tells the number of passengers needing cars
passengers = 90
#subtracts the number of cars from the number of drivers
cars_not_driven = cars - drivers
#there is one car driven per one driver
cars_driven = drivers
#the passenger capacity is the number of cars driven multiplied by how much a car can hold
carpool_capacity = cars_driven * space_in_a_car
#averages the passengers divided by number of cars driven
average_passengers_per_car = passengers / cars_driven

print 'There are', cars, 'cars available.'
print 'There are only', drivers, 'drivers available.'
print 'There will be', cars_not_driven, 'empty cars today.'
print 'We can transport', carpool_capacity, 'people today.'
print 'We have', passengers, 'to carpool today.'
print 'We need to put about', average_passengers_per_car, 'in each car.'
