import random
import threading
import queue
from queue import PriorityQueue


class Task:
    def __init__(self, priority):
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f'Task(priority={self.priority}).      sleep({random.random()})'


class Producer(threading.Thread):
    def __init__(self, q: queue.PriorityQueue):
        super().__init__()
        self.queue = q
        print("Producer: Running")

    def run(self):
        for i in range(10):
            priority = random.randint(0, 6)
            t = Task(priority)
            self.queue.put((priority, t))

        consumer = Consumer(self.queue)
        consumer.start()
        consumer.join()
        print('Producer: Done')


class Consumer(threading.Thread):
    def __init__(self, q: queue.PriorityQueue):
        super().__init__()
        self.queue = q
        self.tasks_done = 0
        print('Consumer: Running')

    def run(self):
        while True:
            try:
                priority, task = self.queue.get(block=False)
            except:
                if q.empty():
                    continue

            print(f'>running {task}')
            self.queue.task_done()
            self.tasks_done += 1
            if self.tasks_done == 10:
                print('Consumer: Done')
                break


if __name__ == '__main__':
    q = PriorityQueue()
    t_producer = Producer(q)
    t_producer.start()
    q.join()
    t_producer.join()
