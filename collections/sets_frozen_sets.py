# Sets and Frozen Sets

# Sets are unordered and unindexed
fruits = {"apple", "bananas", "cherry"}
print(fruits)
print(type(fruits))

# Add
fruits.add("orange")
print(fruits)

# Remove
fruits.remove("apple")
print(fruits)

# Doesn't allow duplicates
fruits.add("bananas")
print(fruits)

# Convert list to a set to remove duplicates

example = ["1", "2", "3", "1", "4", "4", "5", "6", "7", "8", "9", "10"]
no_dupes = set(example)
print(no_dupes)

# Convert set to list to remove dupes first then organise later thought for later

# Frozo set immutable
froz_set = frozenset({"hello", "world"})
print(froz_set)
print(type(froz_set))
# froz_set.add("!")
# print(froz_set)