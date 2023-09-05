#!/usr/bin/python3

def text_indentation(text):
    """prints a text with 2 new lines
    after each of these characters: ., ? and :.
    text must be a string or a TypeError will be
    raised.
    There shouldn't be spaces at the start or end of a line."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == '':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == '':
                i += 1
            continue
        i += 1
