import pandas as pd

users_grades = dict()

#########################################################
# Get ALG 
alg_all_grades_csv = "data/mid-step-alg-grades-per-user.csv"

alg_all_grades_df = pd.read_csv(alg_all_grades_csv)

# Some grouping magic...
# Quite sure this can be done in more efficient way...
alg_all_grades_df = alg_all_grades_df.groupby("userid", as_index=False).agg(lambda x: x.tolist())
alg_all_grades_df["gradecount"] = alg_all_grades_df["gradepercent"].str.len()
alg_all_grades_df["gradesum"] = alg_all_grades_df["gradepercent"].apply(lambda x: sum(x))

users_grades["userid"] = alg_all_grades_df.userid
users_grades["final"] = alg_all_grades_df.gradesum/alg_all_grades_df.gradecount

users_grades = pd.DataFrame(users_grades)
users_grades.to_csv("data/alg-total-grades-per-user.csv", index=False)
#########################################################
# Clear helper dict
users_grades = dict()

# Get ALG 
under_alg_all_grades_csv = "data/mid-step-under-alg-grades-per-user.csv"

under_alg_all_grades_df = pd.read_csv(under_alg_all_grades_csv)

# Some grouping magic...
# Quite sure this can be done in more efficient way...
under_alg_all_grades_df = under_alg_all_grades_df.groupby("userid", as_index=False).agg(lambda x: x.tolist())
under_alg_all_grades_df["gradecount"] = under_alg_all_grades_df["gradepercent"].str.len()
under_alg_all_grades_df["gradesum"] = under_alg_all_grades_df["gradepercent"].apply(lambda x: sum(x))

users_grades["userid"] = under_alg_all_grades_df.userid
users_grades["final"] = under_alg_all_grades_df.gradesum/under_alg_all_grades_df.gradecount

users_grades = pd.DataFrame(users_grades)
users_grades.to_csv("data/under-alg-total-grades-per-user.csv", index=False)
