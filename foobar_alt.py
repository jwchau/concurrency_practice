from threading import Event

class FooBar:
    def __init__(self, n):
        self.n = n
        #self.fooE = Event()
        #self.fooE.set()
        #self.barE = Event()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            #self.fooE.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            #self.fooE.clear()
            #self.barE.set()
            

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            #self.barE.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            #self.barE.clear()
            #self.fooE.set()


@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@

from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = Lock()
        self.barLock = Lock()
        self.barLock.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.fooLock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.barLock.release()
                

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.barLock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.fooLock.release()
            