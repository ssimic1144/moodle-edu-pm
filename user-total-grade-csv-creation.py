import pandas as pd

users_grades = dict()

#########################################################
# Get AI 
ai_all_grades_csv = "data/mid-step-ai-grades-per-user.csv"

ai_all_grades_df = pd.read_csv(ai_all_grades_csv)

# Some grouping magic...
# Quite sure this can be done in more efficient way...
ai_all_grades_df = ai_all_grades_df.groupby("userid", as_index=False).agg(lambda x: x.tolist())
ai_all_grades_df["gradecount"] = ai_all_grades_df["gradepercent"].str.len()
ai_all_grades_df["gradesum"] = ai_all_grades_df["gradepercent"].apply(lambda x: sum(x))

users_grades["userid"] = ai_all_grades_df.userid
users_grades["final"] = ai_all_grades_df.gradesum/ai_all_grades_df.gradecount

# Create DF and write csv
users_grades = pd.DataFrame(users_grades)
users_grades.to_csv("data/ai-total-grades-per-user.csv", index=False)
#########################################################
# Clear helper dict
users_grades = dict()

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
