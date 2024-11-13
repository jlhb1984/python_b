import threading
import time
import multiprocessing

#def calculate_square(n):
    #return(n*n)

#with multiprocessing.Pool() as pool:
#   result=pool.map(calculate_square,numbers)

def process_request(request_id):
    print(f'Procesando solicitud {request_id}')
    time.sleep(3)
    print(f'Solicitud{request_id}completada')

threads=[]

for i in range(3):
    thread=threading.Thread(target=process_request,args=(i,))
    threads.append=(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Todas las funciones completadas.")