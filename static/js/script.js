function translateText() {
    const inputText = document.getElementById('inputText').value.trim();
    const sourceLang = document.getElementById('sourceLang').value;
    const targetLang = document.getElementById('targetLang').value;

    if (!inputText) {
        alert("Please enter text to translate.");
        return;
    }

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: inputText,
            source_lang: sourceLang,
            target_lang: targetLang
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('outputText').innerText = data.translated_text;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
