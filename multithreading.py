import thread
import time
def print_time(threadname,delay):
    count=0
    print("countvalue%dfor%s"%(count,threadname))
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s%s"%(threadname,time.ctime(time.time())))
try:
   thread.start_new_thread(print_time,("thread-1",2))
   print("omg")
except :
    print("error")
try :
    thread.start_new_thread(print_time,("thread-2",3))
except:
    print("error 2:")

