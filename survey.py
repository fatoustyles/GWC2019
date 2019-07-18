import json

def takesurvey(questions, answers):
    answer = {}
    for q in questions:
        answer[q] = input(q)
    answers.append(answer)


answers = []
questions = ["What is your name? ", "How old are you? ", "What is your favorite color? ", "What month is your birthday in? ", "What is your least technical term? ", "What is your Hogwarts House? ", "What is your favorite song? ", "What state do you live in? "]


while(input("Continue Y/N ") == "Y"):
    print("NEW SURVEY!")
    takesurvey(questions, answers)
print(answers)
print(type(answers))

json.dumps(answers)
f = open("answers.json", "w")
f.write(json.dumps(answers))
f.close()
