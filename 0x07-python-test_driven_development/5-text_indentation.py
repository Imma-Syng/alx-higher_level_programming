#!/usr/bin/python3
""" Defines a text indentation function """

def text_indentation(text):
    """
     A function that prints a text with 2 
     new lines after . ? and :

    Args:
        text(str): The text to be printed

    Raises:
        TypeError: text must be a string

    Returns:
        a text with 2 new lines after each character
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    t = 0
    while t < len(text) and text[t] == ' ':
        t += 1

    while t < len(text):
        print(text[t], end="")
        if text[t] == "\n" or text[t] in ".?:":
            if text[t] in ".?:":
                print("\n")
            t += 1
            while t < len(text) and text[t] == ' ':
                t += 1
                continue
            t += 1
