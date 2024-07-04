from googletrans import Translator
import re 


def translate_article(data):
    Titulo, Articulo, Url = data.values()
    translator = Translator()
    translated_data = {}
    url_pattern = re.compile(r'http[s]?://')

    # Iterar sobre los elementos del diccionario original y traducir los valores
    for key, value in data.items():
        if isinstance(value, str) and not url_pattern.match(value):  # Asegurarse de que el valor sea una cadena de texto y no una URL
            try:
                translated = translator.translate(value, src='en', dest='es')
                translated_data[key] = translated.text
            except Exception as e:
                print(f"Error translating {key}: {e}")
                translated_data[key] = value  # Mantener el valor original en caso de error
        else:
            translated_data[key] = value  # Mantener los valores que no son cadenas o son URLs

    return translated_data