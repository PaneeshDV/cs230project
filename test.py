
import csv
import pandas as pd
filename = "my_csv_file.csv"
headers = ["trace", "Cache_policy", "repl","ipc","hit","miss","size"]

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
filename = "my_csv_file.csv"
df = pd.read_csv(filename)

import os
def get_values(s,size):
    global df
    n = (s.split("/")[1]).split("-bimodal")[0]
    c = (s.split("-1core-")[1]).split(".")[0][0]
    r = (s.split("-1core-")[0]).split("-")[-1]
    ipc=0
    hit=0
    miss=0
    os.system(f"./run.sh {s}")
    print(s)
    with open('a.txt', 'r') as file:
        first_line = file.readline()
      #  print(first_line.split(", "))
        ipc=first_line.split(", ")[0]
        hit=first_line.split(", ")[1]
        
    
        miss=first_line.split(", ")[2].replace("\n","")
    # new_data = {'col1': value1, 'col2': value2, 'col3': value3}
    l=[n,c,r,ipc,hit,miss,size]
    df.loc[len(df.index)] = l

 
directory = 'results_30M_a'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith('.txt'):
        get_values(f,1)
directory = 'results_30M_b'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith('.txt'):
        get_values(f,2)
directory = 'results_30M_c'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith('.txt'):
        get_values(f,3)
directory = 'results_30M_d'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith('.txt'):
        get_values(f,4)

        
import numpy as np
import matplotlib.pyplot as plt

traces = ["cadical-high-60K-1227B.champsimtrace.xz","cadical-high-60K-134B.champsimtrace.xz","kissat-inc-high-30K-1802B.champsimtrace.xz"]
sizes = [1,2,3,4]
for trac in traces:
    for si in sizes:
        def fun(trace,policy,s):
            l =[]
            for i in df.index:
                if(df['trace'][i]==trace and df['Cache_policy'][i]==policy and df['size'][i]==s):
                    t = []
                    t.append(df['repl'][i])
                    t.append(float(df['ipc'][i]))
                    l.append(t)
            return l
        # list =[]
        lfu_values= []
        fifo_values = []
        rand_values = []
        lru_values = []

        def extract(p):
            for i in p:
                if(i[0] == 'rand'):
                    rand_values.append(i[1])
                elif(i[0] == 'lru'):
                    lru_values.append(i[1])
                elif(i[0] == 'lfu'):
                    lfu_values.append(i[1])
                elif(i[0] == 'fifo'):
                    fifo_values.append(i[1])

        extract(fun(trac,"I",si))
        extract(fun(trac,"E",si))
        extract(fun(trac,"N",si))
        llc_ways = ['Inclusive','Exclusive','NINE']
        # Set the positions of the bars on the x-axis
        r = np.array([0,0.75,1.5])

        # Set the width of the bars
        bar_width = 0.07

        # y2 = [0.190024,0.190822,0.190351,0.19083]
        # # Create the figure and the axes
        fig, ax = plt.subplots()

        ax.bar(r -  1*bar_width, lfu_values, color='blue', width=0.75*bar_width, edgecolor='black', label='lfu')
        ax.bar(r, fifo_values, color='yellow', width=0.75*bar_width, edgecolor='black', label='fifo')
        ax.bar(r + 1*bar_width, rand_values, color='red', width=0.75*bar_width, edgecolor='black', label='rand')
        ax.bar(r + 2*bar_width, lru_values, color='lightgreen', width=0.75*bar_width, edgecolor='black', label='lru')

        # Set the x-axis labels and ticks
        ax.set_xticks(r)
        ax.set_xticklabels(llc_ways)
        ax.set_xlim([-0.25,2.25])
        # Set the y-axis label
        ax.set_xlabel('Cache_policies')
        ax.set_ylabel('IPC Values')

        # Set the plot title and legend
        ax.set_title(str(si)+trac)
        ax.legend()
        # plt.savefig(str(si)+trac+'.png')
# Show the plot

import numpy as np
import matplotlib.pyplot as plt
traces = ["cadical-high-60K-1227B.champsimtrace.xz","cadical-high-60K-134B.champsimtrace.xz","kissat-inc-high-30K-1802B.champsimtrace.xz"]     
for trace in traces:
    def func(trac,policy,repl):
        l =[]
        for i in df.index:
            if(df['trace'][i]==trac and df['Cache_policy'][i]==policy and df['repl'][i]==repl):
                t = []
                t.append(df['size'][i])
                t.append(float(df['ipc'][i]))
                l.append(t)
        return l

    size1_val = []
    size2_val = []
    size3_val = []
    size4_val = []

    def ext(p):
        for i in p:
            if(i[0] == 1):
                size1_val.append(i[1])
            elif(i[0] == 2):
                size2_val.append(i[1])
            elif(i[0] == 3):
                size3_val.append(i[1])
            elif(i[0] == 4):
                size4_val.append(i[1])

    ext(func(trace,"I","fifo"))
    ext(func(trace,"E","fifo"))
    ext(func(trace,"N","fifo"))
    llc_ways = ['Inclusive','Exclusive','NINE']
    # Set the positions of the bars on the x-axis
    r = np.array([0,0.75,1.5])

    # Set the width of the bars
    bar_width = 0.07

    # y2 = [0.190024,0.190822,0.190351,0.19083]
    # # Create the figure and the axes
    fig, ax = plt.subplots()

    ax.bar(r -  1*bar_width, size1_val, color='blue', width=0.75*bar_width, edgecolor='black', label='2048x16')
    ax.bar(r, size2_val, color='yellow', width=0.75*bar_width, edgecolor='black', label='8192x16')
    ax.bar(r + 1*bar_width, size3_val, color='red', width=0.75*bar_width, edgecolor='black', label='16384x32')
    ax.bar(r + 2*bar_width, size4_val, color='lightgreen', width=0.75*bar_width, edgecolor='black', label='65536x32')

    # Set the x-axis labels and ticks
    ax.set_xticks(r)
    ax.set_xticklabels(llc_ways)
    ax.set_xlim([-0.25,2.25])
    # Set the y-axis label
    ax.set_xlabel('Cache_policies')
    ax.set_ylabel('IPC Values')

    # Set the plot title and legend
    ax.set_title("FIFO - "+trace)
    ax.legend(loc='best')
    # plt.savefig("fifo_dd"+trace+'.png')


import matplotlib.pyplot as plt
import seaborn as sns
  
# use to set style of background of plot
sns.set(style="whitegrid")
# define the set of points
x = [1,2,4,8,12,16]
y = [0.155959, 0.155988, 0.156394, 0.158914, 0.158984, 0.164973]
x1 = [1,2,4 ,8,12, 16]
y1 = [0.155959, 0.157897, 0.163449, 0.169556, 0.169756, 0.174712]

# plot the points and connect them with lines
# plt.plot(x, y, '-x',color='blue',label='plot1')
plt.plot(x, y, color='red', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=8,label ='L2C')
# plt.plot(x1, y1,'-x', color='red',label='plot2')
plt.plot(x1, y1, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=8,label='LLC')
plt.title("ipc value for given multiplication factor for no of sets")
# add labels to the plot
plt.xlabel('value of multiplication factor')
plt.ylabel('ipc value')
# plt.title('Joined Points')
plt.legend()
# show the plot
# plt.savefig('comparison_dd.png')


os.system("rm a.txt")
df.to_csv('data.csv')
