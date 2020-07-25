my_set = {char for char in "hello"}

print(my_set)

# dictionary
simple_dict = {
    "a": 1,
    "b": 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}

print(my_dict)

my_dict2 = {num: num*2 for num in [1, 2, 3]}

print(my_dict2)
