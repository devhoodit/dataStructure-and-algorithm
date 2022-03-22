tmp = []

with open('ds.py','r') as f:
    for line in f.readlines():
        tmp.append(line.replace('\t', '    '))

with open('ds.py', 'w') as f:
    f.writelines(tmp)