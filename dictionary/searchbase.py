import urllib.request
from bs4 import BeautifulSoup
import re
import json
import time
from django.utils.text import slugify
import requests
# from models import Word_Definition
from dictionary.SearchNearBy import SearchNearBy
# from VocabularyController import VocabularyController
from dictionary.models import Vocabulary
# from dictionary.helper import dowloadFileFromUrl

from random import choice

import threading
from dictionary import helper
import os
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


class SearchBase:
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

    def save_vocabulary(self, name, word_type, phon_us, phon_uk, sound_us, sound_uk, definitions_examples):
        if sound_us and sound_uk:
            # print('sound_us: ', sound_us)
            file_name_us = f'{name}_{word_type}__us.mp3'
            file_name_uk = f'{name}_{word_type}__uk.mp3'
            # # helper.downloadFileFromUrl(proxy, sound_us, file_name)
            # thread1 = myThread(
            #     1, f"Thread-{file_name_us}", helper.downloadFileFromUrl(None, sound_us, file_name_us))

            # # print('sound_uk: ', sound_uk)
            # # helper.downloadFileFromUrl(proxy, sound_uk, file_name)
            # thread2 = myThread(
            #     2, f"Thread-{file_name_uk}", helper.downloadFileFromUrl(None, sound_us, file_name_uk))

            # thread1.start()
            # thread2.start()
            # thread1.join()
            # thread2.join()
            # print("Exiting Main Thread")

            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                executor.submit(helper.downloadFileFromUrl,None,sound_us,file_name_us)
                executor.submit(helper.downloadFileFromUrl,None,sound_uk,file_name_uk)

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

            message = f"Saved nearby <{vocabulary}> successfully."
            print(message)
            helper.log_message(message)

    def get_nearby_word_links(self,):
        # accordion ui-grad
        listLink = []

        links = self.soup.find('div', 'responsive_row nearby').find(
            'ul').find_all('li')

        for link in links:

            a = link.select_one('li a')
            try:

                url = link.a.get('href')
                wordOrigin = url.split('/')[-1]
                wordToFind = re.sub(r'_\d', '', wordOrigin)

                a = SearchNearBy(url, wordToFind)
                a.searchVocabulary()
                dataSearch = a.get_data_search()

                nearby_word_cover = dataSearch.get('word_cover')
                nearby_word_definitions = dataSearch.get('word_explaning')
                nearby_word_type = nearby_word_cover.get('type')
                if nearby_word_type == self.word_cover.get('type'):
                    continue

                # print('Nearby word cover: ', dataSearch)
                # print('Nearby word type: ', dataSearch.get(
                #     'word_cover').get('type'))
                # print('=========')

                # print(f'word_cover_type: ', self.word_cover.get('type'))
                name = nearby_word_cover.get('name')
                word_type = nearby_word_cover.get('type')
                phon_us = nearby_word_cover.get('pronunciation_us')
                phon_uk = nearby_word_cover.get('pronunciation_uk')
                sound_us = nearby_word_cover.get('sound_us')
                sound_uk = nearby_word_cover.get('sound_uk')

                self.save_vocabulary(name, word_type, phon_us, phon_uk, sound_us, sound_uk, nearby_word_definitions)

                message = f"save vocabulary <<{name}>> type:<<{word_type}>> successfully"
                helper.log_message(message)
                # wordtype = dataSearch['word_definition']['type']
                # wordname = dataSearch['word_definition']['name']

                # check = self.check_word_local_with_type(wordname, wordtype)
                # if check == False:
                #     wordDefinition = dataSearch['word_definition']
                #     wordExplaination = dataSearch['word_explaination']
                # v = VocabularyController(wordDefinition, wordExplaination)
                # newword = v.save_word_definition()
                # v.save_word_cover_json(json.dumps(dataSearch), newword.id)

            except Exception as e:
                print('-------->error search nearby!!{}'.format(link.a.get('href')))
                print('error: ',e)
                message = f"error search nearby: {e}"
                helper.log_message(message)

    # def get_data(self):
    #     data_response = {}
    #     data_response['word_definition'] = self.word_cover
    #     data_response['word_explaination'] = self.word_explains

    #     return data_response

    # def check_word_local_with_type(self, word, kind):
    #     check_word = Word_Definition.query.filter_by(name={word}).first()

    #     if check_word is None:
    #         return False
    #     elif check_word.type != kind:
    #         return False
    #     else:
    #         return False
