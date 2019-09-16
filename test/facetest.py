import time
import threading

def maxnum( list ):
    print( sorted(list))
    return( sorted(list))

def countnum():
    toutal_num = 0
    for i in range(1,10000):
        s = list(str(i)).count("3")
        toutal_num += s
    return toutal_num

def sayxiaojian( tnum ):
    print( "第[%s]个线程正在运行" %tnum )
    time.sleep(3)

def synchronized(func):

    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return lock_func


class Singleton(object):
    """
    单例模式
    """
    instance = None

    @synchronized
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance

if __name__ == "__main__":
    # t = countnum()
    # print(t)
    t1 = threading.Thread( target = sayxiaojian, args = (11,))
    t2 = threading.Thread(target = sayxiaojian, args = (22,))
    t1.run()
    t2.run()
    print(t1.getName())
    print(t2.getName())
    # t1.join()
    # t2.join()