from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    tr = translator.instantiate_translator()
    french_text = translator.english_to_french(tr, textToTranslate)

    return "Translated text to French: " + french_text["translations"][0]["translation"]

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    tr = translator.instantiate_translator()
    english_text = translator.french_to_english(tr, textToTranslate)

    return "Translated text to English: " + english_text["translations"][0]["translation"]

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
