# i = 0
# for x in range(10):
#     if x % 2 != 0:
#         i += x
#         print(x)
# print(i)

#
# def greetings():
#     print("Hello World")
#
# greetings()
# display = ""
# while True:
#     i = 0
#     i +=1
#     if i > 10:
#         display += "?"
#     else:
#         display += "@"
# print(display)
#
# str1 = "fireflies"
# str2 = "another"
# display = ""
# temp = ""
# for letter in str1:
#     if letter not in str2:
#         display += letter
#         temp += letter
#     else:
#         temp+= letter
#         print(temp)
# print(display)

x, y, z = 10, 15, 20
while x > y:
    print(f"x:{x} y:{y}")
    x -= 1
    y += 1
if x > y:
    print("hello")
else:
    if z > y and z > x:
        print("wow")
        if y < x:
            print("yes")
        else:
            print("no")
    else:
        print("okay")
