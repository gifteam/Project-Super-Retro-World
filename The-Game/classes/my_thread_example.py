import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(work):
    time.sleep(0.5)

    with print_lock:
        print(threading.current_thread().name, work)

def worker():
    while True:
        my_work = worklist.get()
        exampleJob(my_work)
        worklist.task_done()

worklist = Queue()

for x in range(10):
    t = threading.Thread(target = worker)
    t.daemon = True
    t.start()

start = time.time()

for work in range(20):
    worklist.put(work) #add work to the worklist

worklist.join() #wiat for the worklist to be done

print(r"Entire job took: ", time.time() - start)
