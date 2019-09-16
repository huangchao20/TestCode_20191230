from multiprocessing import Process, Manager

def f( d, l ):
    d["list"] = [123,"333sss"]
    d["name"] = "name"
    d["0"] = "men"
    l.reverse()

if __name__ == '__main__':
    # with Manager() as manager:
    #     d = manager.dict()
    #     data = manager.list(range(10))
    #     p = Process(target=f, args=(d, data,))
    #     p.start()
    #     p.join()
    #
    #     print(d)
    #     print("*" * 20)
    #     print(data)
    manager = Manager()
    d = manager.dict()
    data = manager.list(range(10))
    p = Process(target=f, args=(d, data,))
    p.start()
    p.join()
    print(d)
    print("*" * 20)
    print(data)

