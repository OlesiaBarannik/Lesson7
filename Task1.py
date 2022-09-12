

dictionary = {}

list_user = input("Please enter the keys: ").split()

for  key in list_user:
    if key in dictionary:
        dictionary[key] +=1
    else:
        dictionary[key] = 1

print(dictionary)






