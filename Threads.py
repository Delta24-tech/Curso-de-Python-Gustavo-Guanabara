from threading import *
def imprimir():                
    for i in range(10): 
         print("Thread - filho") 
      
Thread_obj = Thread(target=imprimir)         
Thread_obj.start()
for i in range(10):             
     print("Thread - pai") 
