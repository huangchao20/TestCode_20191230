# import threading
# import time
#
# def issettset(i, en):
#     while not en.isSet():
#         print(i + 10)
#
#     en.wait()
#     print(i+100)
#
# if __name__ == '__main__':
#     event = threading.Event()
#     for i in range(10):
#         t = threading.Thread(target=issettset, args=(i, event,))
#         t.start()
#         t.join()
#
#         inp = input(">>>>>>:")
#         if inp == "1":
#             event.set()

# from multiprocessing import Process
# import os
# import time
# def info(name):
#
#
#     print("name:",name)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#     print("------------------")
#     time.sleep(1)
#
# def foo(name):
#
#     info(name)
#
# if __name__ == '__main__':
#
#     info('main process line')
#
#
#     p1 = Process(target=info, args=('xuyaping',))
#     p2 = Process(target=foo, args=('egon',))
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print("ending")


# from multiprocessing import Process, Queue
#
# def son(i, q):
#     print("son ID:", id(q))
#     q.put( i * 3**3)
#
# if __name__ == '__main__':
#     q = Queue()
#     for i in range(3):
#         p = Process(target=son, args=(i, q,))
#         p.start()
#
#     print(q.get())
#     print(q.get())
#     print(q.get())

# from multiprocessing import Process, Pool
# import time
# def foo(i):
#     print(i)
#     time.sleep(1)
#
# if __name__ == '__main__':
#     pool = Pool(5)
#     for i in range(40):
#         pool.apply_async(func=foo, args=(i,))
#
#     pool.close()
#     pool.join()


from greenlet import greenlet

def func1():
    print("111111111")
    grl2.switch()
    print("222222222")
    grl2.switch()

def func2():
    print("3333")
    grl1.switch()
    print(4444444)

def func3():
    print("切换到func3")


if __name__ == '__main__':
    grl1 = greenlet(func1)
    grl2 = greenlet(func2)

    grl1.switch()