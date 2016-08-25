def get_num(text):
    new_list = list(filter(lambda x: x.isdigit(), text))
    new_text = ''.join(new_list)
    return new_text

if __name__ == '__main__':
    text = "aAsmr3idd4bgs7Dlsf9eAF"
    print(get_num(text))
