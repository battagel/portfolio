""" 
This is an example of multi-threading in python. In this file both these
classes execute with a defined delay to get them to alterate printing. To enable
multi-threading make the class inherit the Thread class and then instead of
calling the run() method use start() which automatically starts the thread
AND calls the run method
"""


from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for _ in range(5):
            print("hello")
            sleep(0.5)
    
class Hi(Thread):
    def run(self):
        for _ in range(5):
            print("hi")
            sleep(0.5)

t1 = Hello()
t2 = Hi()

# Start each thread off the main thread. Give a sleep inbetween to stop collision
t1.start()
sleep(0.2)
t2.start()

# Join back both threads to main thread BEFORE running the next lines
t1.join()
t2.join()

print("bye")

