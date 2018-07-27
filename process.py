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
icd_cols = set()
col_fname = columns.txt
with open(os.path.join(fpath, col_fname), 'r') as f:
    for line in f:
        vals = line.strip().split('\t')
        cols.add(vals[0])
        if vals[1] =='yes'
            icd_cols.add(vals[0])
print(cols)
print(icd_cols)

# indices of interest
indices = []
for col in cols:
    indices.append(head[col])
indices.sort()

score_fpath = os.path.join(os.path.sep, 'wittelab', 'data1', 'chenan', 'ukbiobank', 'ad_mr', 'scores', 'score_files', 'SLE_gwascat_score')
score_fname = 'SLE_gwascat_prs'

with open(os.path.join(fpath, fname), 'r') as f:
    
