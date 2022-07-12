import pandas as pd 

# Helper lists
ai_helper = list()
alg_helper = list()

raw_data_dir = "../../Downloads/csv-mdl-dir"

########################################################################

grade_items_csv = "mdl_grade_items.csv"

grade_items_full_df = pd.read_csv(raw_data_dir+"/"+grade_items_csv)

# Get course specific grade items
ai_gi_df = grade_items_full_df[grade_items_full_df.courseid == 4988]
alg_gi_df = grade_items_full_df[grade_items_full_df.courseid == 5002]

# Select only item ids
ai_gi_df = ai_gi_df["id"]
alg_gi_df = alg_gi_df["id"]

# Append to helper
ai_helper.append(ai_gi_df)
alg_helper.append(alg_gi_df)

# Get history items
grade_items_history_csv = "mdl_grade_items_history.csv"

grade_items_full_df = pd.read_csv(raw_data_dir+"/"+grade_items_history_csv)

# Get course specific grade items
ai_gi_df = grade_items_full_df[grade_items_full_df.courseid == 4988]
alg_gi_df = grade_items_full_df[grade_items_full_df.courseid == 5002]

# Select only item ids
ai_gi_df = ai_gi_df["id"]
alg_gi_df = alg_gi_df["id"]

# Append to helper
ai_helper.append(ai_gi_df)
alg_helper.append(alg_gi_df)

# Create full grade items series
ai_gi_df = pd.concat(ai_helper)
alg_gi_df = pd.concat(alg_helper)

########################################################################

# Get outcomes csv
grade_outcomes_csv = "mdl_grade_grades.csv"

grade_out_partial_df = pd.read_csv(raw_data_dir+"/"+grade_outcomes_csv)

# Get outcomes for specific course item
ai_out_df = grade_out_partial_df.merge(ai_gi_df.to_frame(), left_index=True, right_index=True)
alg_out_df = grade_out_partial_df.merge(alg_gi_df.to_frame(), left_index=True, right_index=True)

big_stuff = "mdl_grade_grades_history.csv"

ai_helper = list()
alg_helper = list()

ai_helper.append(ai_out_df)
alg_helper.append(alg_out_df)

chunksize = 10**6

with pd.read_csv(raw_data_dir+"/"+big_stuff, chunksize=chunksize) as reader:
    for chunk in reader:
        ai_helper.append(chunk.merge(ai_gi_df.to_frame(), left_index=True, right_index=True))
        alg_helper.append(chunk.merge(alg_gi_df.to_frame(), left_index=True, right_index=True))
        print(len(ai_helper))

# Create full grades outcomes DF
ai_df = pd.concat(ai_helper)
alg_df = pd.concat(alg_helper)

# Fill nan values
ai_df.finalgrade = ai_df.finalgrade.fillna("0.0")
alg_df.finalgrade = alg_df.finalgrade.fillna("0.0")

# Ensure correct type
ai_df.finalgrade = ai_df.finalgrade.astype(float)
alg_df.finalgrade = alg_df.finalgrade.astype(float)

# Calculate grade percent
ai_df["gradepercent"] = ai_df.finalgrade/ai_df.rawgrademax
alg_df["gradepercent"] = alg_df.finalgrade/alg_df.rawgrademax

# Select only the key columns
ai_df = ai_df[["itemid","userid","gradepercent"]]
alg_df = alg_df[["itemid","userid","gradepercent"]]

# Create csvs
ai_df.to_csv("data/mid-step-ai-grades-per-user.csv", index=False)
alg_df.to_csv("data/mid-step-alg-grades-per-user.csv", index=False)
############################################################################

