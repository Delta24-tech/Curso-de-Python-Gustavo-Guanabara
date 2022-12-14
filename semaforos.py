#RA:60101-2, Thomaz Medeiros de Queiroz
#RA:608009, Rafael Amorim
#RA:590541, Richard Hiroshi da Silva Nishizaki
import _thread
import time, random
saldo = 0
s = _thread.allocate_lock()
def tempo(i):
 t = random.randint(3,7)
 print("Processo %i dormindo por %i\n" %(i, t))
 time.sleep(t)
def thread1():
 global saldo   
 while True:
  print("Processo 1 - Adquirindo semáforo")
  s.acquire()
  saldo+=1
  print("Saldo antes do depósito: ",saldo)
  print("Processo 1 - Seção crítica")
  tempo(1)
  print("Processo 1 - Liberando semáforo\n")
  s.release()
  print("Processo 1 - seção não crítica\n")
  tempo(1)
def thread2():
 global saldo   
 while True:
  print("Processo 2 - Adquirindo semáforo")
  s.acquire()
  saldo-=1
  print("Saldo depois do depósito: ",saldo)
  print("Processo 2 - Seção crítica")
  tempo(2)
  print("Processo 2 - Liberando semáforo\n")
  s.release()
  print("Processo 2 - seção não crítica\n")
  tempo(2)
_thread.start_new_thread(thread1, ())
_thread.start_new_thread(thread2, ())
while 1: pass






 
    












































































































































