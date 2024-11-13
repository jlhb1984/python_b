class Decorator:
    cad1=str
    cad2=str

    def __init__(self,cad1,cad2):
        self.cad1=cad1
        self.cad2=cad2

    def log_transaction(func):
        def wrapper():
            print('1 Log de la transacción...')
            func()
            print('3 Terminado')
        return wrapper
    
    @log_transaction
    def process_payment():
        print('2 Procesando pago...')