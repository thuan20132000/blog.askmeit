
import urllib.request
from bs4 import BeautifulSoup
import re
import json
import time
from django.utils.text import slugify
import requests

from random import choice

import pprint
import threading
from flashcard.models import VocabularyCard
from flashcard import helper
import logging
import inspect
from django.core.mail import send_mail



from flashcard.config import ConfigPath

import local_config

file_path = ConfigPath.PATH_WORK_DIR

import concurrent

class myThread (threading.Thread):
    def __init__(self, threadID, name, func):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.func = func

    def run(self):
        print("Starting " + self.name)
        self.func


class SearchVocabularyBase:
    word_cover = {}
    word_explains = []
    vocabularySearch = ''
    initialVocabularySearch = ''
    soup = ''
    searchResult = False

    def __init__(self, vocabularySearch, proxy):
        self.word_cover = {}
        self.word_explains = []
        self.vocabularySearch = vocabularySearch
        self.initialVocabularySearch = vocabularySearch
        self.proxy = proxy

        url = f'https://www.oxfordlearnersdictionaries.com/definition/english/{vocabularySearch}'

        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"}

        source = requests.get(url, headers=headers, timeout=7, proxies=proxy)
        # print('user agent: ', source.headers)

        self.soup = BeautifulSoup(source.content, 'html5lib')

    def searchBaseVocabulary(self,):
        # vocabulary = self.vocabularySearch
        # print('--->vocabulary search : ')

        # source = requests.get('https://www.oxfordlearnersdictionaries.com/definition/english/')

        # print(source)
        # print('---->url search : ', source)
        vocabulary = self.vocabularySearch

        try:
            word_name = self.soup.select_one(
                "h1", id=re.compile(vocabulary+'_h_(.)'))
            word_pronounciation_br = self.soup.find("div", id=re.compile(
                vocabulary+'_topg_(.)')).find('div', 'phons_br').find('span', 'phon')
            word_pronounciation_am = self.soup.find("div", id=re.compile(
                vocabulary+'_topg_(.)')).find('div', 'phons_n_am').find('span', 'phon')
            word_type = self.soup.find("div", id=re.compile(
                vocabulary+'_topg_(.)')).find('span', 'pos')
            word_sound_uk = self.soup.find(
                "div", "sound audio_play_button pron-uk icon-audio")['data-src-mp3']
            word_sound_us = self.soup.find(
                "div", "sound audio_play_button pron-us icon-audio")['data-src-mp3']

            self.word_cover['name'] = self.initialVocabularySearch
            self.word_cover['pronunciation_uk'] = word_pronounciation_br.text
            self.word_cover['pronunciation_us'] = word_pronounciation_am.text
            self.word_cover['type'] = word_type.text
            self.word_cover['sound_uk'] = word_sound_uk
            self.word_cover['sound_us'] = word_sound_us

            self.get_word_explains(vocabulary)
            self.searchResult = True
            return {"debug": 'true'}

        except:
            print('error in vocabulary firstly')

        try:
            vocabulary_underscore = vocabulary.replace('-', '_')

            word_name = self.soup.select_one(
                "h1", id=re.compile(vocabulary_underscore+'_h_(.)'))
            word_pronounciation_br = self.soup.find("div", id=re.compile(
                vocabulary_underscore+'_topg_(.)')).find('div', 'phons_br').find('span', 'phon')
            word_pronounciation_am = self.soup.find("div", id=re.compile(
                vocabulary_underscore+'_topg_(.)')).find('div', 'phons_n_am').find('span', 'phon')

            word_type = self.soup.find("div", id=re.compile(
                vocabulary_underscore+'_topg_(.)')).find('span', 'pos')
            word_sound_uk = self.soup.find(
                "div", "sound audio_play_button pron-uk icon-audio")['data-src-mp3']
            word_sound_us = self.soup.find(
                "div", "sound audio_play_button pron-us icon-audio")['data-src-mp3']

            self.word_cover['name'] = self.initialVocabularySearch
            self.word_cover['pronunciation_uk'] = word_pronounciation_br.text
            self.word_cover['pronunciation_us'] = word_pronounciation_am.text
            self.word_cover['type'] = word_type.text
            self.word_cover['sound_uk'] = word_sound_uk
            self.word_cover['sound_us'] = word_sound_us

            self.get_word_explains(vocabulary_underscore)
            self.searchResult = True

            return {"debug": 'true'}

        except:
            print('error in secondary vocabulary_underscore')

        try:
            vocabulary_nospace = vocabulary.replace('-', '')

            word_name = self.soup.select_one(
                "h1", id=re.compile(vocabulary_nospace+'_h_(.)'))
            word_pronounciation_br = self.soup.find("div", id=re.compile(
                vocabulary_nospace+'_topg_(.)')).find('div', 'phons_br').find('span', 'phon')
            word_pronounciation_am = self.soup.find("div", id=re.compile(
                vocabulary_nospace+'_topg_(.)')).find('div', 'phons_n_am').find('span', 'phon')
            word_type = self.soup.find("div", id=re.compile(
                vocabulary_nospace+'_topg_(.)')).find('span', 'pos')
            word_sound_uk = self.soup.find(
                "div", "sound audio_play_button pron-uk icon-audio")['data-src-mp3']
            word_sound_us = self.soup.find(
                "div", "sound audio_play_button pron-us icon-audio")['data-src-mp3']

            self.word_cover['name'] = self.initialVocabularySearch
            self.word_cover['pronunciation_uk'] = word_pronounciation_br.text
            self.word_cover['pronunciation_us'] = word_pronounciation_am.text
            self.word_cover['type'] = word_type.text
            self.word_cover['sound_uk'] = word_sound_uk
            self.word_cover['sound_us'] = word_sound_us

            self.get_word_explains(vocabulary_nospace)
            self.searchResult = True
            return {"debug": 'true'}
        except:
            print("error in third vocabulary_underscore")

        try:
            # return {'debug':'not found word but exist in dictionary'}
            if(self.searchResult is False):
                newVocabularySearch = self.vocabularySearch
                self.vocabularySearch = newVocabularySearch+'1'
                self.searchResult = True
                self.searchVocabulary()

        except:
            print("error in fourth try to recursion")

    def get_search_data(self,):

        return {
            "word_cover": self.word_cover,
            "word_explaning": self.word_explains
        }

    def get_word_explains(self, vocabulary):

        # create list word explains
        vocabulary_nospace = vocabulary.replace('-', '')

        vocabulary_final = vocabulary_nospace.replace('_', '')

        print('vocabulary final: ', vocabulary_final)
        # get all element cover by vocabulary
        try:
            word_explain_covers = self.soup.select_one('.senses_multiple').find_all(
                "li", id=re.compile(vocabulary_final+'(.?)_sng_(.)'))
        except:
            word_explain_covers = self.soup.select_one('.sense_single').find_all(
                "li", id=re.compile(vocabulary_final+'(.?)_sng_(.)'))

            # loop to get one by one definitions by vocabulary

        c = 0
        for w in word_explain_covers:
            # print("================")
            # print(str(c)+": "+w.find('span','def').text)
            explain_name = w.find('span', 'def').text
            c += 1
            explain = {}
            explain['id'] = c
            explain['title'] = explain_name
            # create a list to save all examples of definition
            word_examples = []

            # get element cover examples of definition
            examples = w.select('ul.examples li span.x')

            # loop to get one by one example of definition
            for e in examples:
                word_examples.append(e.text)

                # save word examples list into word explains dictionary
                explain['example'] = word_examples

            # Add expolain after get full of information
            self.word_explains.append(explain)


