word = input('Enter your word(Buffalo): ')
index = word.find('a') + 1
last = len(word) - index

print(word[:index])
print(word[index:])