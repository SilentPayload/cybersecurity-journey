# # This is the my first path in python for cybersecurity. Firstly i had to understand or learn the basic syntax of python
# Variable --> is simply a box that stores or carries information
# We create a variable using the assignment operator (=)

# Rules to follow when creating a variable
# ------------------------------------------------------------
# 1. Variables cannot be created starting with a number
# 2. Variables cannot be created using spaces or caught having spaces. Instead we use an  under score
# 3. Variables are case sensitive
# 4. We do not use special characters when creating a variable.
# 5. We do not use key reserve words to create a variable(e.g if, else, elif, for, while....etc)

# Variable --> is simply a box that stores or carries information
# We create a variable using the assignment operator (=)

# Rules to follow when creating a variable
# ------------------------------------------------------------
# 1. Variables cannot be created starting with a number
# 2. Variables cannot be created using spaces or caught having spaces. Instead we use an  under score
# 3. Variables are case sensitive
# 4. We do not use special characters when creating a variable.
# 5. We do not use key reserve words to create a variable(e.g if, else, elif, for, while....etc)

number = 5
print(number)
number1 = 32
print(number1)

my_name = "praise"
print(my_name)


# Datatypes in Python
# integar --> Whole numbers:
# string --> texts:
# float --> Decimal numbers:
# boolean --> Conditions True or False:
# number2 = 50
# type(number2)



cat = 'Lucy'
type(cat)
height = 6.4
type(height)
is_ofure_a_male = False
type(is_ofure_a_male)
# --> Comment
# Multi line string (''', """)
information = """
Personal Information
Name: Joy
Age: 16
Nationality: Nigerian
Occupation: Student
"""

print(information)
# String Formatting --> Injecting variables into a string
# Format method
# F-string method


# format method
Name = "Blessing"
State = "Anambra"

statement = "My name is {Name} and i am from {State} state."
print(statement.format(State=State, Name=Name))


# Fstring method 
action = "going"
place = "school"

sentence = f"i am {action} to {place}"
print(sentence)

print(f"My name is {Name} and i am from {State} state")
# String concatenation
# string and string method
print("Hello " + "World")
print("Hello" + " " + "World")
print("Hello","World")

#String and variables



# string and variables
explore = "Laptop"
explore1 = "Phone"

print("i have a", explore)
print("I have a", explore, "and a", explore1, "that my sister got me for my birthday")
# variable and variable
protocol = "https"
domain = "apple.com"

url = protocol + "://" + domain
print(url)
ip = "192.148.2.1"
port = "22"
target = ip + ":" + port
print(target)

type(port)
info = " coding is fun"
info1 = "HAPPY WEDNESDAY"
print(info.upper()) # --> Uppercase
print(info1.lower()) # --> Lowercase
print(info1.capitalize()) # --> First letter upercase
print(info.title()) # --> First letter of each word uppercase
print(info.split()) # --> Splits each word
print(info.strip()) # --> Removes unecessary spaces
print(info1.replace("WEDNESDAY", "THURSDAY"))
