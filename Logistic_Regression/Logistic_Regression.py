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
    n[int(a[0])] +=1
    l=f.readline()

######################

w=[]
for i in range(0,cols):
    w.append(0.002*random.random()-0.001)

#######################

eta =0.000000001
preErr=0
while True:
    #############################
    dellf=[]
    dellf0=0
    for j in range(0,cols,1):
        dellf.append(0)        
    for i in range(0,rows,1):
        if(trainlabels.get(i) !=None):
            dp=0
            for j in range(0,cols,1):
                dp += (w[j]*data[i][j])
                
            for j in range(0,cols,1):
                dellf[j] += trainlabels[i]-(1/(1+math.e**(-dp))*data[i][j])
           # dellf0 += trainlabels[i]-(1/(1+math.e**(-(dp+w[cols-1]))))
               

    ###########################################          
    for j in range(0,cols-1,1):        
        w[j] +=( eta * dellf[j])
  #  w[cols-1] +=( eta*dellf0)
    ##########################################
    error=0;
    for i in range(0,rows):
        if(trainlabels.get(i) !=None):
            dp=0
            for j in range(0,cols-1):
                dp += w[j]*data[i][j]
            #error += (-trainlabels[i]*math.log(1/1+math.e**-(dp+w[2])))-((1-trainlabels[i])*math.log(math.e**-(dp+w[2])/1+math.e**-(dp+w[2])))
            error +=( (-trainlabels[i])*(math.log(1/1+math.e**(-dp))) )- ((1-trainlabels[i])*(math.log(math.e**(-dp)/1+math.e**(-dp))))
           # error=math.e**(-error)
    ###########################################
   
    #print ("error->",error)
   # print error
    err=abs(preErr-error)
    #print (err)
    preErr=error
    if(err <= 0.001):
        break

print ("w=")
temp=0

for j in range(0,cols-1): 
    w[j]=w[j]#*100
    temp +=w[j]**2
  
    #print( w[j])

#print ("\n")

temp=math.sqrt(temp);
#print("||w||=",temp)
#print temp;
#w[cols-1]*=100
#print w[cols-1]
#print dellf0
d_origin=(w[cols-1]/temp)
#print("distance to origin =",d_origin)
#print d_origin
#print ("\n")

out=open('predication','w')

for i in range(0,rows):
        if(trainlabels.get(i) ==None):
            dp=0
            for j in range(0,cols):
                dp += w[j]*data[i][j]
            if (dp>0):
                print ("1 ",i)

            else:
                print ("0 ",i)
 
out.close()
            
            
            
            
            