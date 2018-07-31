import os
import sys

fpath = os.path.join(os.path.sep, 'wittelab', 'data1', 'jcostello')
fname = 'c34.csv'
diagnosis = fname.split('.')[0]

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

patients = {}
with open(os.path.join(fpath, fname), 'r') as f:

    # verify the diagnosis is of interest
    # record results in dictionary: {eid:[columns of interest]}
    for line in f:
        vals = line.strip().split(',')
        if diagnosis in [vals[i] for i in icd_cols]:
            patients[vals[0]] = [vals[i] for i in indices]

with open(os.path.join(score_fpath, score_fname)) as f:
    # question: in what population should we normalize scores? should we normalize scores?
    # if normalized in entire population, it should be done prior to this code
    # what is our control population?
    for line in f:
        vals = line.strip().split('\t')
        if vals[0] in patients:
            patients[vals[0]].append(vals[2])

out_fpath = fpath
out_fname = 'c34_summary.csv'

with open(os.path.join(out_fpath, out_fname), 'w+') as out:
    #write out the headers...
    out.write('\n'.join(','.join(str(i) for i in subject) for subject in patients.values()))
