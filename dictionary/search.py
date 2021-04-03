from dictionary.searchbase import SearchBase
import requests
from bs4 import BeautifulSoup
from random import choice
from string import ascii_letters, digits
import re
import json
import time
import datetime
from django.utils.text import slugify
import pprint

from dictionary import helper
import random

import threading

from dictionary.models import Vocabulary
import os
from django.core.mail import send_mail
import logging
import inspect
import concurrent
import local_config
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

   
    print('cvocaaaa: ',type(vocabulary))
    word_slug = slugify(vocabulary)
    # proxy_data = "145.40.78.181:3128"
    proxy_parse = {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}"
    }
    search = SearchBase(word_slug, proxy_parse)
    search.searchBaseVocabulary()
    # search.get_word_explains()
    data_search = search.get_search_data()

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data_search)

    word = data_search.get('word_cover')
    name = word.get('name')
    word_type = word.get('type')
    phon_us = word.get('pronunciation_us')
    phon_uk = word.get('pronunciation_uk')
    sound_us = word.get('sound_us')
    sound_uk = word.get('sound_uk')
    definitions_examples = data_search.get('word_explaning')

    if sound_us and sound_uk:
        # print('sound_us: ', sound_us)
        file_name_us = f'{name}_{word_type}__us.mp3'
        file_name_uk = f'{name}_{word_type}__uk.mp3'
      
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(helper.downloadFileFromUrl,proxy,sound_us,file_name_us)
            executor.submit(helper.downloadFileFromUrl,proxy,sound_uk,file_name_uk)
        

        vocabulary = Vocabulary()
        vocabulary.name = name
        vocabulary.word_type = word_type
        vocabulary.phon_us = phon_us
        vocabulary.phon_uk = phon_uk
        vocabulary.sound_us = 'audio/'+file_name_us
        vocabulary.sound_uk = 'audio/'+file_name_uk
        vocabulary.definitions = definitions_examples
        vocabulary.certification_field = ''
        vocabulary.save()
        print(f"Saved <{vocabulary}> successfully.")
        message = f"Saved <{vocabulary}> successfully."

        helper.log_message(message)

        search.get_nearby_word_links()

    # print('sound_us: ',sound_us)
    # print('sound_uk: ',sound_uk)


def check_search(word):

    count = 1
    # send_mail('search vocabulary', 'search start', 'thuan20202000@gmail.com',
    #           ['thuan20132000@gmail.com'], fail_silently=False)

    while True:
        try:
            print(f"Searching {word}")

            if(count >= 10):
                helper.generate_proxy()
                print("Generated New Proxy")
                count = 1
                continue

            proxy = helper.choose_random(local_config.PATH_WORK_DIR+"/proxy_data.txt")

            if proxy:
                print(f"Searching {word} turn {count} with proxy: {proxy} ")
                searchVocabulary(word, proxy)
                return False
            else:
                return False
                
        except Exception as e:
            print(f"Search error {count} : {e}")
            message = f"error: {e}"
            helper.log_message(e)
            count += 1
            continue


def read_vocabulary_to_search(file):
    try:
        start = time.time()
        # Using readlines()
        file1 = open(file, 'r')
        Lines = file1.readlines()
        count = 0
        # Strips the newline character

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

            for line in Lines:
                count += 1
                print(f"=====>Searching for {line.strip()} ")
                message = f"Searching vocabulary <<{line.strip()}>>"
                helper.log_message(message)
                executor.submit(check_search,line.strip())
        end = time.time()

        message = f"=====> Finished Search {count} vocabulary in {end-start} <====="
        helper.log_message(message)
        print(message)
        # send_mail('search vocabulary', message, 'thuan20202000@gmail.com',
        #           ['thuan20132000@gmail.com'], fail_silently=False)
    except Exception as e:
        func = inspect.currentframe().f_back.f_code

        error = f"error: {e} at "+func.co_name + " - " + func.co_filename
        helper.log_message(error)



file = local_config.PATH_WORK_DIR+"/dictionary_data/read_vocabulary.txt"
read_vocabulary_to_search(file)