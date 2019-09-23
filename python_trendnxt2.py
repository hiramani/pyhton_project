#!/usr/bin/env python
# coding: utf-8

# In[6]:


#program 1
r=range(4)
print(type(r))
print(r)
add_r=r
print(add_r)
r.append(4)
print(add_r)
add_r=r[:]
print(add_r)
r.append(5)
print(add_r)


# In[19]:


#program2
def f(n):
    for x in range(n):
        yield x**3

for x in f(6):
    print (x)
   


# In[25]:


#program3
str=input("enter the string value  : ")
count_e=0
for i in str:
    if i=='e'or i=='E':
        count_e+=1
if count_e>=2:
    print(True)
else:
    print(False)
    


# In[6]:


#program4
counter = 1
def dolots(count):
    global counter
    for i in (1, 2, 3):
        counter = count + i
        return counter
        
print(dolots(4))


# In[1]:


#program5
file_name=input("name of the file :")
file1=open(file_name,'r')
line=0
for i in file1:
    count_words=0
    count_char=0
    counter=i.split()
    count_words=len(counter)
    line+=1
    for j in counter:
        
        for k in j:
            count_char+=1
    print("In line {0}, there are {1} words and {2} characters in each line. ".format(line,count_words,count_char))
        
    


# In[9]:


#program6
list1=list(map(int,input("enter the number : ").split()))
list2=list(map(int,input("enter the number : ").strip().split()))
list3=list(map(int,input("enter the number : ").strip().split()))
l2_max1=list2[0]
l2_max2=list2[0]
l3_max1=list3[0]
l3_max2=list3[0]
l2_min1=999999999999
l2_min2=999999999999
l3_min1=999999999999
l3_min2=999999999999
max1=list1[0]
max2=list1[0]
min1=9999999999
min2=999999999999
new_list=[]
new1_list=[]

#for list1
for i in list1:
    if max1<i:
        max1=i
    if min1>i:
        min1=i
for i in list1:
    if min1!=i and min2>i:
        min2=i
    if (max1!=i) and (max2<i):
        max2=i
# for list2
for i in list2:
    if l2_max1<i:
        l2_max1=i
    if l2_min1>i:
        l2_min1=i
for i in list2:
    if l2_min1!=i and l2_min2>i:
        l2_min2=i
    if (l2_max1!=i) and (l2_max2<i):
        l2_max2=i
# for list3
for i in list3:
    if l3_max1<i:
        l3_max1=i
    if l3_min1>i:
        l3_min1=i
for i in list3:
    if l3_min1!=i and l3_min2>i:
        l3_min2=i
    if (l3_max1!=i) and (l3_max2<i):
        l3_max2=i

        
new_list.append(max1)
new_list.append(max2)
new1_list.append(min1)
new1_list.append(min2)
new_list.append(l2_max1)
new_list.append(l2_max2)
new_list.append(l3_max1)
new_list.append(l3_max2)
new1_list.append(l2_min1)
new1_list.append(l2_min2)
new1_list.append(l3_min1)
new1_list.append(l3_min2)


max_avg=sum(new_list)/6
min_avg=sum(new1_list)/6
print("average value from the max list : ",max_avg)
print("average value from the min list : ",min_avg)


    
    


# In[8]:


#program7
def ip_conversion(n):
    ip_no=""
    ip_no=128*int(n[0])+64*int(n[1])+32*int(n[2])+16*int(n[3])+8*int(n[4])+4*int(n[5])+2*int(n[6])+1*int(n[7])
    return ip_no
net_mask=int(input("enter the net mask no. : "))
str1=""
for i in range(net_mask):
    str1+="1"
l=len(str1)
rem_l=32-l
p=[]
for i in range(rem_l):
    str1+="0"
strr=""
join_str='.'
split_str=[str1[i:i+8] for i in range(0,len(str1),8)]
j=0
for i in split_str:
    p1=ip_conversion(i)
    strr=str(p1)
    p.insert(j,strr)
    j+=8
    
join_str=join_str.join(p)
print("IP of the net mask {0} is ".format(net_mask),join_str) 


# In[1]:


#progarm8
import xml.etree.ElementTree as et
tree=et.parse("myxml.xml")
count=0
root=tree.getroot()
for i in root:
    count+=1
    print("Book no.{0} details : ".format(count))
    for j in i:
        print(j.text)



# In[3]:


#program9
import glob
import os
path=input("enter the path :")
files = [f for f in glob.glob(path + "**/*" , recursive=True)]

for f in files:
    size=os.stat(f).st_size
    if size==0:
        print("{0} size: ".format(f),size)


# In[1]:


#program10
n=int(input("enter the no. of element: "))
l1=[] 
[l1.append(input()) for i in range(n)]
l2=set(l1)
l3=[]
l4=list(l2)
l5=[]
for i in l4:
    print(i)
    l3=list(set(i))
    print(l3)
    l5=l5+(l3)  
    print(l5)
print("after deleting the duplicate element :",set(l5))


# In[ ]:




