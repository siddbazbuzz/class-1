#wap in such a way that when user enters input 'ram' as a name break loop and print the list 
#otherwise keep on appending items to list and ask for next input from terminal
name=["asd"]
i=0
while(name[-1]!="ram"):
    i += 1
    name.append(input("enter your name: \n"))
    print(name)                                 
    