# python is a high level programming language -- meaning it is easy to understand and written in plain, readable english like syntaxc rather than complex machine code
print("Hello World")


print()
# A variable is a BOX that stores information
name = "Joseph"
print(name)
plate = "Rice"

print(plate)
# Rules when creating a variable
# A variable cannot be created starting with digits but can end with one....
# A variable shouldn't contain spaces instead underscores are used
# A variable cannot be created using key reserved words --> # if, else, elif, for, while, True, False, str, int --> key reserved words

name1 = "jonathan"

this_is_available = True

print()

#Datatypes in python
# integar --> whole numbers
# string --> texts
# float --> Decimal numbers
# Boolean --> True or false


#Integars
add_1 = 100
add_2 = 200

print(add_1 + add_2)

# Strings

about_me = "My name is dami and i am in abuja"
print(about_me)

#Floats

add_3 = 200.45
print(add_1 + add_2 + add_3)


#Boolean
is_true = True
is_false = False
print(is_true)
print(is_false)

print()

#string formatting
# string method 

name = "Stephen"
state = "Nasarawa"

statement = "My name is {name} and i am from {state} state. "
print(statement.format(name=name, state=state))

# f-string method
mystatement = f"i have a friend, his name is {name} and he is from {state} state."
print(mystatement)


print()

#string concatenation -->  joining 2 or more strings/variables together

# string + string method

print("Hello" + "World")
print("Hello" + " " + "World")

# string + variable
word = "Hello"
print(word + " " + "World")


# variable + variable

word1 = "Hello"
word2 = "World"
print(word1 + word2)
print(word1 + " " + word2)

print()

info = ' coding is fun'
info1 = 'HAPPY SATURDAY'

print(info.upper())
print(info1.lower())
print(info1.capitalize())
print(info.title())
print(info.split())
print(info.strip())
print(info1.replace('SATURDAY', 'SUNDAY'))

print()


details = """
Name: Atiku
Age: 100
Country : USA

"""

print(details)