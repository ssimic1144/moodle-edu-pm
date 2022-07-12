import pandas as pd
import math
import matplotlib.pyplot as plt

ai_csv = "data/ai-total-grades-per-user.csv"
alg_csv = "data/alg-total-grades-per-user.csv"

ai_df = pd.read_csv(ai_csv)
alg_df = pd.read_csv(alg_csv)

#############################################################

ai_group_4 = ai_df[ai_df.final >= 0.9]
ai_group_3 = ai_df[(ai_df.final >= 0.8) & (ai_df.final < 0.9)] 
ai_group_2 = ai_df[(ai_df.final >= 0.65) & (ai_df.final < 0.8)] 
ai_group_1 = ai_df[(ai_df.final >= 0.5) & (ai_df.final < 0.65)]
ai_group_0 = ai_df[ai_df.final < 0.5]
#print(ai_group_1)
#print(ai_group_2)
#print(ai_group_3)
#print(ai_group_4)

#############################################################

alg_group_4 = alg_df[alg_df.final >= 0.9]
alg_group_3 = alg_df[(alg_df.final >= 0.8) & (alg_df.final < 0.9)] 
alg_group_2 = alg_df[(alg_df.final >= 0.65) & (alg_df.final < 0.8)] 
alg_group_1 = alg_df[(alg_df.final >= 0.5) & (alg_df.final < 0.65)]
alg_group_0 = alg_df[alg_df.final < 0.5]
#print(alg_group_1)
#print(alg_group_2)
#print(alg_group_3)
#print(alg_group_4)

############################################################

def addlabels(x,y):
    for i,x in enumerate(x):
        plt.text(x, y[i]//2, y[i], ha = 'center')

############################################################

xaxis = [2,3,4,5]

alg_yaxis = [len(alg_group_1),len(alg_group_2),len(alg_group_3),len(alg_group_4)]

plt.bar(xaxis, alg_yaxis) 
addlabels(xaxis, alg_yaxis)
plt.xticks(xaxis)
plt.title("Algorithms course")
plt.ylabel("Number of students")
plt.xlabel("Grade")
plt.savefig("alg-bar.png")

plt.clf()

ai_yaxis = [len(ai_group_1),len(ai_group_2),len(ai_group_3),len(ai_group_4)]

plt.bar(xaxis, ai_yaxis) 
addlabels(xaxis, ai_yaxis)
plt.xticks(xaxis)
plt.title("AI course")
plt.ylabel("Number of students")
plt.xlabel("Grade")
plt.savefig("ai-bar.png")

