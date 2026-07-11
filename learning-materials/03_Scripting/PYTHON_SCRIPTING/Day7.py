# Object Oriented programming --> OOP
# OOP helps a user combine data and functions into something called a class
# CLASS --> The blueprint
# Object --> the thing we built from the blueprint
# Instance --> same as object
# Attribute - data stored inside the object
# Method - a function inside a class
# __init__ --> constructor: runs when an object is created
# self --> refers to the current object
# Dot(.) --> How you access the attributes and methods

# OOP SYntax
# class Classname:
#     def __init__(self):
#         pass

class UserAccount:
    def __init__(self, username, role):
        self.username = username
        self.role = role

account1 = UserAccount("godwin", "admin")
account2 = UserAccount("dami", "moderator")
account3 = UserAccount("praiz", "user")

print(account1.username)
print(account2.role)
print(account3.username)

print()
# adding a method to useraccount
# just a function inside a class
# it always takes the first parameter
class UserAccount:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Role: {self.role}")

    def greet(self):
        print(f"Hello, {self.username}, you are logged in as {self.role}")

account1 = UserAccount("godwin", "user")
account2 = UserAccount("dami", "admin")

account1.display_info()
account2.greet()

print()
# Methods can use the object's own data (self.attribute)
# And they accept extra parameters

# a method that checks login permission

class UserAccount:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.is_logged_in = False

    def login(self):
        self.is_logged_in = True
        print(f"{self.username} has logged in")

    def logout(self):
        self.is_logged_in = False
        print(f"{self.username} has logged out.")

    def check_access(self, resource):
        if self.role == "admin":
            print(f"{self.username} can access {resource}")
        else:
            print(f"{self.username} Access-Denied for: {resource}")

admin = UserAccount("dami", "admin" )
admin1 = UserAccount("godwin", "admin")
regular = UserAccount("praiz", "user")

admin.login()
admin1.login()
admin.check_access("Server Logs")
admin1.check_access("User database")
regular.login()
regular.check_access("MariaDB")
regular.logout()

print()

class NetworkDevice:
    def __init__(self, ip_address, device_type="unknown", is_online=False):
        self.ip_address = ip_address
        self.device_type = device_type
        self.is_online = is_online
        self.open_ports = []

    def bring_online(self):
        self.is_online = True
        print(self.ip_address, "is now online")

    def add_open_port(self, port):
        self.open_ports.append(port)
        print(f"Port {port} added to {self.ip_address}")

    def show_status(self):
        status = "ONLINE" if self.is_online else "OFFLINE"
        print("---------------")
        print(f"IP ADDRESS: {self.ip_address}")
        print(f"TYPE: {self.device_type}")
        print(f"STATUS: {status}")
        print(f"OPEN PORTS: {self.open_ports}")
        print("---------------")

router = NetworkDevice("192.168.43.128", "router")
server = NetworkDevice("10.23.65.74", "web server")

router.bring_online()
router.add_open_port(80)
router.add_open_port(443)
router.show_status()


server.add_open_port(22)
server.bring_online()
server.show_status()

        