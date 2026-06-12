"""students={
    "name":"Ahammed",
    "age":25,
    "city":"Kerala",
    "country":"India",
    "hobbies":["coding","traveling","cooking"],
    "education":"Bachelor's in Computer Science",
    "bike":"ktm",
}


print(students["name"])"""



## Adding new key-value pair to the dictionary
'''students={
    "name":"Ahammed",
    "age":25,
    "city":"Kerala",
    "country":"India",
    "hobbies":["coding","traveling","cooking"],
    "education":"Bachelor's in Computer Science",
    "bike":"ktm",
}
students["job"]="Data Scientist"
print(students["job"])
'''



## Deleting a key-value pair from the dictionary
students={
    "name":"Ahammed",
    "age":25,
    "city":"Kerala",
    "country":"India",
    "hobbies":["coding","traveling","cooking"],
    "education":"Bachelor's in Computer Science",
    "bike":"ktm",
}


del students["age"]
print(students)