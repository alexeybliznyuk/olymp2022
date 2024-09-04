prompt = input()

word_list = []
word_list = prompt.split(" : ")
short_list = []
long_list = []
w_list = []

# print(123)
for i in range(len(word_list)):
    if len(word_list[i]) < 4:
        word = word_list[i]
        # word = word.replace(word_list[i][0], word_list[i][0].lower())
        word = word.lower()
        short_list.append(word)
        
    if len(word_list[i]) > 7:
        word = word_list[i]
        # word = word.replace(word_list[i][0], word_list[i][0].lower())
        # word = word.lower()
        long_list.append(word)

    if "w" in word_list[i]:
        word = word_list[i]
        word = word.replace(word_list[i][0], word_list[i][0].upper())
        w_list.append(word)

short_out = "Short: " + "; ".join(sorted(short_list))
print(short_out)

long_out = "Long: " + "; ".join(sorted(long_list, reverse=True))
print(long_out)

w_out = "With letter: " + "; ".join(w_list)
print(w_out)
