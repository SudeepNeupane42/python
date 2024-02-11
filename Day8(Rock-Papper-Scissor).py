import random
s=[1,2,3]
while 1:
    n = int(input("\nEnter your choice:\n1.Rock\n2.Paper\n3.Scissors\n4.exit\n"))
    print("")
    i=random.choice(s)
    match n:
        case 1:
                if i==1:
                    print("Draw")
                elif i==2:
                    print("lose")
                else:
                    print("win")          
        case 2:
                if i==1:
                    print("win")
                elif i==2:
                    print("Draw")
                else:
                    print("Lose")                                 
        case 3:           
                if i==1:
                    print("Lose")
                elif i==2:
                    print("Win")
                else:
                    print("Draw")                
        case _:
            exit()
