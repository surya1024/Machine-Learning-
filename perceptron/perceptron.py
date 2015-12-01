import sys
import math
import random

datafile = sys.argv[1]
f = open(datafile)
data = []
i=0
l=f.readline()

while(l != ''):
    a=l.split()
    l2=[]
    for j in range(0,len(a),1):
        l2.append(float(a[j]))
    l2.append(1)
    data.append(l2)
    l=f.readline()

rows = len(data)
cols=len(data[0])
f.close()

labelfile = sys.argv[2]
f=open(labelfile)
trainlabels={}
n=[]
n.append(0)
n.append(0)
l=f.readline()
while(l != ''):
    a=l.split()
    trainlabels[int(a[1])] = int(a[0])
    if(trainlabels[int(a[1])]==0)
        trainlabels[int(a[1])]=-1
    n[int(a[0])] +=1
    l=f.readline()

######################

w=[]
for i in range(0,cols):
    w[i]=0.002* math.random.random()-.001

#######################

eta=0.00001
for i