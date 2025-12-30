import random
choices=["rock","paper","scissors"]
user_score=0
computer_score=0
while True:
    user=input("Choose rock,paper,scissors:").lower()
    computer=random.choice(choices)
    print("Computer chose:",computer)
    if user==computer:
        print("It's a tie!")
    elif(user=="rock"and computer=="scissors")or(user=="scissors"and computer=="paper")or(user=="paper"and computer=="rock"):
         print("you Win!")
         user_score+=1
    else:
        print("Computer Wins!")
        computer_score+=1
    print(f"Score->You:{user_score}|Computer:{computer_score}")
    again=input("Play again?(yes/no):").lower()
    if again!="yes":
        break