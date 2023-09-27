import copy

## Shallow copy

students = [
    {"name": "Balaji", "age": 23},
    {"name": "Sarvan", "age": 22},
    {"name": "Harish", "age": 21}
]

students_copy = students[:]
# students_copy = copy.copy(students)
students_copy[0]["age"] = 25

print("Original Students:\n", students)
print("Copied Students:\n",students_copy)


## Deep copy

application = {
    "software_name": "Hr-os",
    "database": {
        "host": "Terralogic",
        "port": 8080
    },
}

deep_copy = copy.deepcopy(application)

deep_copy["software_name"] = "Terralogic.com"
deep_copy["database"]["host"] = "Google"

print("Original application:\n",application)
print("Deep copy application:\n",deep_copy)

