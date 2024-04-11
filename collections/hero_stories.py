# My Hero

# Define a dictionary called story1. It should have the following keys:
# 'start', 'middle' and 'end'
story1 = {
    "start": "Flyboy is a boy who can fly! At the age of 15 he discovered this power and 3 years later he's still flying around. ",
    "middle": "A kid was stuck in a burning building, people screamed for a hero... then Flyboy flew into the scene. ",
    "end": "After saving the small kid Flyboy flew home and went to sleep for the day. ",
}

# Print the entire dictionary
print(story1)
# Print the type of your dictionary
print(type(story1))
# Print only the keys
print(story1.keys())
# Print only the values
print(story1.values())
# Print the individual values using the keys
print(story1["start"])
print(story1["middle"])
print(story1["end"])
# Now, let's add a new key:value pair:
story1["hero"] = "Flyboy ... the boy who can fly"
print(story1.keys())