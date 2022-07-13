import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

alg_group_5 = pd.read_csv("data/alg_group_5.csv")
alg_group_4 = pd.read_csv("data/alg_group_4.csv")
alg_group_3 = pd.read_csv("data/alg_group_3.csv")
alg_group_2 = pd.read_csv("data/alg_group_2.csv")

alg_trace = pd.read_csv("data/alg.csv")
alg_trace = alg_trace.sort_values("timecreated")
alg_trace["timecreated"] = pd.to_datetime(alg_trace["timecreated"])

alg_trace_5 = alg_trace[alg_trace.userid.isin(alg_group_5.userid)]
alg_trace_4 = alg_trace[alg_trace.userid.isin(alg_group_4.userid)]
alg_trace_3 = alg_trace[alg_trace.userid.isin(alg_group_3.userid)]
alg_trace_2 = alg_trace[alg_trace.userid.isin(alg_group_2.userid)]

xaxis = pd.date_range(start="2021-9-1", end=max(alg_trace.timecreated), freq="1M",normalize=True)
xaxis_day = pd.date_range(min(alg_trace.timecreated), max(alg_trace.timecreated),normalize=True)

yaxis_alg_5 = list()
for d in range(len(xaxis)):
    yaxis_alg_5.append(len(alg_trace_5[alg_trace_5.timecreated.dt.month == xaxis[d].month]))

yaxis_alg_4 = list()
for d in range(len(xaxis)):
    yaxis_alg_4.append(len(alg_trace_4[alg_trace_4.timecreated.dt.month == xaxis[d].month]))

yaxis_alg_3 = list()
for d in range(len(xaxis)):
    yaxis_alg_3.append(len(alg_trace_3[alg_trace_3.timecreated.dt.month == xaxis[d].month]))

yaxis_alg_2 = list()
for d in range(len(xaxis)):
    yaxis_alg_2.append(len(alg_trace_2[alg_trace_2.timecreated.dt.month == xaxis[d].month]))

plt.figure(figsize=(10,4))
plt.plot(xaxis, yaxis_alg_5, color="b",label="Grade 5")
plt.plot(xaxis, yaxis_alg_4, color="g",label="Grade 4")
plt.plot(xaxis, yaxis_alg_3, color="y", label="Grade 3")
plt.plot(xaxis, yaxis_alg_2, color="r", label="Grade 2")
plt.legend()
plt.title("Students interactions with LMS on graduate level Algorithms course\nacademic year 2021/2022")
plt.ylabel("Number of interactions on LMS")
plt.xlabel("Date")

plt.savefig("alg-inter-2021-2022.png")

plt.clf()
############################################################

under_alg_group_5 = pd.read_csv("data/under_alg_group_5.csv")
under_alg_group_4 = pd.read_csv("data/under_alg_group_4.csv")
under_alg_group_3 = pd.read_csv("data/under_alg_group_3.csv")
under_alg_group_2 = pd.read_csv("data/under_alg_group_2.csv")

under_alg_trace = pd.read_csv("data/under_alg.csv")
under_alg_trace = under_alg_trace.sort_values("timecreated")
under_alg_trace["timecreated"] = pd.to_datetime(under_alg_trace["timecreated"])

under_alg_trace_5 = under_alg_trace[under_alg_trace.userid.isin(under_alg_group_5.userid)]
under_alg_trace_4 = under_alg_trace[under_alg_trace.userid.isin(under_alg_group_4.userid)]
under_alg_trace_3 = under_alg_trace[under_alg_trace.userid.isin(under_alg_group_3.userid)]
under_alg_trace_2 = under_alg_trace[under_alg_trace.userid.isin(under_alg_group_2.userid)]

xaxis = pd.date_range(start="2021-10", end=max(under_alg_trace.timecreated), freq="1M",normalize=True)
xaxis_day = pd.date_range(min(under_alg_trace.timecreated), max(under_alg_trace.timecreated),normalize=True)

yaxis_under_alg_5 = list()
for d in range(len(xaxis)):
    yaxis_under_alg_5.append(len(under_alg_trace_5[under_alg_trace_5.timecreated.dt.month == xaxis[d].month]))

yaxis_under_alg_4 = list()
for d in range(len(xaxis)):
    yaxis_under_alg_4.append(len(under_alg_trace_4[under_alg_trace_4.timecreated.dt.month == xaxis[d].month]))

yaxis_under_alg_3 = list()
for d in range(len(xaxis)):
    yaxis_under_alg_3.append(len(under_alg_trace_3[under_alg_trace_3.timecreated.dt.month == xaxis[d].month]))

yaxis_under_alg_2 = list()
for d in range(len(xaxis)):
    yaxis_under_alg_2.append(len(under_alg_trace_2[under_alg_trace_2.timecreated.dt.month == xaxis[d].month]))

plt.figure(figsize=(10,4))
plt.plot(xaxis, yaxis_under_alg_5, color="b",label="Grade 5")
plt.plot(xaxis, yaxis_under_alg_4, color="g",label="Grade 4")
plt.plot(xaxis, yaxis_under_alg_3, color="y", label="Grade 3")
plt.plot(xaxis, yaxis_under_alg_2, color="r", label="Grade 2")
plt.legend()
plt.title("Students interactions with LMS on undergraduate level Algorithms course\nacademic year 2021/2022")
plt.ylabel("Number of interactions on LMS")
plt.xlabel("Date")

plt.savefig("under_alg-inter-2021-2022.png")
