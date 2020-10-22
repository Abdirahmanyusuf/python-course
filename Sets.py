Students = {"Aamina", "Mohamed", "Abdirahman","Ali","Yaasmiin","Omar"}
print(Students)

# Note: the set list is unordered, meaning: the items will appear in a random order.


Students = {"Aamina", "Mohamed", "Abdirahman","Ali","Yaasmiin","Omar"}

for z in Students:
    print(z)

# Loop through the set, and print the values:

# Add Items
Students = {"Aamina", "Mohamed", "Abdirahman","Ali","Yaasmiin","Omar"}
Students.add("Sakariye")
print(Students)

# Add multiple items to a set, using the update() method:
Students = {"Aamina", "Mohamed", "Abdirahman","Ali","Yaasmiin","Omar"}
Students.update(["Najma","Salma","isra","Sahra"])
print(Students)

# Get the Length of a Set
Students = {"Aamina", "Mohamed", "Abdirahman","Ali","Yaasmiin","Omar"}
Students.update(["Najma","Salma","isra","Sahra"])
print(len(Students))

# assignment Remove Item
# 