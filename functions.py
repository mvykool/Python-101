# # create a function

# def print_x_times(parameter = 'loop', loop_amount = 5):
#     counter = 0
#     while counter <= loop_amount:
#         print(counter, parameter)
#         counter += 1

# # call
# print_x_times() 

# # hypotenuse calculator function

# def hypotenuse_calculator(height, width):
#     hypotenuse = (height ** 2 + width ** 2) ** (1/2)
#     return round(hypotenuse, 2)

# print(hypotenuse_calculator(1, 1))

# exercise 

def shouter(string = 'string', number = 1):
    if number < 10:
      for i in range(number):
        print(string.upper())
    else:
        print('you are too loud')
    return 'done'        

print(shouter('hello', 5))        