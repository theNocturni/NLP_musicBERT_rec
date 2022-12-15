from functions import construct_phrase
import sys

def main(dirs):
    for name in dirs:
        construct_phrase(name)

if __name__ == '__main__':
    dirs = [dir[1:-1] for dir in sys.argv[1][1:len(sys.argv[1])-1].split(',')]
    main(dirs)