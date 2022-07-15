import pandas as pd

raw_data_dir = "../../Downloads/csv-mdl-dir"

courses = "mdl_course.csv"

courses_df = pd.read_csv(raw_data_dir+"/"+courses)

# Category 16 is the correct one 
fipu_courses = courses_df[courses_df.category==16]

# Algorithms course
alg_courses = fipu_courses[fipu_courses.fullname.str.contains("algoritmi i st")]

# Undergrad Algorithms course
under_alg_courses = fipu_courses[fipu_courses.fullname.str.contains("Stru")]

# Convert unix timestamp to datetime
alg_courses["timecreated"] = pd.to_datetime(alg_courses["timecreated"], unit="s")
under_alg_courses["timecreated"] = pd.to_datetime(under_alg_courses["timecreated"], unit="s")

# Get correct ids for courses
print(alg_courses[["id", "fullname", "timecreated"]])
print(under_alg_courses[["id", "fullname", "timecreated"]])

# AI = 4988
# ALG grad = 5002
# ALG undergrad = 4720
# E-learning = 4991
# MAT 1 = 5822
# Baze 1 = 5509
# Osnove IKT = 4934
# Mob = 4993
# IOT = 4998


big_stuff = "mdl_logstore_standard_log.csv"

# Get first 100 rows
#big_df = pd.read_csv(raw_data_dir+"/"+big_stuff, nrows=100)
# Find wanted keys
#print(big_df.keys())


# Helper lists
alg_stuff = list()
under_alg_stuff = list()

chunksize = 10**6

with pd.read_csv(raw_data_dir+"/"+big_stuff, chunksize=chunksize) as reader:
    for chunk in reader:
        alg_stuff.append(chunk[chunk.courseid == 5002])
        under_alg_stuff.append(chunk[chunk.courseid == 4720])
        print(len(alg_stuff))

# Create DFs
alg_df = pd.concat(alg_stuff)
under_alg_df = pd.concat(under_alg_stuff)

# Convert unix timestamp to datetime
alg_df["timecreated"] = pd.to_datetime(alg_df["timecreated"], unit="s")
under_alg_df["timecreated"] = pd.to_datetime(under_alg_df["timecreated"], unit="s")

# Boundary date
boundary_date = pd.date_range(start="2021-10-1",end="2021-10-2",periods=1)

# Limit DF based on boundary date
alg_df = alg_df[alg_df.timecreated > boundary_date[0]]
under_alg_df = under_alg_df[under_alg_df.timecreated > boundary_date[0]]

# Take only the needed columns
alg_df = alg_df[["courseid","eventname","timecreated","userid"]]
under_alg_df = under_alg_df[["courseid","eventname","timecreated","userid"]]

#Ending filters

# Remove non student ids
alg_df = alg_df[~alg_df.userid.isin([77,72,2,0])]
under_alg_df = under_alg_df[~under_alg_df.userid.isin([77,72,2,0])]

# Cosmetic stuff for activities
alg_df["eventname"] = alg_df.eventname.str.split("\\").str[-1]
under_alg_df["eventname"] = under_alg_df.eventname.str.split("\\").str[-1]


# Drop attendance from dataset
#alg_df = alg_df[alg_df.eventname != "attendance_taken_by_student"]
#under_alg_df = under_alg_df[under_alg_df.eventname != "attendance_taken_by_student"]

# Create csvs
alg_df.to_csv("data/alg.csv", index=False)
under_alg_df.to_csv("data/under_alg.csv", index=False)
