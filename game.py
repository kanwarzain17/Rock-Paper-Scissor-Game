
import random
choices = ['rock', 'paper', 'scissors']

while True:
    ccount=0
    ucount=0
    uc=int(input('''
    Game Start...
    1 Yes
    2 No
    
    '''))
    if uc==1:
        for i in range(1,6):

          userinput=int(input('''
    1 Rock
    2 Scissor
    3 Paper
    
    '''))
          if userinput==1:
            u_choice="rock"
          elif userinput==2:
              u_choice="scissor"
          elif userinput == 3:
              u_choice="paper"
          computer_choice=random.choice(choices)
          if computer_choice==u_choice:
            print("Computer chooses",computer_choice)
            print("User chooses", u_choice)
            print("It's a tie!")

          elif u_choice == 'rock' and computer_choice == 'scissors' or \
            u_choice == 'scissors' and computer_choice == 'paper' or \
            u_choice == 'paper' and computer_choice == 'rock':
            print("Computer chooses", computer_choice)
            print("User chooses", u_choice)
            print ("User win!")
            ucount = ucount + 1
          else:
             print("Computer chooses", computer_choice)
             print("User chooses", u_choice)
             print("Computer wins!")
             ccount = ccount + 1
    if ucount==ccount:
        print("Round Draw")
        print("User Score",ucount)
        print("Computer Score",ccount)
    elif ucount>ccount:
             print("User win the round")
             print("User Score", ucount)
             print("Computer Score", ccount)
    else:
        print("computer win the round")
        print("User Score", ucount)
        print("Computer Score", ccount)



