from functions import collect_chords, merge_chords, get_chord_index
# collect chord
import sys

def main(dirs):
    for name in dirs:
        collect_chords(name)

    # get chord dict and counts
    merge_chords()

    # get chord index
    get_chord_index()

if __name__ == '__main__':
    dirs = [dir[1:-1] for dir in sys.argv[1][1:len(sys.argv[1])-1].split(',')]
    main(dirs)