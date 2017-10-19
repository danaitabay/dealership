#import json
#import b64encode

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
	while True:
		try:
			year = int(raw_input())
		except ValueError:
			print "Please enter an integer value"
		else:
			break

	if vehicle == 'car':
		print '\nEnter number of doors for %s?' % model,
		while True:
			try:
				numdoor = int(raw_input())
				#a = ['\n%s' % vehicle, '\n%s' % make, '\n%s' % model, '\n%d' % year, '\n%d' % numdoor]
			except ValueError:
				print "Please enter an integer value"
			else:
				break
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
	print '\nEnter 1 to make an entry \nEnter 2 to remove an entry \nEnter 3 to search for vehicle \nEnter 4 to modify Vehicle \nEnter 5 to list of vehicles \nEnter 6 to Exit \n',
	i = int(raw_input())
	if i == 1:
		v = specify_vehicle()
		if v not in vehicles:
			vehicles.append(v)
			print '\nVehicle is Added \nWhat do you want to do next?',
		else:
			print '\nError: You can not add the same vehicle twice.'
		
	elif i == 2:
		v = specify_vehicle()
		vehicles.remove(v)
		print '\nVehicle is Removed. \nWhat do you want to do next?',
		
	elif i == 3:
		print '\nEnter make of vehicle:',
		make = raw_input()
		print '\nEnter model of vehicle:',
		model = raw_input()
		print map(str, [x for x in vehicles if x.make == make and x.model == model])
		print '\nWhat do you want to do next?'

	elif i == 4:
		print '\nEnter the Make of vehicle you want to modify:'
		make = raw_input()
		print '\nAnd the model?'
		model = raw_input()	
		change = [x for x in vehicles if x.make == make and x.model == model]
		if change in vehicles:
			location = vehicles.index(change)
        	vehicles.remove(change)
        	correction = raw_input('Enter correction ' )
        	vehicles.insert(location, correction)

		#else:
			#print('Entry not found in list')
			
	
	elif i == 5:
		print '\nHere are the list of vehicles available \n',
		with open('vehicles.txt', 'r') as f:
			#vehicles = f.read()
			print(f.read())
		
	elif i == 6: 
		print '\nExiting...\n',
		break

with open('vehicles.txt', 'w') as f:
    f.write(str(vehicles))	
#print map(str, vehicles)
print '\n'.join(str(c) for c in vehicles)



#Now read the file back into a Python list object
#with open('vehicles.txt', 'r') as f:
    #a = json.loads(f.read())