import math
import sys
from threading import Semaphore, Thread

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.even_n = math.floor(n/2)
        self.odd_n = math.ceil(n/2)
        self.even_counter = 2
        self.odd_counter = 1
        self.lock_z = Semaphore(1)
        self.lock_e = Semaphore(0)
        self.lock_o = Semaphore(0)
        self.state = "odd"
        
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(0, self.n):
            self.lock_z.acquire()
            printNumber(0)
            if self.state == "odd":
                self.lock_o.release()
            if self.state == "even":
                self.lock_e.release()
   
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(0, self.even_n):
            self.lock_e.acquire()
            printNumber(self.even_counter)
            self.lock_z.release()
            self.state = "odd"
            self.even_counter += 2
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(0, self.odd_n):
            self.lock_o.acquire()
            printNumber(self.odd_counter)
            self.lock_z.release()
            self.state = "even"
            self.odd_counter += 2

def printNumber(num: int):
    print(str(num))
        
if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    solution = ZeroEvenOdd(n)

    threadA = Thread(target=solution.zero, args=(printNumber, ))
    threadB = Thread(target=solution.even, args=(printNumber, ))
    threadC = Thread(target=solution.odd, args=(printNumber, ))

    threadA.start()
    threadB.start()
    threadC.start()   
    
    threadA.join()
    threadB.join()
    threadC.join()