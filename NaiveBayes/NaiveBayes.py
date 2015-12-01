import sys
import math


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
    l=f.readline()
    n[int(a[0])] +=1

######################
def mean(numbers):
    return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers))
    return math.sqrt(variance)
def Model(dataset):
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    return summaries
#####################
c0 = []
c1 = []
for i in range(0,rows,1):
    if(trainlabels.get(i) !=None and trainlabels[i] == 0):
        c0.append(data[i])
    if(trainlabels.get(i) !=None and trainlabels[i] == 1):
        c1.append(data[i])
    
m0=Model(c0)
m1=Model(c1)

for i in range(0,rows,1):
    if(trainlabels.get(i)==None):
        d0=0
        d1=0
        for j in range(0,cols,1):
            if(m0[j][1] != 0):
                d0=d0+((m0[j][0]-data[i][j])/m0[j][1])**2
            if(m1[j][1] != 0):
                d1=d1+((m1[j][0]-data[i][j])/m1[j][1])**2
        if (d0<d1):
            print("0 ",i)
        else:
            print("1 ",i)
