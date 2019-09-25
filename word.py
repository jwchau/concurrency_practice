from threading import Barrier, Lock, Event, Semaphore, Condition


class Foo(object):
    def __init__(self):
        #self.barriers = (Barrier(2), Barrier(2))
        #self.locks = (Lock(), Lock())
        #self.locks[0].acquire()
        #self.locks[1].acquire()
        #self.done = (Event(), Event())
        self.gates = (Semaphore(0), Semaphore(0))


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        # printThird() outputs "third". Do not change or remove this line.
        printThird()