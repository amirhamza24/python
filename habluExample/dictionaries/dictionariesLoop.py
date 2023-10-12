studentInfo = {
    "student1": {
        "name": "Eshan",
        "group": "Science",
        "id": 4,
        "number": 22325343
    },
    "student2": {
        "name": "Jishan",
        "group": "Commerce",
        "id": 7,
        "number": 624255385
    },
    "year": 2023
}

for x in studentInfo:
    print(x)  # ekhane dictionaries er parent key gulo dekhabe.. output: student1 student2 year

for a in studentInfo.values():  # ekhane sob parent key er value dekhabe
    print(a)

for b in studentInfo.keys():  # ekhaneu dictionaries er parent key gulo dekhabe
    print(b)

for c in studentInfo.items():  # ekhane dictionaries er sob key with value 2 tai dekhabe
    print(c)
