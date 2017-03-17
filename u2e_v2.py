# Urdu to English

import requests
import json

# credentials from the OxfordDictionaries site: https://developer.oxforddictionaries.com/admin/account

app_id = '92618303'
app_key = 'c8e511a71ad1f2a8344a7ccab292df14'
api_base_url = 'https://od-api.oxforddictionaries.com/api/v1/entries/'

source_language = 'ur'
target_language = 'en'

# Take an Urdu word as an input

print ('This app will ask you for an Urdu word and show you the following things:\n')
print ('- the corresponding words in English\n')
print ('- how to pronounce the English words\n')
print ('- synonyms and related words for the English words\n')
print ('- example sentences that use the English words\n\n')
word_id = input('Enter an Urdu word (in nastalikh script): ')
print ('\n')
print ('\n','===============================================','\n')

# Get the translation for the word
# GET /entries/{source_lang}/{word_id}/translations={target_lang}

url = api_base_url + source_language + '/' + word_id.lower() + '/translations=' + target_language
r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

#print("code {}\n".format(r.status_code))
#print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))

try:
    json_data = json.loads(json.dumps(r.json()))
    list_of_trans =[]
    print ('English words for', word_id, ':', '\n')
    target_word_id = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    for item in target_word_id:
        for item2 in item['translations']:
            print ('- - -', item2['text'], '\n')
            list_of_trans.append(item2['text'])
#print ([list_of_trans])
except:
    print ('The dictionary does not have a translation for', word_id, 'yet.', '\n')

# See how to pronounce the word
# GET /entries/{source_lang}/{word_id}/pronunciation

print ('\n','===============================================','\n')
for entry in list_of_trans:
    try:
        url = api_base_url + target_language + '/' + entry.lower()
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        #print("code {}\n".format(r.status_code))
        #print("text \n" + r.text)
        #print("json \n" + json.dumps(r.json()))
        json_data = json.loads(json.dumps(r.json()))
        target_word_sound = json_data['results'][0]['lexicalEntries'][0]['pronunciations'][0]['audioFile']
        print ('This is how you pronounce', entry.upper(), ":", target_word_sound)
    except:
        print ('The corpus does not have a pronunciation guide for', entry.upper(), 'yet.','\n')

# Get the synonyms for the translated word
# GET /entries/{source_lang}/{word_id}/synonyms

print ('\n','===============================================','\n')
for entry in list_of_trans:
    try:
        url = api_base_url + target_language + '/' + entry.lower() + '/synonyms;antonyms'
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        #print("code {}\n".format(r.status_code))
        #print("text \n" + r.text)
        #print("json \n" + json.dumps(r.json()))
        json_data = json.loads(json.dumps(r.json()))
        target_word_syn = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
        print ('Here are some synonyms for', entry.upper(), '\n')
        for item in target_word_syn:
            for item2 in item['synonyms']:
                print ('- - -', item2['text'], '\n')
        print ('Here are some related words for', entry.upper(), '\n')
        for item in target_word_syn:
            for item2 in item['subsenses']:
                for item3 in item2['synonyms']:
                    print ('- - -', item3['text'], '\n')
    except:
        print('The corpus does not have synonyms and related words for', entry.upper(), 'yet.','\n')

# Get the sentences for the translated word
# GET /entries/{source_language}/{word_id}/sentences

print ('\n','===============================================','\n')
for entry in list_of_trans:
    try:
        url = api_base_url + target_language + '/' + entry.lower() + '/sentences'
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        #print("code {}\n".format(r.status_code))
        #print("text \n" + r.text)
        #print("json \n" + json.dumps(r.json()))
        json_data = json.loads(json.dumps(r.json()))
        target_word_sentences = json_data['results'][0]['lexicalEntries']
        print ('Here are some example sentences with', entry.upper(), '\n')
        for item in target_word_sentences:
            for item2 in item['sentences']:
                print ('- - -', item2['text'], '\n')
    except:
        print ('The corpus does not have any example sentences for', entry.upper(), 'yet.', '\n')
