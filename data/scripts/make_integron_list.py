import sys

fi = sys.argv[1]

data = {}
for i in open(fi):
    key, _class = i.strip().split('\t')
    data[key] = [key, _class]

for i in data.values():
    print("\t".join(i))
