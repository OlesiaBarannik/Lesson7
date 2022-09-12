# user_list = []
#
# for i in range (1, 11):
#     j = i**2
#     user_list.append((i, j))
#
# print(user_list)


user_list = []

[user_list.append((i, i**2)) for i in range(1,11)]

print(user_list)

