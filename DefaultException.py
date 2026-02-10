user_Data = {"name": "sdvdfaff", "email": "123@gmail.com"}

try:
    keyInput = input("Enter some Key Value to fetch:")
    print(user_Data[keyInput])
except KeyError:
    print("The key is not available")


# keyInput = input("Enter some Key Value to fetch:")
# print(user_Data[keyInput])
