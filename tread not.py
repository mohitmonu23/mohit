import thread
import time
def print_time(threadname,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s%s"%(threadname,time.ctime(time.time())))
print_time("thread1",1)
print_time("thread2",3)
