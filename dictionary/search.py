from dictionary.searchbase import SearchBase
import requests

from bs4 import BeautifulSoup
from random import choice
from string import ascii_letters, digits
import re
import json
import time
from django.utils.text import slugify
import pprint

from dictionary import helper
import random

import threading

from dictionary.models import Vocabulary

class myThread (threading.Thread):
    def __init__(self, threadID, name, func):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.func = func

    def run(self):
        print("Starting " + self.name)
        self.func


def searchVocabulary(vocabulary, proxy):
    word_slug = slugify(vocabulary)
    # proxy_data = "145.40.78.181:3128"
    proxy_parse = {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}"
    }
    search = SearchBase(word_slug, proxy_parse)
    search.searchVocabulary()
    # search.get_word_explains()
    data_search = search.get_search_data()

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data_search)



    word = data_search.get('word_cover')
    name = word.get('name')
    phon_us = word.get('pronunciation_us')
    phon_uk = word.get('pronunciation_uk')
    sound_us = word.get('sound_us')
    sound_uk = word.get('sound_uk')
    definitions_examples = data_search.get('word_explaning')

    if sound_us and sound_uk:
        # print('sound_us: ', sound_us)
        file_name_us = f'{name}+us.mp3'
        file_name_uk = f'{name}+uk.mp3'
        # helper.downloadFileFromUrl(proxy, sound_us, file_name)
        thread1 = myThread(
            1, f"Thread-{file_name_us}", helper.downloadFileFromUrl(proxy, sound_us, file_name_us))

        # print('sound_uk: ', sound_uk)
        # helper.downloadFileFromUrl(proxy, sound_uk, file_name)
        thread2 = myThread(
            2, f"Thread-{file_name_uk}", helper.downloadFileFromUrl(proxy, sound_us, file_name_uk))

        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        print("Exiting Main Thread")

        vocabulary = Vocabulary()
        vocabulary.name = name
        vocabulary.phon_us = phon_us
        vocabulary.phon_uk = phon_uk
        vocabulary.sound_us = file_name_uk
        vocabulary.sound_uk = file_name_us
        vocabulary.definitions = definitions_examples
        vocabulary.certification_field = 'ielts'
        vocabulary.save()
        print(f"Saved <{vocabulary}> successfully.")
        

    # print('sound_us: ',sound_us)
    # print('sound_uk: ',sound_uk)


def check_search(word):

    count = 1

    while True:
        try:
            print(f"Searching {word}")

            if(count >= 10):
                helper.generate_proxy()
                print("Generated New Proxy")
                count = 1
                continue

            proxy = helper.choose_random("dictionary/proxy_data.txt")
            print(f"Searching {word} turn {count} with proxy: {proxy} ")

            searchVocabulary(word, proxy)
            return False

        except Exception as e:
            print(f"Search error {count} : {e}")
            count += 1
            if count >=15:
                break
            continue


# check_search('irregular')


def read_vocabulary_to_search(file):

    start = time.time()
    # Using readlines()
    file1 = open(file, 'r')
    Lines = file1.readlines()
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        print(f"=====>Searching for {line.strip()} ")
        check_search(line.strip())
    end  = time.time()

    print(f"Search {count} vocabulary in {end-start} ")

    


read_vocabulary_to_search('dictionary/vocabulary_data/test_vocabulary.txt')
