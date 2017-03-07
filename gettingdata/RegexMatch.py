import sys, re

regex=sys.argv[1]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)
    else:
        sys.stdout.write("not a match")

# cat input.txt | python RegexMatch.py "[0-9]"