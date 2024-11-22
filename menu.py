import pandas as pd
from decorator import Decorator
from args_kwargs import Args_kwargs
from employee import Employee
from base_class import Base_class
from person import Student
from joins import Joins

print("Python basic.")

print("\nMENU: \n1.Print.\n2.Decorators.\n3.Args&Kwarg.\n4.Privated, protected and public.",end="")
print("\n5.Paralelism.\n6.Super.\n7.Dictionaries.\n8.Exit!")

option=int(input())

while option!=8:
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
    
    elif option==7:
        print("Developing")
        item_number=int(input("Type number of items "))
        key01=[]
        key02=[]       
        values01=[]
        values02=[]
        indexes01=[]
        indexes02=[]
              
        for i in range (0,item_number):
            key01.append(input("Type key "))
            values01.append(input("Type value "))
            indexes01.append(key01)            
        dictionary01=({str(key01):str(values01)})
        print(dictionary01)
        for j in range (0,item_number):
            key02.append(input("Type key "))
            values02.append(input("Type value "))
            indexes02.append(key02)            
        dictionary02=({str(key02):str(values02)})
        print(dictionary02)

        df01=pd.DataFrame(dictionary01,index=indexes01)
        df02=pd.DataFrame(dictionary02,index=indexes02)
        Joins.joins_df(df01,df02)       
        
    print("\nMENU: \n1.Print.\n2.Decorators.\n3.Args&Kwarg.\n4.Privated, protected and public.",end="")
    print("\n5.Paralelism.\n6.Super.\n7.Dictionaries.\n8.Exit!")

    option=int(input())

