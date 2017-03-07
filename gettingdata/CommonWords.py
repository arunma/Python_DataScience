import sys
from collections import Counter

try:
    num_words=int(sys.argv[1])
except:
    num_words=5

counter=Counter(word.lower()
                for line in sys.stdin
                for word in line.strip().split()
                if word) #skip empty words

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")