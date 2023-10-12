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

 # accessing dictionaries items

print(studentInfo["student2"]["group"])
print(studentInfo["year"])

x = studentInfo.get("student2")
print(x)

key = studentInfo.keys()
print(key)

value = studentInfo.values()
print(value)
