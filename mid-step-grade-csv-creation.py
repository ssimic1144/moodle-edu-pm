import pandas as pd 

# Helper lists
alg_helper = list()
under_alg_helper = list()

raw_data_dir = "../../Downloads/csv-mdl-dir"

########################################################################

grade_items_csv = "mdl_grade_items.csv"

grade_items_full_df = pd.read_csv(raw_data_dir+"/"+grade_items_csv)

# Get course specific grade items
alg_gi_df = grade_items_full_df[grade_items_full_df.courseid == 5002]
under_alg_gi_df = grade_items_full_df[grade_items_full_df.courseid == 4720]

# Select only item ids
alg_gi_df = alg_gi_df["id"]
under_alg_gi_df = under_alg_gi_df["id"]

# Append to helper
alg_helper.append(alg_gi_df)
under_alg_helper.append(under_alg_gi_df)

# Get history items
grade_items_history_csv = "mdl_grade_items_history.csv"

grade_items_full_df = pd.read_csv(raw_data_dir+"/"+grade_items_history_csv)

# Get course specific grade items
alg_gi_df = grade_items_full_df[grade_items_full_df.courseid == 5002]
under_alg_gi_df = grade_items_full_df[grade_items_full_df.courseid == 4720]

# Select only item ids
alg_gi_df = alg_gi_df["id"]
under_alg_gi_df = under_alg_gi_df["id"]

# Append to helper
alg_helper.append(alg_gi_df)
under_alg_helper.append(under_alg_gi_df)

# Create full grade items series
alg_gi_df = pd.Series(alg_helper).explode(ignore_index=True)
under_alg_gi_df = pd.Series(under_alg_helper).explode(ignore_index=True)

########################################################################

# Get outcomes csv
grade_outcomes_csv = "mdl_grade_grades.csv"

grade_out_partial_df = pd.read_csv(raw_data_dir+"/"+grade_outcomes_csv)

# Get outcomes for specific course item
alg_out_df = grade_out_partial_df[grade_out_partial_df.itemid.isin(alg_gi_df)]
under_alg_out_df = grade_out_partial_df[grade_out_partial_df.itemid.isin(under_alg_gi_df)]


big_stuff = "mdl_grade_grades_history.csv"

alg_helper = list()
under_alg_helper = list()

alg_helper.append(alg_out_df)
under_alg_helper.append(under_alg_out_df)

chunksize = 10**6

with pd.read_csv(raw_data_dir+"/"+big_stuff, chunksize=chunksize) as reader:
    for chunk in reader:
        alg_helper.append(chunk[chunk.itemid.isin(alg_gi_df)])
        under_alg_helper.append(chunk[chunk.itemid.isin(under_alg_gi_df)])
        print(len(alg_helper))

# Create full grades outcomes DF
alg_df = pd.concat(alg_helper)
under_alg_df = pd.concat(under_alg_helper)


# Fill nan values
#alg_df.finalgrade = alg_df.finalgrade.fillna("0.0")
#under_alg_df.finalgrade = under_alg_df.finalgrade.fillna("0.0")

# Drop NA
alg_df = alg_df.dropna(subset=["finalgrade"])
under_alg_df = under_alg_df.dropna(subset=["finalgrade"])

# Ensure correct type
alg_df.finalgrade = alg_df.finalgrade.astype(float)
under_alg_df.finalgrade = under_alg_df.finalgrade.astype(float)

# Calculate grade percent
alg_df["gradepercent"] = alg_df.finalgrade/alg_df.rawgrademax
under_alg_df["gradepercent"] = under_alg_df.finalgrade/under_alg_df.rawgrademax

# Select only the key columns
alg_df = alg_df[["itemid","userid","gradepercent"]]
under_alg_df = under_alg_df[["itemid","userid","gradepercent"]]

# Create csvs
alg_df.to_csv("data/mid-step-alg-grades-per-user.csv", index=False)
under_alg_df.to_csv("data/mid-step-under-alg-grades-per-user.csv", index=False)
############################################################################
