#!/usr/bin/env python
import sys

prev_show = "  "
abc_found = False

viewers_total = 0

line_cnt = 0  # count input lines

for line in sys.stdin:
    line = line.strip()  # strip out carriage return
    key_value = line.split('\t')  # split line, into key and value, returns a list
    line_cnt += 1

    curr_show = key_value[0]
    value_in = key_value[1]

    if curr_show != prev_show:

        if line_cnt > 1 and abc_found:
            print('{0} {1}'.format(prev_show, viewers_total))

        # now reset lists
        viewers_total = 0
        abc_found = False
        prev_show = curr_show

    if value_in[0:3] == 'ABC':
        abc_found = True
    else:
        viewers_total += int(value_in)  # if the value field was just the total count then its
        # the first (and only) item in this list
# for last row
print('{0} {1}'.format(curr_show, viewers_total))
