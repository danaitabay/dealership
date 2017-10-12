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
	def __str__(self):
		return self.make + ' ' + self.model + ' ' + str(self.year) + ' ' + str(self.doors)
	#def __repr__(self):
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
class Truck(Vehicle):
	def __init__(self, make, model, year, hasBed):
		super(Truck, self).__init__(make, model, year)
		self.hasBed = hasBed
	def __str__(self):
		return self.make + ' ' + self.model + ' ' + str(self.year) + ' ' + self.hasBed		
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
class Motorcycle(Vehicle):
	def __init__(self, make, model, year, hasSideCar):
		super(Motorcycle, self).__init__(make, model, year)
		self.hasSideCar = hasSideCar
	def __str__(self):
		return self.make + ' ' + self.model + ' ' + str(self.year) + ' ' + self.hasSideCar
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__

vehicles = []

def specify_vehicle():
	print '\nEnter type of vehicle:', 
	vehicle = raw_input('--> ')
	print '\nEnter make of %s?' % vehicle,
	make = raw_input()
	print '\nEnter model of %s?' % make,
	model = raw_input()
	print '\nEnter year of %s?' % model,
	year = int(raw_input())
	if vehicle == 'car':
		print '\nEnter number of doors for %s?' % model,
		numdoor = int(raw_input())
		#a = ['\n%s' % vehicle, '\n%s' % make, '\n%s' % model, '\n%d' % year, '\n%d' % numdoor]
		v = Car(make, model, year, numdoor)
	elif vehicle == 'truck':
		print '\n%s with bed or without?' % vehicle,
		bed = raw_input()
		v = Truck(make, model, year, bed)
	elif vehicle == 'motorcycle':
		print '\n%s with side cars or without?' % vehicle,
		sidecar = raw_input()
		v = Motorcycle(make, model, year, sidecar)
		
	return v
	
while True:
	#vehicles.append(specify_vehicle())
	print '\nEnter 1 to make an entry \nEnter 2 to remove an entry \nEnter 3 to exit \n',
	i = int(raw_input())
	if i == 1:
		v = specify_vehicle()
		if v not in vehicles:
			vehicles.append(v)
			print '\nVehicle Added \nWhat do you want to do next?'
		else:
			print '\nError: You can not add the same vehicle twice.'
		
	elif i == 2:
		v = specify_vehicle()
		vehicles.remove(v)
		print '\nVehicle Removed \nWhat do you want to do next?'
	elif i == 3: 
		print '\nExiting...'
		break

		
#print map(str, vehicles)
print '\n'.join(str(c) for c in vehicles)

#print v
#print '\nHere are the list of %s %s %s in stock.\n' %(
#year, make, model)





