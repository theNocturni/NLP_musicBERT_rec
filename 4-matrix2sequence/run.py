from functions import matrix_to_sequence
import sys

def main(dirs):
    for name in dirs:
        matrix_to_sequence(name)

if __name__ == '__main__':
    dirs = [dir[1:-1] for dir in sys.argv[1][1:len(sys.argv[1])-1].split(',')]
    main(dirs)