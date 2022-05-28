# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import re

def read_file_content(filename):
    with open(filename, "r") as f:
        text = f.read()
    return text.strip()


def count_words():
    text = re.findall("[a-zA-Z]+", read_file_content("./story.txt"))
    result = {i.rstrip(): 0 for i in text}
    for i in text:
        result[i] += 1
    return result
