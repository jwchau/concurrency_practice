from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.div3 = Semaphore(0)
        self.div5 = Semaphore(0)
        self.div35 = Semaphore(1)
        self.numb = Semaphore(0)
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1, 1):
            self.div3.acquire()
            if (i % 3 == 0 and i % 5 != 0):
                printFizz()
            self.numb.release()


    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n +1, 1):
            self.div5.acquire()
            if (i % 5 == 0 and i % 3 != 0):
                printBuzz()
            self.numb.release()
            
            
    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n +1, 1):
            self.div35.acquire()
            if (i % 3 == 0 and i % 5 == 0):
                printFizzBuzz()
            self.div3.release()
            self.div5.release()

            
    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 1):
            self.numb.acquire()
            self.numb.acquire()
            if (i % 3 != 0 and i % 5 != 0):
                printNumber(i)
            self.div35.release()
 
