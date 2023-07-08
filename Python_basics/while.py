#i = 10
#while i <= 15:
#   print(i)
#   i += 1
#print("done")

i = 1
while (i <= 3):
    guess= int(input("Guess: "))
    if(guess == 9):
        print("You win")
        break
    elif(i == 3):
        print("You lose")
        break
    i += 1
