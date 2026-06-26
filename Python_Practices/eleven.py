# 11. Create a dictionary of usernames and passwords. Ask the user to enter username and password and check if the login is valid or invalid.

dict = {
    "mann":123,
    "mann2":1234,
    "mann3":12345,
    "mann4":123456,
    "mann5":1234567,
    
}


username = input("enter the username : ")
password = int(input("enter the password : "))

if username in dict and dict[username] == password:
    print("Valid login")
else:
    print("Invalid login")