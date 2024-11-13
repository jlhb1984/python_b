print("Python basic.")
from decorator import Decorator
option=int(input("\nMENU: \n1.Print.\n2.Decorators.\n3.Args&Kwarg.\n4.Exit! "))

while option!=4:
    if option==1:
        print('''Printing in 2
        lines''')
        break
    elif option==2:
        print("Working on decorators.")
        Decorator.process_payment()
        break
option=int(input("\nMENU: \n1.Print.\n2.Decorators.\n3.Args&Kwarg.\n4.Exit! "))
    

