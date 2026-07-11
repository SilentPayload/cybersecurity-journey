# try:
#     result = 10 / 0
# except:
#     print("something went wrong. cannot divide by 0")

# print()

# def cvss_rating(score_input):
#     try:
#         score = float(score_input)
#         if score < 0 or score > 10:
#             print("CVSS score must be between 0.0 and 10.0")
#             return
        
#         if score >= 9.0:
#             print(f"Score {score}: Critical ")
#         elif score >= 7.0:
#             print(f"Score {score}: High")
#         elif score >= 4.0:
#             print(f"Score {score}: Medium")
#         else:
#             print(f"Score {score}: Low")

#     except ValueError:
#         print("Error! Please Enter a number like 4.9")
#     except TypeError:
#         print("Error! Please enter the right data type")

# cvss_rating("9.8")
# cvss_rating("five")
# cvss_rating("2.4")
# cvss_rating("4 point 5")

# print()


# def read_log_file(filename):
#     try:
#         file = open(filename, "r")
#         content = file.read()
#         file.close()
#         print("Log file loaded successfully")
#         print("First 100 characters:", content[:100])

#     except FileNotFoundError:
#         print(f"Error The file {filename} does not exist")
#         print("Check path and try again")


#     except PermissionError:
#         print(f"Error You do not have the permission to read {filename}")
#         print("Try running the script as administrator")

#     except Exception as e:
#         print(f"Unexpected error: {e}")

# read_log_file("myfile")
# read_log_file("C:/Windows/System32")
# read_log_file(23)

# print()

# def connect_server(ip_address, port):
#     try:
#         parts = ip_address.split(".")
#         if len(parts) != 4:
#             raise ValueError("Not a valid ip address")
        
#         port_num = int(port)
#         if not (1 <= port_num <= 65535):
#             raise ValueError("Port must be between 1 and 65535.")
        
#     except ValueError as e:
#         print(f"Error: {e}")
#         return
        
#     print(f"Connecting to {ip_address} on port {port_num}")
#     print("Connection established successfully. ")

# connect_server("192.168.43.128", "22")
# connect_server("192.168.43.128", "99999")
# connect_server("192.168.43.128", "89")
# connect_server("192.168.43.128", "80")


# print()

# def login(username, password):
#     valid_users = {"ian": "SecurePass123", "John": "Admin2026"}
#     try:
#         if not isinstance(username, str) or not isinstance(password, str):
#             raise TypeError("Username and password must be text")
        
#         if username not in valid_users:
#             raise ValueError(f"Username: {username} not found.")
#         if valid_users[username] != password:
#             raise KeyError("Incorrect Password.")
        
#     except TypeError as e:
#         print(f"Login Error Type Problem {e}")

#     except KeyError as e:
#         print(f"Login error: {e}")

#     except ValueError as e:
#         print(f"Login error: {e}")

#     else:
#         print(f"Login Successful, welcome {username}")
#     finally:
#         print("Login attempt logged.")


# login("Praix", "Securepass99")
# login("Praix", "Securepass123")
# login("John", "Admin2026")
# login(123, "password")


# place = "Nyanya"
# for letter in place:
#     print(letter)

import hashlib
word = "ekwonyeaso"
print(hashlib.sha256(word.encode()).hexdigest())