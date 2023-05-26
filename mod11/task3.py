import logging
import random
import threading
import time

TOTAL_TICKETS = 10
TICKETS_MAX = 100

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super(Director, self).__init__()
        self.lock = semaphore
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS, TICKETS_MAX
        while TICKETS_MAX:
            if TOTAL_TICKETS <= 4:
                with self.lock:
                    tickets_to_print = 10 - (TOTAL_TICKETS % 10)
                    if tickets_to_print > TICKETS_MAX:
                        tickets_to_print = TICKETS_MAX
                    TOTAL_TICKETS += tickets_to_print
                    TICKETS_MAX -= tickets_to_print
                    logger.info(f'Director put {tickets_to_print} tickets')
        logger.info(f'Director printed tickets, stop work')


class Seller(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS, TICKETS_MAX
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TICKETS_MAX <= 0:
                    break
                self.tickets_sold += 1
                TICKETS_MAX -= 1
                logger.info(f'{self.name} sold one;  {TICKETS_MAX} left')
        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


def main():
    semaphore = threading.Semaphore()


    director = Director(semaphore)
    director.start()
    sellers = [director]

    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()


if __name__ == '__main__':
    main()