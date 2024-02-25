tuple = ('bob', 123, 'lisa', ('another list')) # immutable

list = ['bob', 123, 'lisa', ('another list')] # mutable

set = {1,2,3, 'test'} # every entry is unique

# key paired, kind of like an object

dictionary = {
    'name': 'bob',
    123: 'test',
    'lisa': (1,2,3)
}

# how to get values from a container

user_list = ['lisa', 'bob', 'joe', 'harry' ]
print(user_list[0:3])