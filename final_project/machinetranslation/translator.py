import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def instantiate_translator():
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version="2018-05-01",
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    return language_translator

def english_to_french(language_translator, english_text):
    if english_text is not None:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()      
        return french_text
    else:
        return "Please include a sentence to translate."


def french_to_english(language_translator, french_text):
    if french_text is not None:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        return english_text
    else:
        return "Please include a sentence to translate."


if __name__ == '__main__':
    tr = instantiate_translator()
    print(apikey)
    print(english_to_french(tr, None))
    print(french_to_english(tr, "Bonjour")['translations'][0]['translation'])
