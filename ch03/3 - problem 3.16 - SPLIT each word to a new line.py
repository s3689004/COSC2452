# Split each word on to a new line
def split_line(text):
    words = text.split()
    for current_word in words:
        print(current_word)