my_list = [5, 4, 3]

print(list(map(lambda item: item ** 2, my_list)))
# ya da
new_list = list(map(lambda item: item ** 2, my_list))
print(new_list)

# list sorting "ikinci öğeye göre sıralamak"

a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])
print(a)
