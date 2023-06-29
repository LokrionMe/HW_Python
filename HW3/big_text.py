from string import punctuation
b_text = "Python also includes a data type for sets. A set is an unordered collection with"\
    " no duplicate elements. Basic uses include membership testing and eliminating duplicate"\
    " entries. Set objects also support mathematical operations like union, intersection,"\
    " difference, and symmetric difference.\n"\
    "Curly braces or the set() function can be used to create sets. Note: to create an empty"\
    "set you have to use set(), not {}; the latter creates an empty dictionary, a data "\
    "structure that we discuss in the next section."
list_punct = []
for i in range(len(punctuation)):
    list_punct.append(punctuation[i])
for i in list_punct:
    b_text = b_text.replace(i, '')
list_words = b_text.lower().split()
set_words = set(list_words)
outter_lib: dict[str, int] = {}
maximum = 0
k = 10
len_max_word = 0
len_max_numb = 0
for item in set_words:
    count_word = list_words.count(item)
    outter_lib[item] = count_word
    if count_word > maximum:
        maximum = count_word
    if len(item) > len_max_word:
        len_max_word = len(item)
    if len(str(count_word)) > len_max_numb:
        len_max_numb = len(str(count_word))
point = 1
while k > 0:
    for key, val in outter_lib.items():
        if val == maximum:
            count_space = len_max_word + len_max_numb + 3 - \
                len(str(point)) - len(key)
            print(f"{point}. {key}{val:>{count_space}}")
            k -= 1
            point += 1
        if k == 0:
            break
    maximum -= 1
