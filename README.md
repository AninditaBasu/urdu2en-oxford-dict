__The code in this repo is no longer being maintained. For newer stuff, see [Mercury](https://github.com/AninditaBasu/mercury), which uses v2.3 of the Oxford Dictionaries API.__

__The version of the API used in this code (Oxford Dictionaries API v1) reached sunset on 30 June 2019. Therefore, this code hasn't worked after the API v1 sunset.__

![version 1.0](https://img.shields.io/badge/version-1.0-green.svg)  ![python 3.4.3](https://img.shields.io/badge/python-3.4.3-blue.svg)  ![license: CC 4.0](https://img.shields.io/badge/license-CC%204.0-lightgrey.svg)  

# urdu2en-oxford-dict

This is an Urdu-to-English learning app that uses the [Oxford Dictionaries APIs](https://developer.oxforddictionaries.com/documentation) to show you word translations, their pronunciations, and synonyms and related words.

This app is an entry for the [Oxford Dictionaries API Contest](https://developer.oxforddictionaries.com/2017-competition). Here's a demo:
[![urdu2englishAppDemo](https://raw.github.com/AninditaBasu/urdu2en-oxford-dict/master/app_screenshot.PNG)](https://youtu.be/RgcfrWC4Vww)

## System requirements

- Python 3.4.3 with the following packages: Flask, requests, json
- A web browser
- A media player
 
 ## Input requirements
 
 - An API ID and key of an Oxford Dictionaries account. See [getting your API ID and key](https://developer.oxforddictionaries.com/documentation/getting_started).
 - A keyboard than can handle Nastalikh. If you do not have such a keyboard, use an online resource to copy-paste words in Nastalikh when the app prompts you to.
 
 ## How to use
 
 1.  Download and extract the contents of this repo to a local drive.
 2.  Open the `urdu2english_oxfordDictAPI.py` file in a text editor, and edit lines 16 and 17 to specify your API credentials.
 2.  Save the `urdu2english_oxfordDictAPI.py` file and run it.
 3.  Follow the on-screen instructions.
