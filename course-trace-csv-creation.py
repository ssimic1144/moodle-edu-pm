import pandas as pd

raw_data_dir = "../../Downloads/csv-mdl-dir"

courses = "mdl_course.csv"

courses_df = pd.read_csv(raw_data_dir+"/"+courses)

# Category 16 is the correct one 
fipu_courses = courses_df[courses_df.category==16]

# Take all AI courses
ai_courses = fipu_courses[fipu_courses.fullname.str.contains("Umj")]

#Algorithms course
alg_courses = fipu_courses[fipu_courses.fullname.str.contains("algoritmi i st")]

# Convert unix timestamp to datetime
ai_courses["timecreated"] = pd.to_datetime(ai_courses["timecreated"], unit="s")
alg_courses["timecreated"] = pd.to_datetime(alg_courses["timecreated"], unit="s")

# Get correct ids for courses
print(ai_courses[["id","timecreated"]])
print(alg_courses[["id", "fullname", "timecreated"]])


big_stuff = "mdl_logstore_standard_log.csv"

# Get first 100 rows
#big_df = pd.read_csv(raw_data_dir+"/"+big_stuff, nrows=100)
# Find wanted keys
#print(big_df.keys())

# Helper lists
ai_2019_stuff = list()
alg_2019_stuff = list()

chunksize = 10**6

with pd.read_csv(raw_data_dir+"/"+big_stuff, chunksize=chunksize) as reader:
    for chunk in reader:
        ai_2019_stuff.append(chunk[chunk.courseid == 4988])
        print("AI :", len(ai_2019_stuff))
        alg_2019_stuff.append(chunk[chunk.courseid == 5002])
        print("Alg :", len(alg_2019_stuff))

# Create DFs
ai_df = pd.concat(ai_2019_stuff)
alg_df = pd.concat(alg_2019_stuff)

# Take only the needed columns
ai_df = ai_df[["courseid","eventname","timecreated","userid"]]
alg_df = alg_df[["courseid","eventname","timecreated","userid"]]

# Convert unix timestamp to datetime
ai_df["timecreated"] = pd.to_datetime(ai_df["timecreated"], unit="s")
alg_df["timecreated"] = pd.to_datetime(alg_df["timecreated"], unit="s")

# Create csvs
ai_df.to_csv("data/ai.csv", index=False)
alg_df.to_csv("data/alg.csv", index=False)
