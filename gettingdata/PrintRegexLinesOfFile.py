import sys,re

file_name=sys.argv[1]
with open (file_name, 'r') as f:
    for line in f:
        if re.match("^#", line):
            print(line)

#python PrintRegexLinesOfFile.py RegexMatch.py