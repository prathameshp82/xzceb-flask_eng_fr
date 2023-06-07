from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation.translator import englishToFrench, frenchToEnglish
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def translateEnglishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = frenchToEnglish(textToTranslate)
    return translatedText


@app.route("/frenchToEnglish")
def translateFrenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = englishToFrench(textToTranslate)
    return translatedText

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
