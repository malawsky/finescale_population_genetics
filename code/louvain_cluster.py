### change $OUTPUT

import pandas as pd
from igraph import Graph
import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx
import argparse
import collections

parser=argparse.ArgumentParser()
req_grp=parser.add_argument_group(title="Required arguments")

req_grp.add_argument("--IBD_file","-I",dest="input",help="IBD sharing file",type=str,required=True)
req_grp.add_argument("--out","-o",dest="outpre",help="output directory",type=str,required=True)
req_grp.add_argument("--resolution","-r",dest="res",help="resolution for Louvain clustering",type=float,required=True)
args=parser.parse_args()
print(args)

data = pd.read_csv(args.input, sep=" ", header=None)
df2 = data.set_axis(['sample1', 'sample2', 'weight'], axis=1, inplace=False)
df2.sample1 = df2.sample1.astype('str')
df2.sample2 = df2.sample2.astype('str')
df2.weight = df2.weight.astype('float')

edgeList = df42.values.tolist()
G=nx.Graph()
for i in range(len(edgeList)):
  G.add_edge(edgeList[i][0], edgeList[i][1], weight=edgeList[i][2])
partition1 =  community_louvain.best_partition(G, weight='weight', resolution= args.res)

percentile_list = pd.DataFrame(
    {'name': partition1.keys(),
     'cluster': partition1.values()
    })
    
percentile_list.to_csv(args.outpre + '/IBD_clusters.txt', header=None, index=None, sep='\t')

