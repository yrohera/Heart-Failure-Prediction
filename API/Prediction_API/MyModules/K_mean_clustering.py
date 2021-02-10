import matplotlib.pyplot as plt 
import numpy as np
import random
from KNN import eucledian_distance
from matplotlib import style
from matplotlib import colors as mcolors
import  math

style.use('ggplot')

def get_cluster_graph(dictionary):  #For 2d
    clusts=len(dictionary)
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    Colors=[i for i in colors]
    colors=random.sample(Colors,clusts)
    for count,i in enumerate(dictionary):
        for j in dictionary[i]:
            plt.scatter(j[0],j[1],color=colors[count])
    plt.show()

def clusters(X,clusts,error=50,iter=100):
    best=(len(X)//clusts)
    lower=int(best-best*(error/100))
    upper=math.ceil(best+best*(error/100))
    count_1,count_2,count_3=0,0,0
    main_dict={}
    max=-np.inf
    for i in range(iter):
        dict={}
        Random=random.sample(X,clusts)
        for j in range(clusts):
            dict.setdefault(j+1,[Random[j]])
        min=np.inf
        for j in X:
            for count,k in enumerate(Random):
                dist=eucledian_distance(k,j)
                if dist<min:
                    min=dist
                    min_index=count+1
            if dict[min_index][0]!=j:
                dict[min_index].append(j)
            min=np.inf
        mean=[]
        for j in dict:
            mean.append([np.mean([i[0] for i in dict[j]]),np.mean([i[1] for i in dict[j]])])
        dict.clear()
        for j in range(clusts):
            dict.setdefault(j+1,[])
        min=np.inf
        for j in X:
            for count,i in enumerate(mean):
                dist=eucledian_distance(j,i)
                if dist<min:
                    min=dist
                    min_index=count+1
            dict[min_index].append(j)
            min=np.inf
        for a in dict:
           if len(dict[a])==best:
               count_1+=1
           if len(dict[a])>=lower and len(dict[a])<=upper:
               count_2+=1
        if count_1>=count_2 and count_1>=max:
            main_dict=dict
            max=count_1
            count_1,count_2=0,0
        else:
            count_1,count_2=0,0
            continue
    if len(main_dict)!=0:
        return main_dict,1
    return dict,0





