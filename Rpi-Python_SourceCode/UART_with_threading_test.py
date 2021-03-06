from UART_interface import *
from queue import Queue
from threading import Timer,Thread, Lock

def PrintQueue():
    global uart_q
    # print(list(uart_q.queue))
    timer1 = Timer(1,PrintQueue)
    timer1.start()


def FillQueue(the_q, the_lock):
    while True:
        rx=UART_Getline()
        print(rx)
        with the_lock:
            the_q.put(rx)
        # the_q.task_done()

UART_Init()

lock = Lock()
uart_q = Queue()
timer1 = Timer(1,PrintQueue)
uart_thread = Thread(target=FillQueue, args=(uart_q,lock)) 
uart_thread.daemon = True

uart_thread.start()
timer1.start()

while True:
    pass