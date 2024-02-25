# # for classes we should use pascal case

# # variables in classes are attribute, and functions in classes are methods

# class TestClass:
#     test_var = (1,2,3)
#     another_var = 'something'

#     # self refers to any instance of the class and 
#     # must be the first parameter for all methods
#     # it allows you to target attributes everywhere within the class

#     def test_func(self):
#         print('function inside class')
#         print(self.test_var)
#         self.another_func('123')

#     def another_func(self, test_param):   
#         print(test_param)
# # create instance

# test = TestClass()    

# print(test.test_var)

# test.another_var = 'new value'

# print(test.another_var)

# # new var

# test2 = TestClass()

# print(test2.another_var)
# test2.test_func()

# test2.another_func('test')

# # dunder methods are special methods of a class
# # __init__ is run when a instance of the class is created
# # __len__ gets called when the instance is passed into the len function

# # mage class

# class Mage:
#     def __init__(self, health, mana):
#         self.health = health
#         self.mana = mana
#         print('mage class was created')
#         print(self.health, self.mana)
    
#     def attack(self, target):
#         target.health -= 50

# class Monster:
#     health = 100

# mage = Mage(150, 2000)        
# monster = Monster()

# print(monster.health)

# mage.attack(monster)

# print(monster.health)

# # inheritance

# # with inheritance one class can get the methods and attributes of another class
# # a class can also inherit from multiple classes and you can have entire family trees

# class Human:
#     def __init__(self, health):
#         self.health = health

#     def attack(self):
#         print('attack')

# class Warrior(Human):
#     def __init__(self, health, defense):
#         super().__init__(health)
#         self.defense = defense

# class Barbarian(Human):
#     def __init__(self, health, damage):
#         super().__init__(health)
#         self.damage = damage

# warrior = Warrior(100, 5.5)
# barbarian = Barbarian(200, 8.1)

# warrior.attack()
# barbarian.attack()

# exercises

class entity:
    def attack(self):
        print(f'attack with {self.damage} damage')

class Monster(entity):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def __repr__(self):
        return f'monsters {self.health} hp'    

monster = Monster(100, 10)
monster.attack()

print(monster)