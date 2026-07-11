# ============================================================================
#              INTERN PROJECT: CYBER SECURITY TOOLKIT (CST)
#                    Build a Mini Cybersecurity Toolkit
# ============================================================================
#
# OVERVIEW:
# You will build a command-line Cybersecurity Toolkit that combines
# everything you've learned from Day 1 to Day 7 into ONE program.
#
# The toolkit should display a menu and let the user pick a tool to use.
# The program should keep running until the user chooses to exit.
#
# ============================================================================
#
# YOUR TOOLKIT MUST HAVE THESE 5 TOOLS:
#
# ────────────────────────────────────────────────────────────────────────────
# TOOL 1: PASSWORD STRENGTH CHECKER
# ────────────────────────────────────────────────────────────────────────────
# - Ask the user to enter a password
# - Check the following:
#       → Is it at least 8 characters long?
#       → Does it contain at least one UPPERCASE letter?
#       → Does it contain at least one lowercase letter?
#       → Does it contain at least one number (digit)?
#       → Does it contain at least one special character? (!@#$%^&*)
# - Print which checks passed and which failed
# - Give a final rating: "Weak", "Medium", or "Strong"
#       → 1-2 checks passed = Weak
#       → 3-4 checks passed = Medium
#       → All 5 checks passed = Strong
#
# Concepts used: strings, string methods, loops, conditionals, functions
#
#
# ────────────────────────────────────────────────────────────────────────────
# TOOL 2: PASSWORD HASHER
# ────────────────────────────────────────────────────────────────────────────
# - Ask the user to enter a password
# - Display the hash of the password in:
#       → MD5
#       → SHA-256
#       → SHA-512
# - Then ask the user to re-enter the password
# - Hash the re-entered password and compare it to the original hash
# - Print "Match!" or "No Match!"
#
# Concepts used: hashlib module, string methods, conditionals, functions
#
#
# ────────────────────────────────────────────────────────────────────────────
# TOOL 3: PORT SCANNER (Basic)
# ────────────────────────────────────────────────────────────────────────────
# - Ask the user to enter an IP address (use "127.0.0.1" for testing)
# - Scan ports 1 to 100 using a loop
# - For each port, try to connect using socket
# - Print which ports are OPEN
# - At the end, print a summary:
#       → Total ports scanned
#       → Number of open ports
#       → List of open ports
#
# Concepts used: socket module, loops, lists, f-strings, functions
#
#

#
#
# ────────────────────────────────────────────────────────────────────────────
# TOOL 5: IP/DNS LOOKUP
# ────────────────────────────────────────────────────────────────────────────
# - Ask the user to enter a website name (e.g. "google.com")
# - Use socket.gethostbyname() to find the IP address
# - Display the result: "google.com → 142.250.x.x"
# - Allow the user to look up multiple websites in a loop
# - Store all results in a dictionary: {website: ip_address}
# - When the user is done, print all results in a clean format
#
# Concepts used: socket module, dictionaries, loops, functions, f-strings
#
#
# ============================================================================
#                         MAIN MENU (REQUIRED)
# ============================================================================
# Your program should display this menu when it runs:
#
#   ╔══════════════════════════════════════╗
#   ║      CYBERSECURITY TOOLKIT v1.0      ║
#   ╠══════════════════════════════════════╣
#   ║  [1] Password Strength Checker       ║
#   ║  [2] Password Hasher                 ║
#   ║  [3] Port Scanner                    ║
#   ║  [4] User Login System               ║
#   ║  [5] IP/DNS Lookup                   ║
#   ║  [0] Exit                            ║
#   ╚══════════════════════════════════════╝
#
# - The menu should keep showing after each tool finishes (use a while loop)
# - If the user enters an invalid option, print "Invalid choice, try again."
# - If the user enters 0, print "Goodbye!" and exit
#
#
# ============================================================================
#                      STRUCTURE / HINTS
# ============================================================================
# Organize your code like this:
#
#   1. Import your modules at the top (hashlib, socket, math)
#   2. Define your User class
#   3. Define a function for each tool:
#       - def password_checker():
#       - def password_hasher():
#       - def port_scanner():
#       - def login_system():
#       - def dns_lookup():
#   4. Define a function to display the menu: def show_menu():
#   5. Write your main while loop at the bottom that:
#       - Shows the menu
#       - Takes user input
#       - Calls the correct function based on the choice
#
#
# ============================================================================
#                      GRADING CRITERIA
# ============================================================================
#   - Code runs without errors                       → 20 marks
#   - All 5 tools work correctly                     → 40 marks (8 each)
#   - Menu loop works properly (with exit)           → 10 marks
#   - Used functions for each tool                   → 10 marks
#   - Used a class for the login system (Tool 4)     → 10 marks
#   - Clean output and good formatting               → 10 marks
#                                              TOTAL → 100 marks
#
# ============================================================================
#                      SUBMISSION
# ============================================================================
# Save your completed file as: CST_YourName.py
# Deadline: _______________
#
# ============================================================================


# START YOUR CODE BELOW THIS LINE
# ============================================================================


