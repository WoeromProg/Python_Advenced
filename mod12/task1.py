import logging
import time
import threading
import requests
import sqlite3
from multiprocessing.pool import ThreadPool, Pool
import multiprocessing

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

information = []
URL = "https://swapi.dev/api/people/"
sql_information_on_dict = """
    INSERT INTO arguments (name, birth_year, gender) VALUES (?,?,?)
"""


def get_image(url: str, i: int):
    global information
    response = requests.get(url + str(i))
    if response.status_code == 200:
        dict_information = dict(response.json())
        print(dict_information['name'], dict_information['birth_year'], dict_information['gender'])
        if dict_information is not None:
            information.append((dict_information["name"], dict_information["birth_year"], dict_information["gender"]))


def load_images_with_ThreadPool():
    with ThreadPool(processes=multiprocessing.cpu_count() * 5) as pool:
        #global information
        start = time.time()
        threads = []
        for i in range(1, 22):
            get_image(URL, i)
        pool.map(get_image, threads)
        logger.info('Done in {:4}'.format(time.time() - start))


def load_images_with_pool():
    with Pool(processes=multiprocessing.cpu_count() * 5) as pool:
        #global information
        start = time.time()
        threads = []
        for i in range(1, 22):
            threads.append((URL, i))
        pool.starmap(get_image, threads)
        logger.info('Done {:4}'.format(time.time() - start))


if __name__ == '__main__':
    with sqlite3.connect('homework.sqlite') as conn:
        cursor = conn.cursor()
        load_images_with_ThreadPool()
        load_images_with_pool()
