from collections import Counter
import re

# Считываем текст из файла
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()

# Разбиваем текст на слова (с помощью регулярки, чтобы убрать знаки препинания)
words = re.findall(r'\b\w+\b', text)

# Считаем частоту каждого слова
counter = Counter(words)

# Находим слово с максимальной частотой
most_common_word, freq = counter.most_common(1)[0]

result = f"Самое частое слово: '{most_common_word}' встречается {freq} раз(а)."

# Записываем результат в output.txt
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print(result)