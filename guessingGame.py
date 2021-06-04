number=int(input("Enter Your Guess: "))


while chances<5:
     if guess==number:
         print("Congratulation YOU WON!!!")
         break
          
          if not chances<5:
              print("You Lose!!! The number is",number)
