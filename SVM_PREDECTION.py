# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:04:14 2018

@author: mm
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 07:52:44 2018

@author: mm
"""
import sys
from sklearn import svm
import pickle , gzip

from math import *
MT=[]
M1T=[]
N=[]

test=sys.argv[1] # IDS file of the blind dataset
ids2=open(test)

l=[]
for lines in ids2 :
  
  l.append( lines.rstrip().split("_"))
#print l
for i in l :
   # print i
    if len(i)>10:
        pT=open("/home/um52/project_2/blind/pro/"+i[0]+".fasta.txt") # sequnces profiles of our blind dataset
       
    else:
        pT=open("/home/um52/project_2/blind/pro/"+i[0]+"_"+i[1]+".txt")
       
    B=".".join (i)
    N.append( B)

    matrix=[]
    #print array1
    for linep in pT :
        linep=linep.split()
        matrix.append(linep)
    MT.append(matrix)


   # print len(matrix)
    m=[]
    list1=[] #print len(linep)
    for lines in ssT:
        if lines[0]!=">":
           lines=lines.split()
           lines ="".join(lines )
           list2=[]
           for i in lines :
               list2.append(i)
               m2=[]
               n=0
               for i1 in range (0,len(list2)):
                   n=+i1
                   m2.append(n)
    matrix1 = [] # matrix ss +pos
    for  i in range((len(m2))):
         matrix1.append([list2[i], m2[i]])
    M1T.append(matrix1)
    
XT_all=[]
for matrix ,matrix1 in zip(MT,M1T):
    XT=[]
    for k in matrix1:
       
        all_pro=[]
        for i in  range(k[1]-8,k[1]+9):
           # print range(k[1]-8,k[1]+9)
            if i>-1 and i <len(matrix):
                all_pro.append([float(x1) for x1 in matrix[i]])
            else :
                    all_pro.append([0.0]*20)
        XT.append(all_pro)
    XT_all.append(XT)
#print len(XT_all)
T=[]
for profile in XT_all:
   # print len(profile)
    k=[]
    for windows in profile :
        l=[]
        w=windows
        for i in range (len(w)):
            for val in w[i]:
                l.append(val)
        k.append(l)
    T.append(k)
ALL_SEQ=[]
mySVC=pickle.load(gzip.open("/home/um52/project_2/m/modelB_.pkl.gz",'r')) #SVM model 
for seq in T:
    y=mySVC.predict(seq)
    ALL_SEQ.append( y)
    
SEQ=[]
for ss in ALL_SEQ:
    s=[]
    for val in ss:
        if val==1:
            val= "H"
        if val==2:
            val= "E"
        if val==3:
            val= "-"
        s.append(val)
    SEQ.append(s)
for seq , n in zip(SEQ,N):
    seq="".join(seq)
    print (">",n,seq,'\n')

    
      
    
                
    
    

    
    
   # print len(matrix)
    
   # T.append(fT_X)
    
   
#print len(T)  
    
#tagme3
#mySVC=pickle.load(gzip.open("/home/mm/Desktop/model_.pkl.gz",'r'))
#y=mySVC.predict(T)
#for i in y :
   # if i==1:
     #   print "H"

    
    

                
            
    
    
    
    #T=[]
   # print len(matrix)
   # for list1 in matrix:
       # print len(list1)
        #for val in list1:
         #   T.append(val)
    #print len(T)

#print len(X_all[0])
   # X_all.append(X)
#print len(X_all[0][0])
