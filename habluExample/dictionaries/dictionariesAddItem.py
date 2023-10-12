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

studentInfo.pop("student2")  # remove the element with the specific key
print(studentInfo)

studentInfo.popitem()  # popitem a kono argument ba kono value dite hoyna, se emnitei dictionary er last er value ta remove kore dibe
print(studentInfo)