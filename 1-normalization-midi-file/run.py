from functions import normalization_midi_file
import sys
def main(dirs):
    normalization_midi_file(dirs)

if __name__ == '__main__':
    dirs = [dir[1:-1] for dir in sys.argv[1][1:len(sys.argv[1])-1].split(',')]
    main(dirs)