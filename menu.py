from decorator import Decorator
from args_kwargs import Args_kwargs
from employee import Employee
from base_class import Base_class
from person import Student

print("Python basic.")

print("\nMENU: \n1.Print.\n2.Decorators.\n3.Args&Kwarg.\n4.Privated, protected and public.",end="")
print("\n5.Paralelism.\n6.Super.\n7.Exit!")

option=int(input())

while option!=7:
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

    elif option==5:
        #id1: int x = 1
        #id2: int y = 2 
        print('Developing.')
    
    elif option==6:
        student=Student("Ana",20,"S123")
        student.greet()

    print("\nMENU: \n1.Print.\n2.Decorators.\n3.Args&Kwarg.\n4.Privated, protected and public.",end="")
    print("\n5.Paralelism.\n6.Super.\n7.Exit!")

    option=int(input())

