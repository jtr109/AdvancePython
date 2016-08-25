import os, sys


def get_tree(inpath):
    for dirpath, dirnames, filenames in os.walk(inpath):
        for d in dirnames:
            print(dirpath + d)
        for f in filenames:
            print(dirpath + f)

if __name__ == '__main__':
    narg = len(sys.argv)
    if not narg == 2:
        print("usage: %s path" % \
              os.path.basename(sys.argv[0]))
    else:
        get_tree(sys.argv[1])