def searchVocabulary(vocabulary, proxy,topic_id):

    word_slug = slugify(vocabulary)
    # proxy_data = "145.40.78.181:3128"
    proxy_parse = {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}"
    }
    search = SearchVocabularyBase(word_slug, proxy_parse)
    search.searchBaseVocabulary()
    # search.get_word_explains()
    data_search = search.get_search_data()

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(data_search)

    word = data_search.get('word_cover')
    name = word.get('name')
    word_type = word.get('type')
    phon_us = word.get('pronunciation_us')
    phon_uk = word.get('pronunciation_uk')
    sound_us = word.get('sound_us')
    sound_uk = word.get('sound_uk')
    definitions_examples = data_search.get('word_explaning')
    definition = definitions_examples[0]['title']
    example = definitions_examples[0]['example'][0]

    if sound_us and sound_uk:
        # print('sound_us: ', sound_us)
        file_name_us = f'{name}+{word_type}+us.mp3'
        file_name_uk = f'{name}+{word_type}+uk.mp3'
        # helper.downloadFileFromUrl(proxy, sound_us, file_name)
   
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(helper.downloadFileFromUrl,proxy,sound_us,file_name_us)
            executor.submit(helper.downloadFileFromUrl,proxy,sound_uk,file_name_uk)

        vocabulary = VocabularyCard()
        vocabulary.name = name
        vocabulary.word_type = word_type
        vocabulary.phon_us = phon_us
        vocabulary.phon_uk = phon_uk
        vocabulary.sound_us = '/audio/'+file_name_us
        vocabulary.sound_uk = '/audio/'+file_name_uk
        vocabulary.definition = definition
        vocabulary.example = example
        vocabulary.save()            
        vocabulary.topics.add(topic_id)

        print(f"Saved <{vocabulary}> successfully.")
        message = f"Saved <{vocabulary}> successfully."

        helper.log_message(message)


