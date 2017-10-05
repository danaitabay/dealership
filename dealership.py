class Vehicle(object):
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		
class Car(Vehicle):
	door = (1, 2, 3, 4)
	def __init__(self, make, model, year, doors):
		if doors not in self.door:
			raise ValueError("%s is not a valid door" % doors)	
		super(Car, self).__init__(make, model, year)
		self.doors = doors
				
class Truck(Vehicle):
	def __init__(self, make, model, year, hasBed):
		super(Truck, self).__init__(make, model, year)
		self.hasBed = hasBed

class Motorcycle(Vehicle):
	def __init__(self, make, model, year, hasSideCar):
		super(Motorcycle, self).__init__(make, model, year)
		self.hasSideCar = hasSideCar
'''		
v = Car('Honda', 'Accord', 2014, 5)
print v	
'''

print '\nEnter type of vehicle:', 
vehicle = raw_input('--> ')
print '\nEnter make of %s?' % vehicle,
make = raw_input()
print '\nEnter model of %s?' % make,
model = raw_input()
print '\nEnter year of %s?' % model,
year = raw_input()
if '%s' % vehicle is 'car':
	print '\nEnter number of doors for %s?' % model,
	numdoor = int(raw_input())
elif '%s' % vehicle is 'truck':
	print '\n%s with bed?' % vehicle,
elif '%s' % vehicle is 'motorcycle':
	print '\n%s with side cars?' % vehicle,
print '\nHere are the list of %s %s %s in stock.\n' %(
year, make, model)

