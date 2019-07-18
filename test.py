answer = input("What is your name?")
print ("Hello", answer,  "stan loona!")
print (f"Hello{answer}")
i = -1
while True:
    i += 1
    if(i > 20):
        break
    if (i % 2 != 0):
        continue
    print(i)
