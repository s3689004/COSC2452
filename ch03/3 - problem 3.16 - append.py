def split_line(text):
    words = text.split()
    for current_word in words:
        print(current_word)

my_list = [] # make empty list
for current_word in words:
    my_list.append(current_word.lower())