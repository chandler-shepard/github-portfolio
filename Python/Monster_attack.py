class Monster(object):
	"""A virtual monster"""

	monster_attacks = 1

	@staticmethod
	def total_attacks():
		print("Total monster attacks:", Monster.monster_attacks)

	def __init__(self, name, health):
		self.__name = name
		self.__health = health
		self.__attacks = 0
		Monster.monster_attacks += 1

	def __str__(self):
		reply = ("-" * 35) + "\n"
		reply += "Monster object:\n"
		reply += "Name: " + self.__name + "\n"
		reply += "Health remaining: " + str(self.__health) + "\n"
		reply += self.__name + " has attacked " + str(self.__attacks) + " time(s).\n"
		return reply

	def attack(self, other):
		self.__attacks += 1
		print("ROOOOOAAAAARRRRRR!")
		print("STOMP STOMP SLASH SLASH")
		print(self.__name + " has attacked " + other.__name + "\n")
		other.__health -= 200
		if other.__health <= 0:
			print(self.__name + " has defeated " + other.__name + "!\n")

	def get_name(self):
		return self.__name

	def set_name(self, new_name):
		if new_name:
			print(self.__name, "is now named", new_name + ".\n")
			self.__name = new_name
		else:
			print("Monster names cannot be empty.\n")


#main
monster1 = Monster("Godzilla", 1000)
monster2 = Monster("King Gidhora", 400)

#monsters attack eachother
monster1.attack(monster2)
monster2.attack(monster1)
monster1.attack(monster2)

#See how many attacks have been made 
Monster.total_attacks()

print(monster1)
print(monster2)

Monster.get_name(monster2)
#monster2.set_name("")
#Change the name of a monster
monster2.set_name("Mothra")
