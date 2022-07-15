import pandas as pd
import pm4py

alg_5_df = pd.read_csv("data/trace-alg-group-5.csv")
alg_5_df = pm4py.format_dataframe(alg_5_df, case_id="courseid", activity_key="eventname", timestamp_key="timecreated")
log = pm4py.convert_to_event_log(alg_5_df)

dfg, start_activities, end_activities = pm4py.discover_performance_dfg(log)
pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, 'alg-g-5.svg')

alg_4_df = pd.read_csv("data/trace-alg-group-4.csv")
alg_4_df = pm4py.format_dataframe(alg_4_df, case_id="courseid", activity_key="eventname", timestamp_key="timecreated")
log = pm4py.convert_to_event_log(alg_4_df)

dfg, start_activities, end_activities = pm4py.discover_performance_dfg(log)
pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, 'alg-g-4.svg')

alg_3_df = pd.read_csv("data/trace-alg-group-3.csv")
alg_3_df = pm4py.format_dataframe(alg_3_df, case_id="courseid", activity_key="eventname", timestamp_key="timecreated")
log = pm4py.convert_to_event_log(alg_3_df)

dfg, start_activities, end_activities = pm4py.discover_performance_dfg(log)
pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, 'alg-g-3.svg')

alg_2_df = pd.read_csv("data/trace-alg-group-2.csv")
alg_2_df = pm4py.format_dataframe(alg_2_df, case_id="courseid", activity_key="eventname", timestamp_key="timecreated")
log = pm4py.convert_to_event_log(alg_2_df)

dfg, start_activities, end_activities = pm4py.discover_performance_dfg(log)
pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, 'alg-g-2.svg')

alg_1_df = pd.read_csv("data/trace-alg-group-1.csv")
alg_1_df = pm4py.format_dataframe(alg_1_df, case_id="courseid", activity_key="eventname", timestamp_key="timecreated")
log = pm4py.convert_to_event_log(alg_1_df)

dfg, start_activities, end_activities = pm4py.discover_performance_dfg(log)
pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, 'alg-g-1.svg')

##################################################


under_alg_5_df = pd.read_csv("data/trace-under_alg-group-5.csv")
under_alg_5_df = pm4py.format_dataframe(under_alg_5_df, case_id="courseid", activity_key="eventname", timestamp_key="timecreated")
log = pm4py.convert_to_event_log(under_alg_5_df)

dfg, start_activities, end_activities = pm4py.discover_performance_dfg(log)
pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, 'under_alg-g-5.svg')

under_alg_4_df = pd.read_csv("data/trace-under_alg-group-4.csv")
under_alg_4_df = pm4py.format_dataframe(under_alg_4_df, case_id="courseid", activity_key="eventname", timestamp_key="timecreated")
log = pm4py.convert_to_event_log(under_alg_4_df)

dfg, start_activities, end_activities = pm4py.discover_performance_dfg(log)
pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, 'under_alg-g-4.svg')

under_alg_3_df = pd.read_csv("data/trace-under_alg-group-3.csv")
under_alg_3_df = pm4py.format_dataframe(under_alg_3_df, case_id="courseid", activity_key="eventname", timestamp_key="timecreated")
log = pm4py.convert_to_event_log(under_alg_3_df)

dfg, start_activities, end_activities = pm4py.discover_performance_dfg(log)
pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, 'under_alg-g-3.svg')

under_alg_2_df = pd.read_csv("data/trace-under_alg-group-2.csv")
under_alg_2_df = pm4py.format_dataframe(under_alg_2_df, case_id="courseid", activity_key="eventname", timestamp_key="timecreated")
log = pm4py.convert_to_event_log(under_alg_2_df)

dfg, start_activities, end_activities = pm4py.discover_performance_dfg(log)
pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, 'under_alg-g-2.svg')

under_alg_1_df = pd.read_csv("data/trace-under_alg-group-1.csv")
under_alg_1_df = pm4py.format_dataframe(under_alg_1_df, case_id="courseid", activity_key="eventname", timestamp_key="timecreated")
log = pm4py.convert_to_event_log(under_alg_1_df)

dfg, start_activities, end_activities = pm4py.discover_performance_dfg(log)
pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, 'under_alg-g-1.svg')
