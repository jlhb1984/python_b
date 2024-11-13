from decorator import Decorator
from args_kwargs import Args_kwargs
from employee import Employee
from base_class import Base_class

print("Python basic.")

option=int(input("\nMENU: \n1.Print.\n2.Decorators.\n3.Args&Kwarg.\n4.Privated, protected and public.\n5.Exit! "))

while option!=5:
    if option==1:
        print('''Printing in 2
        lines''')
        
    elif option==2:
        print("Working on decorators.")
        Decorator.process_payment()
        
    elif option==3:        
        sum1=Args_kwargs.sum_numbers(1,2,3)
        sum2=Args_kwargs.sum_numbers(98,2)
        print("Sum1= ",sum1)
        print("Sum1= ",sum2)
        Args_kwargs.print_info(name='Jose',age=40,city='Cali')
        employee=Employee('Luis','Python','Java','C++',age=40,city='Cali')
        employee.show_employee() 

    elif option==4:
        print("Accesing a private method from a public one!")
        base=Base_class()
        base.public_method()          
    option=int(input("\nMENU: \n1.Print.\n2.Decorators.\n3.Args&Kwarg.\n4.Privated, protected and public.\n5.Exit! "))
    

