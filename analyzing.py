import json

f = open("answers.json", "r")
x = json.load(f)
f.close()

sum_ages = 0
lst_ages = []
for i in x:
    temp = i["How old are you? "]
    if temp.isnumeric():
        age = int(temp)
        sum_ages += age
        lst_ages.append(age)

avg = sum_ages / len(x)

print(avg)

colors = []
for i in x:
    num = i["What is your favorite color? "]
    color = num.lower()
    colors += [color]
print(set(colors))
