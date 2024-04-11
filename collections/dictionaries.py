# Dictionaries

# Key Value pairs
# Key is the reference, value is the storage mechanism

student1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up", "collections"]
}

print(student1["completed_lesson_names"][1])
student1["completed_lessons"] = 3
print(student1["completed_lessons"])
student1["completed_lesson_names"].pop()
print(student1["completed_lesson_names"])

# Getting the keys for a dict

print(student1.keys())