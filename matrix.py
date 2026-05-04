#nano mapper.py
#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    matrix, i, j, value = line.split(",")
    i, j, value = int(i), int(j), int(value)

    if matrix == "A":
        for k in range(2):
            print "%d,%d\tA,%d,%d" % (i, k, j, value)
    else:
	for k in range(2):
            print "%d,%d\tB,%d,%d" % (k, j, i, value)

#nano reducer.py
#!/usr/bin/env python
import sys

current_key = None
values = []

def compute(key, values):
    A = {}
    B = {}

    for val in values:
        matrix, k, v = val.split(",")
        k = int(k)
        v = int(v)

        if matrix == "A":
            A[k] = v
        else:
            B[k] = v
    result = 0
    for k in A:
        if k in B:
            result += A[k] * B[k]

    print "%s\t%d" % (key, result)
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    key, value = line.split("\t")

    if current_key == key:
        values.append(value)
    else:
	if current_key:
            compute(current_key, values)
        current_key = key
        values = [value]

if current_key:
    compute(current_key, values)

#chmod +x mapper.py reducer.py
#hdfs dfs -mkdir /matrix
#hdfs dfs -put matrix.txt /matrix
#hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
# -file mapper.py \
# -file reducer.py \
# -mapper mapper.py \
# -reducer reducer.py \
# -input /matrix \
# -output /matrix_out
# cat matrix.txt | python mapper.py | sort | python reducer.py