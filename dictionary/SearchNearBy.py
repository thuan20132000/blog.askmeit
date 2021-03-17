import requests
from bs4 import BeautifulSoup
import re
import json
import slugify


class SearchNearBy:
    word_cover = {}
    word_explains = []
    nearby_words_list = []
    wordToFind = ''

    def __init__(self, linkToSearch, wordToFind):
        self.word_cover = {}
        self.word_explains = []
        self.wordToFind = wordToFind
        # url = 'https://www.oxfordlearnersdictionaries.com/definition/english/{}'.format(wordToSearch)
        url = linkToSearch

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

        source = requests.get(linkToSearch, headers=headers)

        self.soup = BeautifulSoup(source.content, 'html5lib')

    def searchVocabulary(self,):
        vocabulary = self.wordToFind
        try:
            word = self.soup.select_one(
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

            self.word_cover['name'] = word.text
            self.word_cover['pronunciation_uk'] = word_pronounciation_br.text
            self.word_cover['pronunciation_us'] = word_pronounciation_am.text
            self.word_cover['type'] = word_type.text
            self.word_cover['sound_uk'] = word_sound_uk
            self.word_cover['sound_us'] = word_sound_us

            self.get_word_explains(vocabulary)
            # print('success in find element vocabulary:{} '.format(vocabulary))
            # print(self.word_cover)
            return

        except:
            print('error in vocabulary')

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

            self.word_cover['name'] = word.text
            self.word_cover['pronunciation_uk'] = word_pronounciation_br.text
            self.word_cover['pronunciation_us'] = word_pronounciation_am.text
            self.word_cover['type'] = word_type.text
            self.word_cover['sound_uk'] = word_sound_uk
            self.word_cover['sound_us'] = word_sound_us

            self.get_word_explains(vocabulary_underscore)
            # print('success in find element vocabulary underscore:{} '.format(
            #     vocabulary_underscore))
            # print('data: '+self.word_cover)

            return

        except:
            print('error in vocabulary_underscore')

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

            self.word_cover['name'] = word.text
            self.word_cover['pronunciation_uk'] = word_pronounciation_br.text
            self.word_cover['pronunciation_us'] = word_pronounciation_am.text
            self.word_cover['type'] = word_type.text
            self.word_cover['sound_uk'] = word_sound_uk
            self.word_cover['sound_us'] = word_sound_us

            self.get_word_explains(vocabulary_nospace)
            # print('success in find element vocabulary nospace:  {}'.format(
            #     vocabulary_nospace))
            # print('data: '+self.word_cover)
            return
        except:
            print("error in vocabulary nospace")

    def get_word_explains(self, vocabulary):

        # print('get word explains...'+vocabulary)

        # create list word explains
        vocabulary_nospace = vocabulary.replace('-', '')
        vocabulary_final = vocabulary_nospace.replace('_', '')

        # print(vocabulary_final)
        # get all element cover by vocabulary
        try:
            word_explain_covers = self.soup.select_one('.senses_multiple').find_all(
                "li", id=re.compile(vocabulary_final+'_sng_(.)'))
            # print("senses multiple")
        except:
            word_explain_covers = self.soup.select_one('.sense_single').find_all(
                "li", id=re.compile(vocabulary_final+'_sng_(.)'))
            # print('sense single')

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
            self.word_explains.append(explain)

    def get_data_search(self,):
        # data_response = {}
        # data_response['word_definition'] = self.word_cover
        # data_response['word_explaination'] = self.word_explains
        # print('-->get data: {}'.format(data_response))
        # return data_response
        return {
            "word_cover ": self.word_cover,
            "word_explaning": self.word_explains
        }
