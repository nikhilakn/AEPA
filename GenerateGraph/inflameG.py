import os
import csv
import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def nodeCopy(x, s):
    nx=int(x.split(".")[0])+s
    return str(nx)+".c"
def nodeMap(x,s):
    nx=int(x.split(".")[0])-s
    if nx > 0:
        return str(nx)+".c"
    else:
        return x
def edgeMap(e, el,ns):
    u=nodeMap(e[0],ns)
    v=nodeMap(e[1],ns)
    for ed in el:
        if (ed[0]==u and ed[1]==v) or (ed[0]==v and ed[1]==u):
            return (e[0],e[1],ed[2])
        if (e[0]==ed[0] and e[1]==ed[1]) or (e[1]==ed[0] and e[0]==ed[1]):
            return ed
        if (u==v):
            return (e[0],e[1],1)
   

p=input("Enter file path: ")
n=os.listdir(p) # Nodes of G
e=[] # Edges of G
e.append(('3.c', '1.c',1))
e.append(('3.c', '2.c',2))
e.append(('1.c', '2.c',3))

n1=[nodeCopy(x,len(n)) for x in n] #Copying nodes from G
cn=n+n1 #Combining nodes of G and G1
ce=list(itertools.combinations(cn,2))
e2=[edgeMap(edge,e,len(n)) for edge in ce ] # Edge maping 
print(e2)
#exit()
G=nx.Graph() #Networkx graph for combined graph
G.add_nodes_from(cn)
G.add_weighted_edges_from(e2)
pos=nx.circular_layout(G)
nx.draw_networkx_nodes(G,pos,node_color='red',node_size=2)
nx.draw_networkx_edges(G,pos)
plt.show()
print(nx.degree(G))

