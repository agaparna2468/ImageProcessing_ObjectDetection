flag= False
while True:
    inst = input(">").lower()
    if(inst =="help"):
        print("start- to start the car \nstop- to stop the car \nquit- to end the game")
    elif (inst =="start"):
        if( flag == False):
            print("started the car")
            flag = True
        else:
            print("already started the car")
    elif (inst =="stop"):
        if (flag == False):
            print("car already stop")
        else:
            print("stopped")
            flag= False
    elif (inst =="quit"):
        print("game end")
        break
    else:
        print("I don't understand")

