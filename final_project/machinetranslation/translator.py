#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(APIKEY)
translator = LanguageTranslatorV3(
    version='2022-03-14',
    authenticator=AUTHENTICATOR
)

translator.set_service_url(URL)

def english_to_french(english_text):
    french_text = translator.translate(text=english_text, model_id='en-fr').get_result()['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    english_text = translator.translate(text=french_text, model_id='fr-en').get_result()['translations'][0]['translation']
    return english_text
