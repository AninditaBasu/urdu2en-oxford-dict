from flask import Flask
from flask import request
from flask import render_template
import requests
import json
import os

app = Flask(__name__)

@app.route('/')
def word_get():
    return render_template("word_enter.html")

@app.route('/', methods=['POST'])
def word_process():
    # credentials from the OxfordDictionaries site: https://developer.oxforddictionaries.com/admin/account
    app_id = '92618303'#:) please don't misuse these creds
    app_key = 'c8e511a71ad1f2a8344a7ccab292df14'#:) please don't misuse these creds
    api_base_url = 'https://od-api.oxforddictionaries.com/api/v1/entries/'

    source_language = 'ur'
    target_language = 'en'

    word_id = request.form['urduword']

    try:
        # Get the translation for the word
        # GET /entries/{source_lang}/{word_id}/translations={target_lang}
        url = api_base_url + source_language + '/' + word_id.lower() + '/translations=' + target_language
        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        try:
            json_data = json.loads(json.dumps(r.json()))
            list_of_trans = []
            target_word_id = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
            for item in target_word_id:
                for item2 in item['translations']:
                    #print('- - -', item2['text'], '\n')
                    list_of_trans.append(item2['text'])
        except:
            list_of_trans = ['The dictionary does not have a translation for this word yet.']

        # See how to pronounce the word
        # GET /entries/{source_lang}/{word_id}/pronunciation
        list_of_sounds = []
        try:
            for entry in list_of_trans:
                url = api_base_url + target_language + '/' + entry.lower()
                r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
                # print("code {}\n".format(r.status_code))
                # print("text \n" + r.text)
                # print("json \n" + json.dumps(r.json()))
                json_data = json.loads(json.dumps(r.json()))
                target_word_sound = json_data['results'][0]['lexicalEntries'][0]['pronunciations'][0]['audioFile']
                #print('This is how you pronounce', entry.upper(), ":", target_word_sound)
                list_of_sounds.append(target_word_sound)
        except:
            list_of_sounds = ['The corpus does not have a pronunciation guide for these words yet.']

        # Get the synonyms for the translated word
        # GET /entries/{source_lang}/{word_id}/synonyms
        list_of_synonyms = []
        list_of_related_words = []
        try:
            url = api_base_url + target_language + '/' + entry.lower() + '/synonyms;antonyms'
            r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
            #print("code {}\n".format(r.status_code))
            #print("text \n" + r.text)
            #print("json \n" + json.dumps(r.json()))
            json_data = json.loads(json.dumps(r.json()))
            target_word_syn = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
            #print('Here are some synonyms for', entry.upper(), '\n')
            for item in target_word_syn:
                for item2 in item['synonyms']:
                    #print('- - -', item2['text'], '\n')
                    list_of_synonyms.append(item2['text'])
            #print('Here are some related words for', entry.upper(), '\n')
            for item in target_word_syn:
                for item2 in item['subsenses']:
                    for item3 in item2['synonyms']:
                        #print('- - -', item3['text'], '\n')
                        list_of_related_words.append(item3['text'])
        except:
            list_of_synonyms = ['The corpus does not have any synonyms for this word yet.']
            list_of_related_words = ['The corpus does not have any related words for this word yet.']

        return render_template('word_out.html', transwords=list_of_trans, word_id=word_id, transounds = list_of_sounds, transyns = list_of_synonyms, transrels = list_of_related_words)
    except:
        return 'Error'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
