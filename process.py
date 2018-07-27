import os
import sys

fpath = os.path.join(os.path.sep, 'wittelab', 'data1', 'jcostello')
fname = 'c34.csv'

head = {}
with open(os.path.join(fpath, fname), 'r') as f:
    head_line = f.readline().strip().split(',')
for i, col in enumerate(head_line):
    head[col] = i


# columns of interest
cols = set()
col_fname = columns.txt
with open(os.path.join(fpath, col_fname), 'r') as f:
    lines = f.readlines()
    for line in lines:
        cols.add(line.strip())

print(cols)


