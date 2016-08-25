import re


def get_letters(text):
    text_list = text.split('\n')
    new_text = ''.join(text_list)

    pattern = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
    letters_list = re.findall(pattern, new_text)
    return ''.join(letters_list)

if __name__ == '__main__':
    text = open('equality.txt').read()
    print(get_letters(text))



