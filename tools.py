# # f strings

# user_name = 'abby'
# user_age = 20

# user_info = f'{user_name} is {user_age} years old'

# print(user_info)

# # single line if statements

# user_status = 'adult' if user_age >= 20 else 'child'

# # list comprehension

# simple_list = [i for i in range(0,11,1)]

# print(simple_list)  

# # lambda function

# double_value = lambda num: num * 2

# print(double_value(10))

# # some functions want a function as an argument

# random_list = [('ana', 20), ('paul', 40), ('lisa', 10)]

# sorted_list = sorted(random_list, key = lambda user: user[1])

# print(sorted_list)

# exercise 

battleship = [f'{j}{i}' for j in ('a', 'b', 'c', 'd', 'e') for i in range(1, 6) if not (j == 'c' and i == 3)]

print(battleship)

