# -*- coding: utf-8 -*-

import string
uppercase = string.ascii_uppercase


def valid_substr(s):
    for u in uppercase:
        if s.count(u) >= 4:
            return False
        sublist = s.split(u)
        sublist.pop(0)
        while len(sublist) > 1:
            other_chars = ''.join(sublist[1:])
            for c in sublist[0]:
                if c in other_chars:
                    return False  # 'xyxy' mode exist
            sublist.pop(0)
    return True


def no_continuous(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return False
    return True


def likes_or_not(s):
    if no_continuous(s) is False:
        return 'Dislikes'
    if valid_substr(s) is False:
        return 'Dislikes'
    return 'Likes'

if __name__ == '__main__':
    l = ['ABBA', 'THETXH', 'ABACADA', 'A', 'BA', 'ABCBA']
    for s in l:
        print('XiaoYi %s %s' % (likes_or_not(s), s))
