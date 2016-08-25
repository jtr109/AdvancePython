import string


def decode_sc(secret_code, movement=2):
    chars = string.ascii_lowercase
    decode_chars = chars[movement:] + chars[:movement]
    table = str.maketrans(chars, decode_chars)

    reality_string = secret_code.translate(table)
    return reality_string

if __name__ == '__main__':
    secret_code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    true_string = decode_sc(secret_code)
    print(true_string)

