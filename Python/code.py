# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class =class_1 + class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.pop(5)
# Print the list
print(new_class)


# Create the Dictionary
courses = {'Math' : 65, 'English' : 70, 'History' : 80, 'French' : 70, 'Science' : 60}


# Slice the dict and stores  the all subjects marks in variable

total=courses['Math'] + courses['English'] + courses['History'] + courses['French'] + courses['Science']
print(total)

# Store the all the subject in one variable `Total`
percentage = (total * 100.0) / 500
print(percentage)
# Print the total

# Insert percentage formula

# Print the percentage




# Create the Dictionary
 
mathematics = {'Geoffrey Hinton' : 78, 'Andrew Ng' : 95, 'Sebastian Raschka' : 65, 'Yoshua Benjio' : 50, 'Hilary Mason' : 70, 'Corinna Cortes' : 66, 'Peter Warden' : 75}


# Given string
#max_marks_scored = max(mathematics,key = mathematics.get)
#print (max_marks_scored)
max_marks_scored = max(courses,key = courses.get)
print (max_marks_scored)
topper = max(mathematics,key = mathematics.get)
print(topper)
# Create variable first_name 
#first_name = topper.split()
x = topper.split()
first_name =x[0]
last_name = x[1]
# Create variable Last_name and store last two element in the list
full_name = last_name +" "+ first_name
certificate_name = full_name.upper()
# Concatenate the string
print(certificate_name)
# print the full_name

# print the name in upper case

# Code ends here


