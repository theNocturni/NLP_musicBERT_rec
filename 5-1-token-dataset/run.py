from functions import get_token_dataset
import sys

def main(dirs):
    for name in dirs:
        get_token_dataset(name)
    
if __name__ == '__main__':
    dirs = [dir[1:-1] for dir in sys.argv[1][1:len(sys.argv[1])-1].split(',')]
    main(dirs)