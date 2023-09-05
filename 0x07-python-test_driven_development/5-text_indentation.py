#!/usr/bin/python3
"""Task: 4. Text indentation"""


def text_indentation(text):
    """function that prints a text with 2 new lines after ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text_list = text.split(' ')
    new_text_list = [element for element in new_text_list if element != '']
    new_text = ' '.join(new_text_list)
    new_text = (new_text
                .replace('. ', '.').replace('.', '.\n\n')
                .replace('? ', '?').replace('?', '?\n\n')
                .replace(': ', ':').replace(':', ':\n\n')
                )

    print(new_text, end='')
