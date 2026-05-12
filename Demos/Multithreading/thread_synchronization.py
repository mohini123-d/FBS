from threading import Thread,Lock
import time

def deposit(amt):
    lock.acquire()
    with open('core python/Demos/Multithreading/balance.txt','r')as fp:
        bal = int(fp.read())
        bal +=amt

    with open('core python/Demos/Multithreading/balance.txt','w')as fp:
        fp.write(str(bal))
    lock.release()

def withd(amt):
    lock.acquire()
    with open('core python/Demos/Multithreading/balance.txt','r')as fp:
        bal = int(fp.read())
        bal -=amt

    with open('core python/Demos/Multithreading/balance.txt','w')as fp:
        fp.write(str(bal))
    lock.release()

lock = Lock()

t1 = Thread(name='Thread1', target =deposit, args=(5000,))
t2 = Thread(name='Thread2', target =withd, args=(3000,))
t1.start()
t2.start()

    

