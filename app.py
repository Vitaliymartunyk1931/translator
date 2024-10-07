from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Простий словник для перекладу
translations = {
    "en": {
        "Hello": "Привіт",
        "Goodbye": "До побачення",
        "Thank you": "Дякую",
        "How are you?": "Як справи?",
        "What is your name?": "Як тебе звати?",
        "I love programming.": "Я люблю програмування.",
    },
    "uk": {
        "Привіт": "Hello",
        "До побачення": "Goodbye",
        "Дякую": "Thank you",
        "Як справи?": "How are you?",
        "Як тебе звати?": "What is your name?",
        "Я люблю програмування.": "I love programming.",
    },
    "es": {
        "Hola": "Привіт",
        "Adiós": "До побачення",
        "Gracias": "Дякую",
        "¿Cómo estás?": "Як справи?",
        "¿Cuál es tu nombre?": "Як тебе звати?",
        "Me encanta programar.": "Я люблю програмування.",
    },
    "fr": {
        "Bonjour": "Привіт",
        "Au revoir": "До побачення",
        "Merci": "Дякую",
        "Comment ça va?": "Як справи?",
        "Quel est ton nom?": "Як тебе звати?",
        "J'aime programmer.": "Я люблю програмування.",
    }
}

# Зберігає перекладені фрази у файл
def save_translation(original, translated):
    with open('translations.txt', 'a', encoding='utf-8') as f:
        f.write(f"{original} -> {translated}\n")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data['text']
    source_lang = data['source_lang']
    target_lang = data['target_lang']

    # Переклад тексту
    translated_text = translations.get(source_lang, {}).get(text, "Translation not found.")

    # Зберігаємо перекладену фразу у файл
    save_translation(text, translated_text)

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    if not os.path.exists('translations.txt'):
        open('translations.txt', 'w', encoding='utf-8').close()  # Створюємо файл, якщо його ще немає
    app.run(debug=True)
