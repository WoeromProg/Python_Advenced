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
        super().__init__()
        self.sem = semaphore
        self.max_tickets = TICKETS_MAX
        self.tickets_added = 0
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS
        global TICKETS_MAX
        is_running = True
        while is_running:
            if TOTAL_TICKETS == 4:
                with self.sem:
                    tickets_to_print = min(TICKETS_MAX, 10 - TOTAL_TICKETS)
                    TOTAL_TICKETS += tickets_to_print
                    TICKETS_MAX -= tickets_to_print
                    self.tickets_added += tickets_to_print
                    logger.info(f'Director added {tickets_to_print} tickets; {TICKETS_MAX} left')
                    if TICKETS_MAX == 0:
                        is_running = False
        logger.info(f'Director printed {self.tickets_added} tickets')


class Seller(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        global TICKETS_MAX
        is_running = True
        while is_running:
            self.random_sleep()
            if TICKETS_MAX != 0 and TOTAL_TICKETS <= 4:
                continue
            else:
                if TOTAL_TICKETS == 0:
                    break
                with self.sem:
                    self.tickets_sold += 1
                    TOTAL_TICKETS -= 1
                    logger.info(f'{self.name} sold one;  {TOTAL_TICKETS} left')
                    logger.info(f'{self.name} MAX_TICKETS = {TICKETS_MAX}')
        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


def main():
    semaphore = threading.Semaphore()
    workers = []

    director = Director(semaphore)
    director.start()

    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        workers.append(seller)

    workers.append(director)

    for worker in workers:
        worker.join()


if __name__ == '__main__':
    main()