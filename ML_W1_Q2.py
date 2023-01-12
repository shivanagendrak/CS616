user = int(input("Enter the First Number: "))
user1 = int(input("Enter the Second Number: "))
user2 = int(input("Enter the Third Number: "))
if (user>=user1) and (user>=user2):
    Biggest = user
elif (user1>=user) and (user1>=user2):
    Biggest = user1
else:
    Biggest = user2
print("The Biggest Number is :",Biggest)