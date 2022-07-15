import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

alg_trace = pd.read_csv("data/alg.csv")

alg_trace_5 = pd.read_csv("data/trace-alg-group-5.csv")
alg_trace_4 = pd.read_csv("data/trace-alg-group-4.csv")
alg_trace_3 = pd.read_csv("data/trace-alg-group-3.csv")
alg_trace_2 = pd.read_csv("data/trace-alg-group-2.csv")
alg_trace_1 = pd.read_csv("data/trace-alg-group-1.csv")

# Put back datetime dtype, since pandas do not preserve it ...
alg_trace_5["timecreated"] = alg_trace_5["timecreated"].astype("datetime64[ns]")
alg_trace_4["timecreated"] = alg_trace_4["timecreated"].astype("datetime64[ns]")
alg_trace_3["timecreated"] = alg_trace_3["timecreated"].astype("datetime64[ns]")
alg_trace_2["timecreated"] = alg_trace_2["timecreated"].astype("datetime64[ns]")
alg_trace_1["timecreated"] = alg_trace_1["timecreated"].astype("datetime64[ns]")

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

yaxis_alg_1 = list()
for d in range(len(xaxis)):
    yaxis_alg_1.append(len(alg_trace_1[alg_trace_1.timecreated.dt.month == xaxis[d].month]))

plt.figure(figsize=(10,4))
plt.plot(xaxis, yaxis_alg_5, color="b",label="Grade 5")
plt.plot(xaxis, yaxis_alg_4, color="g",label="Grade 4")
plt.plot(xaxis, yaxis_alg_3, color="y", label="Grade 3")
plt.plot(xaxis, yaxis_alg_2, color="r", label="Grade 2")
plt.plot(xaxis, yaxis_alg_1, color="c", label="Grade 1")
plt.legend()
plt.title("Students interactions with LMS on graduate level Algorithms course\nacademic year 2021/2022")
plt.ylabel("Number of interactions on LMS")
plt.xlabel("Date")

plt.savefig("alg-inter-2021-2022.png")

plt.clf()
############################################################

under_alg_trace = pd.read_csv("data/under_alg.csv")

under_alg_trace_5 = pd.read_csv("data/trace-under_alg-group-5.csv")
under_alg_trace_4 = pd.read_csv("data/trace-under_alg-group-4.csv")
under_alg_trace_3 = pd.read_csv("data/trace-under_alg-group-3.csv")
under_alg_trace_2 = pd.read_csv("data/trace-under_alg-group-2.csv")
under_alg_trace_1 = pd.read_csv("data/trace-under_alg-group-1.csv")

# Put back datetime dtype, since pandas do not preserve it ...
under_alg_trace_5["timecreated"] = under_alg_trace_5["timecreated"].astype("datetime64[ns]")
under_alg_trace_4["timecreated"] = under_alg_trace_4["timecreated"].astype("datetime64[ns]")
under_alg_trace_3["timecreated"] = under_alg_trace_3["timecreated"].astype("datetime64[ns]")
under_alg_trace_2["timecreated"] = under_alg_trace_2["timecreated"].astype("datetime64[ns]")
under_alg_trace_1["timecreated"] = under_alg_trace_1["timecreated"].astype("datetime64[ns]")

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

yaxis_under_alg_1 = list()
for d in range(len(xaxis)):
    yaxis_under_alg_1.append(len(under_alg_trace_1[under_alg_trace_1.timecreated.dt.month == xaxis[d].month]))

plt.figure(figsize=(10,4))
plt.plot(xaxis, yaxis_under_alg_5, color="b",label="Grade 5")
plt.plot(xaxis, yaxis_under_alg_4, color="g",label="Grade 4")
plt.plot(xaxis, yaxis_under_alg_3, color="y", label="Grade 3")
plt.plot(xaxis, yaxis_under_alg_2, color="r", label="Grade 2")
plt.plot(xaxis, yaxis_under_alg_1, color="c", label="Grade 1")
plt.legend()
plt.title("Students interactions with LMS on undergraduate level Algorithms course\nacademic year 2021/2022")
plt.ylabel("Number of interactions on LMS")
plt.xlabel("Date")

plt.savefig("under_alg-inter-2021-2022.png")
