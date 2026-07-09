# Implicit --> this automatically assigns the value to the right data type
# Explicit --> The user converts the datatype for a variable

# Implicit
x = 50
type(x)

#explicit
y =  "200"
z  = "500"
print(int(y) + int(z))
# input function --> Used to collect data from a user in a program
name = input("Enter your name: ")
print(name)
name1 = input("Enter Your name: ").strip()
print(name1)
pin = int(input("Enter Your pin: "))
print(pin)
# Operators are special symbols that perform operations in a program
"""
Arithmetic Operators
Addition --> (+)
Subtraction --> (-)
Multiplication --> (*)
Division --> (/)
Floor Division --> (//)
Exponential --> (**)
Modulus --> (%)
"""

num = 70
num1 = 60
print(f"{num} + {num1} = {num + num1}")
print(f"{num} - {num1} = {num - num1}")
print(f"{num} * {num1} = {num * num1}")
print(f"{num} / {num1} = {num / num1}")
print(f"{num} // {num1} = {num // num1}")
print(f"{num} ** {num1} = {num ** num1}")
print(f"{num} % {num1} = {num % num1}")
# Assignment Operator --> (=)



"""
Comparism operators
Greater than (>)
Less than (<)
Equal to (==)
Greater than or equal to (>=)
Less Than or equal to (<=)
Not equal to (!=)
"""
NUM = 62
NUM1 = 60
print(f"{NUM} > {NUM1} = {NUM > NUM1}")
print(f"{NUM} < {NUM1} = {NUM < NUM1}")
print(f"{NUM} == {NUM1} = {NUM == NUM1}")
print(f"{NUM} >= {NUM1} = {NUM >= NUM1}")
print(f"{NUM} <= {NUM1} = {NUM <= NUM1}")
print(f"{NUM} != {NUM1} = {NUM != NUM1}")
# Logical Operators --> (and, or , not)
word = True
word1 =False
print(word and word1)
print(word or word1)
print(not word)
print(not word1)
# Membership operator --> Check if an item exists --> (in, not in)
place = 'Nyanya'
print('N' in place)
print('a' not in place)
# Identity operator --> (is, is not)
WORD = "Early"
WORD1 = "Late"
print(WORD is WORD1)
print(WORD is not WORD1)
"""
Build a login banner generator
1. Ask the user for their name
2. Ask for their role
3. Ask the user to enter his shift
4. combine the inputs into a welcome banner
"""


"""
===========Welcome to your cybersecurity dashboard=================
User: 
Role: 
Shift: 
"""
name = input("Enter name: ")
role = input("Enter Role: ")
shift = input("Enter Shift: ")

print("====Welcome to your cyber dashboard====")
print(f"User: {name}")
print(f"Role: {role}")
print(f"Shift: {shift}")
