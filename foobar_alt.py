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
            
@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@

from threading import Lock, Semaphore, Barrier

class FooBar:
    def __init__(self, n):
        self.n = n
        self.barrier = Barrier(2)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.barrier.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.barrier.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            
            
@zero even odd ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@

from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zLock = Semaphore(1)
        self.oLock = Semaphore(0)
        self.eLock = Semaphore(0)
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zLock.acquire()
            printNumber(0)
            if (i % 2):
                self.eLock.release()
            else:
                self.oLock.release()
            #(self.eLock if i % 2 else self.oLock).release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.eLock.acquire()
            printNumber(i)
            self.zLock.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.oLock.acquire()
            printNumber(i)
            self.zLock.release()
        

            
                
