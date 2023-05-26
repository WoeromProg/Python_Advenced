import logging
import threading
import random
import time
from threading import Lock


logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)
lock = Lock()
class Philosopher(threading.Thread):
    def __init__(self, left_fork: threading.Lock, right_fork: threading.Lock):
        super().__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork
    def run(self):
        while self.running:
            logger.info(f'Pholosopher {self.getName()} start thinking')
            time.sleep(random.randint(1, 5))
            logger.info(f'Philosop {self.getName()} is hungry')
            # self.left_fork.acquire()
            with self.left_fork:
                logger.info(f'Pholosopher {self.getName()} acquired left fork')
                with self.right_fork:
                    logger.info(f'Philosopher {self.getName()} acquired right fork')
                    self.dining()

            # if self.right_fork.locked():
            #     continue
            # try:
            #     self.right_fork.acquire()
            #     logger.info(f'Pholosopher {self.getName()} acquired right fork')
            #     self.dining()
            # finally:
            #     self.left_fork.release()
            #     self.right_fork.release()
    def dining(self):
        logger.info(f'Pholosopher {self.getName()} starts eating')
        time.sleep(random.randint(1, 5))
        logger.info(f'Pholosopher {self.getName()} finishes eating and leaves to think.')

def main():
    forks = [threading.Lock() for n in range(5)]
    philosophers = [
        Philosopher(forks[1 % 5], forks[(i + 1) % 5])
        for i in range(5)
    ]

    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(180)
    Philosopher.running = False
    logger.info("Now we're finishing.")

if __name__ == '__main__':
    main()