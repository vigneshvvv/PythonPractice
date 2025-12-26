userInput = int(input("please enter a number to proceed: "))
# result = "you have given a correct number" if(userInput <10) else "Enter a number within 10"
# print(result)

result = ("the Entered number is less than 5" if(userInput <5) else "The Entered Number is greater than 5") if(userInput <= 10) else "Enter a number within 10" 

print(result)
