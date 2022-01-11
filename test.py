import json

'''
response = input("insert a number.  ")

first = None
second = None
third = None
fourth = None
decimal1 = None
decimal2 = None

if len(response) == 7 and "." in response:
    over_all_value = response.split(".")
    value1 = over_all_value[0]

    if value1[0] == "1":
        first = "one thousand"
    elif value1[0] == "2":
        first = "two thousand"
    elif value1[0] == "3":
        first = "three thousand"
    elif value1[0] == "4":
        first = "four thousand"
    elif value1[0] == "5":
        first = "five thousand"
    elif value1[0] == "6":
        first = "six thousand"
    elif value1[0] == "7":
        first = "seven thousand"
    elif value1[0] == "8":
        first = "eight thousand"
    elif value1[0] == "9":
        first = "nine thousand"

    if value1[1] = "0":
'''

with open("data.json", mode="r") as datafile:
    data = json.load(datafile)
    name = data['115079']["name"]
    print(name)
