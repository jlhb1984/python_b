class Base_class:
    def __init__(self):
        self.protected_variable='Protected'
        self.__private_variable='Private'

    def _protected_method(self):
        print('Protected method.')

    def __private_method(self):
        print('Private method.')
    
    def public_method(self):
        print("Public method.")
        self.__private_method()