import threading
from queue import Queue
import time
import numpy

startTime = time.time()

print_lock = threading.Lock()
counter = 0

def exampleJob(worker):
    matrix = numpy.random.rand(2000,2000)
    inv = numpy.linalg.inv(matrix)

    with print_lock:
        global counter
        counter +=1
        print(threading.current_thread().name,worker,'\n',inv)

def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

q = Queue()

for i in range(10):#number of threads
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(20):
    q.put(worker)

q.join()

print('entire job took',time.time()-startTime,'\nand the counter is',counter)
input('press any key to exit...')
