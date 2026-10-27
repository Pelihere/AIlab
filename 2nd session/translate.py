words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "hello": "سلام",
    "book": "کتاب",
    "computer": "رایانه",
    "student": "دانشجو",
    "school": "مدرسه"
}

sentence = "I love python and AI"

translated_words = []
translated_count = 0
untranslated_count = 0

for word in sentence.lower().split():
    if word in words:
        translated_words.append(words[word])
        translated_count += 1
    else:
        translated_words.append(f"[{word}]")
        untranslated_count += 1

print(" ".join(translated_words))
print("Translated words:", translated_count)
print("Untranslated words:", untranslated_count)