#!/usr/bin/env python

#Complexity script
import numpy as np
import sys
import pandas as pd
import timeit
sys.path.append('')
from algs import bubblesort, quicksort

#testing 100 random vectors of various sizes to determine 1)the number of assignments, 2)the numnber of conditionals, 3)the time
#bubble_100_assign=[]
#bubble_100_cond=[]
complexity_df=pd.DataFrame()
for i in range(100):
    #print(i)
    #generate random vectors
    test_100=np.random.randint(low=-1000, high=5000,size=100)
    test_200=np.random.randint(low=-1000, high=5000,size=200)
    test_300=np.random.randint(low=-1000, high=5000,size=300)
    test_400=np.random.randint(low=-1000, high=5000,size=400)
    test_500=np.random.randint(low=-1000, high=5000,size=500)
    test_600=np.random.randint(low=-1000, high=5000,size=600)
    test_700=np.random.randint(low=-1000, high=5000,size=700)
    test_800=np.random.randint(low=-1000, high=5000,size=800)
    test_900=np.random.randint(low=-1000, high=5000,size=900)
    test_1000=np.random.randint(low=-1000, high=5000,size=1000)
    start=timeit.timeit()
    list,cond,assign=bubblesort(test_100)
    complexity_df.loc[i,'100_assign']=assign
    complexity_df.loc[i,'100_cond']=cond
    complexity_df.loc[i,'100_time']=timeit.timeit()-start
    start=timeit.timeit()
    list,cond,assign=bubblesort(test_200)
    complexity_df.loc[i,'200_assign']=assign
    complexity_df.loc[i,'200_cond']=cond
    complexity_df.loc[i,'200_time']=timeit.timeit()-start
    start=timeit.timeit()
    list,cond,assign=bubblesort(test_300)
    complexity_df.loc[i,'300_assign']=assign
    complexity_df.loc[i,'300_cond']=cond
    complexity_df.loc[i,'300_time']=timeit.timeit()-start
    start=timeit.timeit()
    list,cond,assign=bubblesort(test_400)
    complexity_df.loc[i,'400_assign']=assign
    complexity_df.loc[i,'400_cond']=cond
    complexity_df.loc[i,'400_time']=timeit.timeit()-start
    start=timeit.timeit()
    list,cond,assign=bubblesort(test_500)
    complexity_df.loc[i,'500_assign']=assign
    complexity_df.loc[i,'500_cond']=cond
    complexity_df.loc[i,'500_time']=timeit.timeit()-start
    start=timeit.timeit()
    list,cond,assign=bubblesort(test_600)
    complexity_df.loc[i,'600_assign']=assign
    complexity_df.loc[i,'600_cond']=cond
    complexity_df.loc[i,'600_time']=timeit.timeit()-start
    start=timeit.timeit()
    list,cond,assign=bubblesort(test_700)
    complexity_df.loc[i,'700_assign']=assign
    complexity_df.loc[i,'700_cond']=cond
    complexity_df.loc[i,'700_time']=timeit.timeit()-start
    start=timeit.timeit()
    list,cond,assign=bubblesort(test_800)
    complexity_df.loc[i,'800_assign']=assign
    complexity_df.loc[i,'800_cond']=cond
    complexity_df.loc[i,'800_time']=timeit.timeit()-start
    start=timeit.timeit()
    list,cond,assign=bubblesort(test_900)
    complexity_df.loc[i,'900_assign']=assign
    complexity_df.loc[i,'900_cond']=cond
    complexity_df.loc[i,'900_time']=timeit.timeit()-start
    start=timeit.timeit()
    list,cond,assign=bubblesort(test_1000)
    complexity_df.loc[i,'1000_assign']=assign
    complexity_df.loc[i,'1000_cond']=cond
    complexity_df.loc[i,'1000_time']=timeit.timeit()-start
    #bubble_100_assign.append(assign)
    #bubble_100_cond.append(cond)

#print(bubble_100_cond)
complexity_df_bubblesort=complexity_df
print(complexity_df_bubblesort)
complexity_df_bubblesort.to_csv('complexity_df_bubblesort.csv', index=False)

