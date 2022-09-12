

text = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday"
day_of_week = text.split(" ")

print(day_of_week)


day = {}

for i, key in enumerate(day_of_week):
	day[key] = i+1
print(day)

day_revers = {}

for i, key in  day.items():
	day_revers[key] = i
print(day_revers)





