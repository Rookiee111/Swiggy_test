class Parking_lot:
	def __init__(self, size):
		self.slots = [None] * size
		self.slot_dic = {}

	#returns the size of the parking lot
	def slot_size(self):
		return len(self.slots)

	# function to allocate a parking space to a car using Hashing function, in case the slot is already occupied it computes new hash value using rehash function
	# benefit of using hash is that it searches for the spot in O(1), so it is a comprise between space and compute time, and for this scenario the parking space is limited using hashing technique make sense
	def allocate_parking_spot(self, reg_num, color):
		self.reg = reg_num
		self.col = color
		r_lst = self.reg.split('-')
		c_num = r_lst[3]
		key = int(c_num[:2]) + int(c_num[2:])
		slot_value = self.hash_func(key, self.slot_size())
		if self.slots[slot_value] == None:
			self.slots[slot_value] = (self.reg, self.col)
		else:
			rehash_slot_value = self.rehash_func((slot_value + 1), self.slot_size()) #rehashing to compute new value
			print(rehash_slot_value)
			while self.slots[rehash_slot_value] != None:
				rehash_slot_value = self.rehash_func((rehash_slot_value + 1), self.slot_size())
				print(rehash_slot_value)
			self.slots[rehash_slot_value] = (self.reg, self.col)
		return self.slots

	# Returns a dictionary that maps the parking slot to the car details of the car parked in that spot
	def get_allocated_slots(self):
		for alloc_slots in range(len(self.slots)):
			if self.slots[alloc_slots] != None:
				self.slot_dic[alloc_slots] = self.slots[alloc_slots]
		return self.slot_dic

	#function to empty the slot when the car leaves
	def vacate_parking_slot(self, slot_value):
		self.slots[slot_value] = None
		self.slot_dic.pop(slot_value)
		return self.slots, self.slot_dic

	# function to check number of free slot, this could easily be modified to O(1) by using the operation of subtracting len slots available minus the len of dictionary
	def get_free_slots(self):
		count = 0
		for non_alloc_slots in self.slots:
			if non_alloc_slots == None:
				count += 1
		return count

	# using the hash function, in this case we are using the folding technique to compute key value, splitting the 4 digit number of the reg_num into 2 and adding them up, then computing hash value using modulo operator
	def hash_func(self, key, slot_size):
		return key % slot_size

	# this will compute by using the old hash value and adding one to it, all though there is a possibility of clustering however adding 1 will help us find the nearest slot.
	def rehash_func(self, key, slot_size):
		return key % slot_size


p = Parking_lot(6)
n = int(input("No of cars to be parked: "))
print(p.get_free_slots())
for x in range(n):
	if p.get_free_slots() == 0:
		print("printing in the if cond:", p.get_free_slots())
		print("Sorry Parking is full")
	else:
		print("printing in the else condition:",p.get_free_slots())
		s = input("park ").split(',')
		reg_n = s[0]
		color = s[1]
		print(p.allocate_parking_spot(reg_n, color))
print(p.get_allocated_slots())
print(p.vacate_parking_slot(4))
print(p.get_free_slots())