def check_search(word,topic):

    count = 1
    # send_mail('search vocabulary', 'search start', 'thuan20202000@gmail.com',
    #           ['thuan20132000@gmail.com'], fail_silently=False)
    cancel_count = 1
    while True:
        try:
            if cancel_count >= 28:
                helper.log_message("Break search <<%s>>" % word)
                break
            print(f"Searching {word}")

            if(count >= 10):
                helper.generate_proxy()
                print("Generated New Proxy")
                count = 1
                continue

            proxy = helper.choose_random(local_config.PATH_WORK_DIR+"/proxy_data.txt")

            if proxy:
                print(f"Searching {word} turn {count} with proxy: {proxy} ")
                searchVocabulary(word, proxy,topic)
                return False
            else:
                return False

        except Exception as e:
            print(f"Search error {count} : {e}")
            message = f"error: {e}"
            helper.log_message(e)
            count += 1
            cancel_count += 1

            continue


# check_search('bureaucracy',1)




def read_vocabulary_to_search(file,topic_id):
    try:
        start = time.time()
        # Using readlines()
        file1 = open(file, 'r')
        Lines = file1.readlines()
        count = 0
        # Strips the newline character

        with concurrent.futures.ThreadPoolExecutor(max_workers= 5) as executor:
            for line in Lines:
                count += 1
                print(f"=====>Searching for {line.strip()} ")
                message = f"Searching vocabulary <<{line.strip()}>>"
                helper.log_message(message)
                executor.submit(check_search,line.strip(),topic_id)
        end = time.time()

        message = f"Search {count} vocabulary in {end-start} "
        print("message: ",message)
        # send_mail('FlashCard:  search vocabulary', message, 'thuan20202000@gmail.com',
        #           ['thuan20132000@gmail.com'], fail_silently=False)
    except Exception as e:
        func = inspect.currentframe().f_back.f_code
        error = f"error: {e} at "+func.co_name + " - " + func.co_filename
        helper.log_message(error)



file = local_config.PATH_WORK_DIR+"/flashcard_data/sport.txt"


read_vocabulary_to_search(file,3)