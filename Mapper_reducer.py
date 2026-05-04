#mapper.py
#!/usr/bin/env python
import sys

target_word = "big"
for line in sys.stdin:
        words = line.strip().split()
        for word in words:
                if word.lower() == target_word:
                        print "%s\t1" % target_word

#reducer.py
#!/usr/bin/env python
import sys
current,count=None,0
for line in sys.stdin:
        word,value=line.strip().split("\t")
        value = int(value)
        if word == current:
                count+=value
        else:
             	if current:
                        print(current,count)
                current,count = word,value
if current:
	print(current,count)

cmds:
nano mapper.py
nano reducer.py
chmod +x mapper.py reducer.py
echo "data science is growing big data is powerful data analysis is important" > sample.txt
hdfs dfs -mkdir /input_py
hdfs dfs -put sample.txt /input_py
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-mapper mapper.py \
-reducer reducer.py \
-input /input_py \
-output /output_py
cat sample.txt | python mapper.py | sort | python reducer.py
hdfs dfsadmin -safemode get
hdfs dfsadmin -safemode leave