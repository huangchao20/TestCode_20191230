import queue
import threading
import contextlib
import time

StopEvent = object()


class ThreadPool(object):

    def __init__(self, max_num):
        self.q = queue.Queue()
        self.max_num = max_num

        self.terminal = False
        self.generate_list = []
        self.free_list = []

    def run(self, func, args, callback=None):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行失败或成功后执行的回调函数，回调函数有两个参数1、任务函数执行状态；2、任务函数返回值（默认为None，即：不执行回调函数）
        :return: 如果线程池已经终止，则返回True否则None
        """

        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()
        w = (func, args, callback,)
        self.q.put(w)

    def generate_thread(self):
        """
        创建一个线程
        """
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        """
        循环去获取任务函数并执行任务函数
        """
        current_thread = threading.currentThread
        self.generate_list.append(current_thread)

        event = self.q.get()  # 获取线程
        while event != StopEvent:   # 判断获取的线程数不等于全局变量

            func, arguments, callback = event   # 拆分元祖，获得执行函数，参数，回调函数
            try:
                result = func(*arguments)   # 执行函数
                status = True
            except Exception as e:    # 函数执行失败
                status = False
                result = e

            if callback is not None:
                try:
                    callback(status, result)
                except Exception as e:
                    pass

            # self.free_list.append(current_thread)
            # event = self.q.get()
            # self.free_list.remove(current_thread)
            with self.work_state():
                event = self.q.get()
        else:
            self.generate_list.remove(current_thread)

    def close(self):
        """
        关闭线程，给传输全局非元祖的变量来进行关闭
        :return:
        """
        for i in range(len(self.generate_list)):
            self.q.put(StopEvent)

    def terminate(self):
        """
        突然关闭线程
        :return:
        """
        self.terminal = True
        while self.generate_list:
            self.q.put(StopEvent)
        self.q.empty()

    @contextlib.contextmanager
    def work_state(self):
        self.free_list.append(threading.currentThread)
        try:
            yield
        finally:
            self.free_list.remove(threading.currentThread)




def work(i):
    print(i)
    return i +1 # 返回给回调函数

def callback(ret):
    print(ret)

pool = ThreadPool(10)
for item in range(50):
    pool.run(func=work, args=(item,),callback=callback)

pool.terminate()
# pool.close()