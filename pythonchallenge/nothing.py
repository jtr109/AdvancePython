import urllib.request
import re


def get_final_url(base_url, nothing):
    url = base_url + str(nothing)
    pattern = r'.+ (\d+)$'
    count = 0
    while True:
        count += 1
        print('Connecting url %3d:' % count + url)
        msg = urllib.request.urlopen(url).read().decode('utf-8')
        try:
            nothing = re.match(pattern, msg).group(1)
        except AttributeError:
            break
        url = base_url + str(nothing)
    return url

if __name__ == '__main__':
    base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    final_url = get_final_url(base_url, 12345)
    print('final url is' + final_url)

