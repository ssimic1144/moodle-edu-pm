import pandas as pd
import math
import matplotlib.pyplot as plt


alg_group_5 = pd.read_csv("data/alg_group_5.csv")
alg_group_4 = pd.read_csv("data/alg_group_4.csv")
alg_group_3 = pd.read_csv("data/alg_group_3.csv")
alg_group_2 = pd.read_csv("data/alg_group_2.csv")
alg_group_1 = pd.read_csv("data/alg_group_1.csv")

############################################################

under_alg_group_5 = pd.read_csv("data/under_alg_group_5.csv")
under_alg_group_4 = pd.read_csv("data/under_alg_group_4.csv")
under_alg_group_3 = pd.read_csv("data/under_alg_group_3.csv")
under_alg_group_2 = pd.read_csv("data/under_alg_group_2.csv")
under_alg_group_1 = pd.read_csv("data/under_alg_group_1.csv")

############################################################

def addlabels(x,y):
    for i,x in enumerate(x):
        plt.text(x, y[i]//2, y[i], ha = 'center')

############################################################

xaxis = [1,2,3,4,5]

alg_yaxis = [len(alg_group_1),len(alg_group_2),len(alg_group_3),len(alg_group_4),len(alg_group_5)]

plt.bar(xaxis, alg_yaxis) 
addlabels(xaxis, alg_yaxis)
plt.xticks(xaxis)
plt.title("Algorithms course")
plt.ylabel("Number of students")
plt.xlabel("Grade")
plt.savefig("alg-bar.png")

plt.clf()

under_alg_yaxis = [len(under_alg_group_1),len(under_alg_group_2),len(under_alg_group_3),len(under_alg_group_4),len(under_alg_group_5)]

plt.bar(xaxis, under_alg_yaxis) 
addlabels(xaxis, under_alg_yaxis)
plt.xticks(xaxis)
plt.title("Undergradute Algorithms course")
plt.ylabel("Number of students")
plt.xlabel("Grade")
plt.savefig("under-alg-bar.png")

