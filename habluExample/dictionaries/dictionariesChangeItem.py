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

# dictionaries change item
studentInfo["year"] = 2003
print(studentInfo["year"])

# # update dictionaries value
studentInfo.update({"student2": "Jishan is an CSE Student"})
print(studentInfo["student2"])