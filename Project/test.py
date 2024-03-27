from translate import Translator
translator = Translator(provider = "mymemory", from_lang = "en", to_lang = "es")
translation = translator.translate("Hello")
print(translation)