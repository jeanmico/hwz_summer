import os
import sys

#fpath = os.path.join(os.path.sep, 'wittelab', 'data1', 'jcostello')
fpath = os.path.join(os.path.sep, 'Users', 'student', 'GitHub', 'hwz_summer')
fname = 'c34.csv'
diagnosis = fname.split('.')[0].upper()

head = {}  # dictionary key: column name, value: column index
with open(os.path.join(fpath, fname), 'r') as f:
    # read only the first line to obtain the header values
    head_line = f.readline().strip().split(' ')
for i, col in enumerate(head_line):
    head[col] = i

# columns of interest
cols =  []
icd_cols = set()
col_fname = 'columns.txt'
with open(os.path.join(fpath, col_fname), 'r') as f:
    for line in f:
        vals = line.strip().split(',')
        cols.append(vals[0])
        if vals[1].strip() =='yes':
            icd_cols.add(head[vals[0].strip()])

# indices of interest
indices = []
for col in cols:
    indices.append(head[col])
indices.sort()

icd_indices = list(icd_cols)
icd_indices.sort()

#score_fpath = os.path.join(os.path.sep, 'wittelab', 'data1', 'chenan', 'ukbiobank', 'ad_mr', 'scores', 'score_files', 'SLE_gwascat_score')
score_fpath = fpath
score_fname = 'SLE_gwascat_prs'
#score_fname = 'mini_patients'

patients = {}
with open(os.path.join(fpath, fname), 'r') as f:

    # verify the diagnosis is of interest
    # record results in dictionary: {eid:[columns of interest]}
    for line in f:
        vals = line.strip().split()
        a = [vals[i] for i in icd_indices]
        for i in range(len(a)):
            if diagnosis == a[i][0:3]:
                patients[vals[0]] = [vals[i] for i in indices]

print(len(patients))

with open(os.path.join(score_fpath, score_fname)) as f:
    # question: in what population should we normalize scores? should we normalize scores?
    # if normalized in entire population, it should be done prior to this code
    # what is our control population?
    for line in f:
        vals = line.strip().split()
        if vals[0] in patients:
            patients[vals[0]].append(vals[2])

out_fpath = fpath
out_fname = 'c34_summary.csv'

# sort columns (do this earlier, this is really dumb)
tmp = {}
for key, val in head.items():
    if val in indices:
        tmp[val] = key

sorted_header = []
for x in indices:
    sorted_header.append(tmp[x])
sorted_header.append('prs_calc')

with open(os.path.join(out_fpath, out_fname), 'w+') as out:
    # write out the headers...
    out.write(','.join(str(i) for i in sorted_header))
    out.write('\n')
    # write out the patient data
    out.write('\n'.join(','.join(str(i) for i in subject) for subject in patients.values()))
