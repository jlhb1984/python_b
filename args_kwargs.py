class Args_kwargs:

    def __init__(self,numbers):
        self.numbers=numbers

    def sum_numbers(*args):
        return sum(args)
    
    def print_info(**kwargs):
        for key,value in kwargs.items():
            print(f'{key}:{value}')
    
    