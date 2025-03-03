import random
print("Welcome to Rock Paper Scissors game")
print("What do you choose? Type 0 for Rock Type 1 paper Type 2 Scissors ")
type=["Rock ","Paper","Scissor"]
symbol=["✊","✋","✌️"]
choice = int(input("Enter your choice: "))
if choice == 0:
    print("You chose Rock" ,symbol[0])
elif choice==1:
    print("You chose Paper" ,symbol[1])
else:
    print("You chose Scissor" ,symbol[2])


computer = random.randint(0, 2)
if computer == 0:
    print("Computer chose Rock" ,symbol[0])
elif computer == 1:
    print("Computer chose Paper" ,symbol[1])
else:
    print("Computer chose Scissor" ,symbol[2])

if (choice==0 & computer==2)|(choice==2 & computer==1)|(choice==1 & computer==0):
    print("You win!")
elif choice==computer:
    print("It's a tie!")
else:
    print("Computer wins!")

    
 