# ~466k English words
# Credits: https://github.com/dwyl/english-words

import itertools
import json
import sys

fp = open("words.json")
words = json.load(fp)
fp.close()


def find(asc=True):
    lst = input("Type the characters, space separated:\n").split()
    pos = set()
    for permutation in itertools.permutations(lst):
        s = ""
        for i in range(len(permutation)):
            s += permutation[i]
            if s in words:  # O(1) amortized
                pos.add(s)
    ret = list(pos)
    ret.sort(key=lambda x: len(x), reverse=not asc)
    return ret


if __name__ == "__main__":
    while True:
        try:
            words = find()
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)

        print("-------------")
        for word in words:
            print(word)
        print("-------------")
