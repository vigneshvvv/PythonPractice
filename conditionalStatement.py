userInput = int(input("please enter a number to proceed: "))

if(userInput <10):
    userInput *= 100
    print("you have given a correct number")
    print("congrats")
    print(userInput)

elif(userInput == 10):
    userInput /= 10
    print("You have entered correct number 10")  
    print(userInput)
else:
    print("Enter a number within 10")

