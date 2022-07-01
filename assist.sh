#!/bin/bash
rm status-file.txt
touch status-file.txt
txt1="There are no Unreachable nodes"
num_lines=$(bash -c "cat text | grep -A 1 Unreachable_nodes: | wc -l")
if [[ $num_lines -eq 0 ]]
then
	echo $txt1 >> status-file.txt
else
	echo "The following node(s) are down: " >> status-file.txt
	cat text | grep -A1 Unreachable_nodes: | grep -v Unreachable_nodes: | sort | uniq >> status-file.txt
fi
txt2="None of the nodes are functioning"
num_active=$(bash -c "cat text | grep -A1 Mode: | wc -l")
if [[ $num_active -eq 0 ]]
then
	echo $txt2 >> status-file.txt
else
	echo "The following node(s) are live: " >> status-file.txt
	cat text | grep -A1 Mode: | grep -v Mode: | awk '{print $2}' >> status-file.txt
fi
	

