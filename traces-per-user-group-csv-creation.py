import pandas as pd

alg_group_5 = pd.read_csv("data/alg_group_5.csv")
alg_group_4 = pd.read_csv("data/alg_group_4.csv")
alg_group_3 = pd.read_csv("data/alg_group_3.csv")
alg_group_2 = pd.read_csv("data/alg_group_2.csv")
alg_group_1 = pd.read_csv("data/alg_group_1.csv")

alg_trace = pd.read_csv("data/alg.csv")
alg_trace = alg_trace.sort_values("timecreated")
alg_trace["timecreated"] = pd.to_datetime(alg_trace["timecreated"])

alg_trace_5 = alg_trace[alg_trace.userid.isin(alg_group_5.userid)]
alg_trace_4 = alg_trace[alg_trace.userid.isin(alg_group_4.userid)]
alg_trace_3 = alg_trace[alg_trace.userid.isin(alg_group_3.userid)]
alg_trace_2 = alg_trace[alg_trace.userid.isin(alg_group_2.userid)]
alg_trace_1 = alg_trace[alg_trace.userid.isin(alg_group_1.userid)]

######################################################################

under_alg_group_5 = pd.read_csv("data/under_alg_group_5.csv")
under_alg_group_4 = pd.read_csv("data/under_alg_group_4.csv")
under_alg_group_3 = pd.read_csv("data/under_alg_group_3.csv")
under_alg_group_2 = pd.read_csv("data/under_alg_group_2.csv")
under_alg_group_1 = pd.read_csv("data/under_alg_group_1.csv")

under_alg_trace = pd.read_csv("data/under_alg.csv")
under_alg_trace = under_alg_trace.sort_values("timecreated")
under_alg_trace["timecreated"] = pd.to_datetime(under_alg_trace["timecreated"])

under_alg_trace_5 = under_alg_trace[under_alg_trace.userid.isin(under_alg_group_5.userid)]
under_alg_trace_4 = under_alg_trace[under_alg_trace.userid.isin(under_alg_group_4.userid)]
under_alg_trace_3 = under_alg_trace[under_alg_trace.userid.isin(under_alg_group_3.userid)]
under_alg_trace_2 = under_alg_trace[under_alg_trace.userid.isin(under_alg_group_2.userid)]
under_alg_trace_1 = under_alg_trace[under_alg_trace.userid.isin(under_alg_group_1.userid)]


#######################################################################

alg_trace_5.to_csv("data/trace-alg-group-5.csv", index=False)
alg_trace_4.to_csv("data/trace-alg-group-4.csv", index=False)
alg_trace_3.to_csv("data/trace-alg-group-3.csv", index=False)
alg_trace_2.to_csv("data/trace-alg-group-2.csv", index=False)
alg_trace_1.to_csv("data/trace-alg-group-1.csv", index=False)

under_alg_trace_5.to_csv("data/trace-under_alg-group-5.csv", index=False)
under_alg_trace_4.to_csv("data/trace-under_alg-group-4.csv", index=False)
under_alg_trace_3.to_csv("data/trace-under_alg-group-3.csv", index=False)
under_alg_trace_2.to_csv("data/trace-under_alg-group-2.csv", index=False)
under_alg_trace_1.to_csv("data/trace-under_alg-group-1.csv", index=False)
