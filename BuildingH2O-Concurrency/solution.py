import time
from threading import Semaphore, Thread

class H2O:
    def __init__(self):
        self.lock_o = Semaphore(1)
        self.lock_h = Semaphore(2)
        self.o_count = 0
        self.h_count = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.lock_h.acquire()
        releaseHydrogen()
        self.h_count += 1
        if self.o_count > 0:
            ratio = self.h_count / self.o_count
            if ratio <= 2:
                self.lock_h.release()
            elif ratio >= 2:
                self.lock_o.release()
                
    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.lock_o.acquire()
        releaseOxygen()
        self.o_count += 1
        ratio = self.h_count / self.o_count
        if ratio <= 2:
            self.lock_h.release()

def rh():
    print("H")

def ro():
    print("O")

if __name__ == "__main__":
    h2o = H2O()
    inp_strain = "HHHHHHOOO"
    print("input strain: ", inp_strain)
    func_map = {"H": (h2o.hydrogen, rh), "O": (h2o.oxygen, ro)}
    for inp in inp_strain:
        t = Thread(target=func_map[inp][0], args=(func_map[inp][1], ))
        t.start()
        time.sleep(.25)