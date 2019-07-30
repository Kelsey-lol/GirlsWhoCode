#the_dictionary = {}

dictionary = {}

questions = ["What is your name?",
    "What is your favorite season? ",
    "What is your favorite color? ",
    "What is your favorite fruit? ",
    "What is your favorite candy? "]

keys = ["name",
    "season",
    "color",
    "fruit",
    "candy"]

keys = ["name", "season", "color", "fruit", "candy"]
allUsers = []

done = "no"
while done == "no":
    answers = {}

    index = 0
    for q in questions:
        ans = input(q)
        answers[keys[index]] = ans
        index += 1
        allUsers.append(answers)
    done = input("Are you finished? (yes or no): ")
print(allUsers)

import json

with open("list.json") as f:
    try:
        olddata = json.load(f)
    except ValueError:
        olddata = []
allUsers.extend(olddata)
f.close()

f = open ("list.json", "w")
json.dump(allUsers, f)
f.close()

count = 0
scount = 0
fwcount = 0

for u in allUsers:
    count += 1
    ans = u["season"]
    if ans == "summer" or "spring":
        scount += 1
    else:
        fwcount += 1

if scount > fwcount:
    print(str(scount) + " out of " + str(count) + " like the warm wether IT IS NOT WORKING")
elif fwcount > scount:
    print(str(fwcount) + " out of " + str(count) + " like the cold wether")
