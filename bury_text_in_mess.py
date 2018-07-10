#!/bin/sh

from random import shuffle, randint

output = open('top-secret.txt' , 'w') #create file and write to it ('w')

total_size = 1000 #file size
clusterF = [] 
for i in range(total_size):
	pos = range(0, 255)
	shuffle(pos)
	for j in pos:
		clusterF.append(chr(j))

	if i == total_size/2: #bury you message in the middle of this mess
		clusterF.append("Type your hidden message here")

content = "".join(clusterF)
output.write(content)
output.close()