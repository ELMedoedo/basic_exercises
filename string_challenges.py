# Вывести последнюю букву в слове
word = "Архангельск"
print(word[-1])


# Вывести количество букв "а" в слове
word = "Архангельск"
print(word.lower().count("а"))

# Вывести количество гласных букв в слове
word = "Архангельск"
schet, vowels = 0, "уеыаоэяию"
for i in range(len(word)):
    if word[i].lower() in vowels:
        schet += 1
print(schet)


# Вывести количество слов в предложении
sentence = "Мы приехали в гости"
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = "Мы приехали в гости"
spis = sentence.split()
for i in range(len(spis)):
    print(spis[i][0])


# Вывести усреднённую длину слова в предложении
sentence = "Мы приехали в гости"
spis, all_letters = sentence.split(), 0
for i in range(len(spis)):
    all_letters += len(spis[i])
print(all_letters // len(spis))