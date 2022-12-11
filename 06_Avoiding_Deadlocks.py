# import 
# import threading

# # avoid deadlocks by using a lock hierarchy
# def avoidDeadlocks():
#     # create a lock hierarchy
#     lock1 = threading.Lock()
#     lock2 = threading.Lock()
#     # create a thread to acquire lock1
#     thread1 = threading.Thread(args=(lock1, lock2))
#     # create a thread to acquire lock2
#     thread2 = threading.Thread(args=(lock2, lock1))
#     # start the threads
#     thread1.start()
#     thread2.start()
#     # wait for the threads to finish
#     thread1.join()
#     thread2.join()
    