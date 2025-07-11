sentence = input("Enter a sentence: ").lower()
words = sentence.split()
word_count = {}
for word in words:
    word = word.strip(",.!?\"“”‘’")
 
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print("Word count:")
for word, count in word_count.items():
    print(f"{word}: {count}")
