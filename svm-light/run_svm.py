'''
Created on Nov 18, 2015

@author: suryamylar
'''
import sys
import os
import subprocess

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
    if(trainlabels[int(a[1])]==0):
        trainlabels[int(a[1])]=-1
    n[int(a[0])] +=1
    l=f.readline()
    
    
#######################################

C = sys.argv[3]

svmtrain=open("svmtrain",'w')
svmtest=open("svmtest",'w')

for i in range(rows):
    if i in trainlabels:
        svmtrain.write(str(trainlabels.get(i)))
        for j in range(cols):
            svmtrain.write(" "+str(j+1)+":"+str(data[i][j]))
        svmtrain.write("\n")
    else:
        for j in range(cols):
            svmtest.write("0")
            svmtest.write(" "+str(j+1)+":"+str(data[i][j]))
        svmtest.write("\n")
cmd1="./svm_light/svm_learn -c " + str(C) +" svmtrain svmmodel >& /dev/null"        
os.system(cmd1)
cmd2="./svm_light/svm_classify svmtest svmmodel svmclassification >& /dev/null"
subprocess.call(cmd2,shell=True)


classification=open("svmclassification")
pridect=open("svmpredication",'w')
for i in range(0,rows):     
    if(trainlabels.get(i) ==None): 
        l=classification.readline()
        if(l!=''):
            a=l.split(' ')
            a=float(a[0])
            if a<0:
                pridect.write("0 "+ str(i)+"\n")
                print
            else:
                pridect.write("1 "+ str(i)+"\n")   