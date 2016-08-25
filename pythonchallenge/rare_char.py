import string


def get_rare(text):
    rare_list = list(filter(lambda c: c in string.ascii_letters, text))
    ret = ''.join(rare_list)
    return ret

if __name__ == '__main__':
    text = open('orc.txt').read()
    rare = get_rare(text)
    print (rare)