print('Starting Quicksort')
complexity_df=pd.DataFrame()
for i in range(100):
    print(i)
    #generate random vectors
    test_100=np.random.randint(low=-1000, high=5000,size=100)
    test_200=np.random.randint(low=-1000, high=5000,size=200)
    test_300=np.random.randint(low=-1000, high=5000,size=300)
    test_400=np.random.randint(low=-1000, high=5000,size=400)
    test_500=np.random.randint(low=-1000, high=5000,size=500)
    test_600=np.random.randint(low=-1000, high=5000,size=600)
    test_700=np.random.randint(low=-1000, high=5000,size=700)
    test_800=np.random.randint(low=-1000, high=5000,size=800)
    test_900=np.random.randint(low=-1000, high=5000,size=900)
    test_1000=np.random.randint(low=-1000, high=5000,size=1000)
    start=timeit.timeit()
    list,cond,assign=quicksort(test_100)
    complexity_df.loc[i,'100_time']=timeit.timeit()-start
    complexity_df.loc[i,'100_assign']=np.sum(assign)
    complexity_df.loc[i,'100_cond']=np.sum(cond)
    start=timeit.timeit()
    list,cond,assign=quicksort(test_200)
    complexity_df.loc[i,'200_time']=timeit.timeit()-start
    complexity_df.loc[i,'200_assign']=np.sum(assign)
    complexity_df.loc[i,'200_cond']=np.sum(cond)
    start=timeit.timeit()
    list,cond,assign=quicksort(test_300)
    complexity_df.loc[i,'300_time']=timeit.timeit()-start
    complexity_df.loc[i,'300_assign']=np.sum(assign)
    complexity_df.loc[i,'300_cond']=np.sum(cond)
    start=timeit.timeit()
    list,cond,assign=quicksort(test_400)
    complexity_df.loc[i,'400_time']=timeit.timeit()-start
    complexity_df.loc[i,'400_assign']=np.sum(assign)
    complexity_df.loc[i,'400_cond']=np.sum(cond)
    start=timeit.timeit()
    list,cond,assign=quicksort(test_500)
    complexity_df.loc[i,'500_time']=timeit.timeit()-start
    complexity_df.loc[i,'500_assign']=np.sum(assign)
    complexity_df.loc[i,'500_cond']=np.sum(cond)
    start=timeit.timeit()
    list,cond,assign=quicksort(test_600)
    complexity_df.loc[i,'600_time']=timeit.timeit()-start
    complexity_df.loc[i,'600_assign']=np.sum(assign)
    complexity_df.loc[i,'600_cond']=np.sum(cond)
    start=timeit.timeit()
    list,cond,assign=quicksort(test_700)
    complexity_df.loc[i,'700_time']=timeit.timeit()-start
    complexity_df.loc[i,'700_assign']=np.sum(assign)
    complexity_df.loc[i,'700_cond']=np.sum(cond)
    start=timeit.timeit()
    list,cond,assign=quicksort(test_800)
    complexity_df.loc[i,'800_time']=timeit.timeit()-start
    complexity_df.loc[i,'800_assign']=np.sum(assign)
    complexity_df.loc[i,'800_cond']=np.sum(cond)
    start=timeit.timeit()
    list,cond,assign=quicksort(test_900)
    complexity_df.loc[i,'900_time']=timeit.timeit()-start
    complexity_df.loc[i,'900_assign']=np.sum(assign)
    complexity_df.loc[i,'900_cond']=np.sum(cond)
    start=timeit.timeit()
    list,cond,assign=quicksort(test_1000)
    complexity_df.loc[i,'1000_time']=timeit.timeit()-start
    complexity_df.loc[i,'1000_assign']=np.sum(assign)
    complexity_df.loc[i,'1000_cond']=np.sum(cond)
    #bubble_100_assign.append(assign)
    #bubble_100_cond.append(cond)

#print(bubble_100_cond)
complexity_df_quicksort=complexity_df
print(complexity_df_quicksort)
complexity_df_quicksort.to_csv('complexity_df_quicksort.csv', index=False)
