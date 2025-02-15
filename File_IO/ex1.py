from translate import Translator

translator = Translator(to_lang="ja")

with open("S13/text.txt") as text:
    tt = text.read()

    translation = translator.translate(tt)
    print(translation)
