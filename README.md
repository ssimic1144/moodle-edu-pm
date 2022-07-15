# Process mining on Moodle dataset

## Purpose

The main purpose of this project is to discover and analyse business process
in a higher education institution based on students and professors interactions 
with Moodle LMS.

### Requirements

Python requirements are as located in requirements.txt 
```
$ pip install -r requirements.txt
```

On Debian-like distributions graphviz is required for pm4py package
```
# apt install graphviz
```

## Steps taken

### 1. step

To preform any kind of analysis, the first step is to create datasets, in csv 
format, from database logs. In later steps, the before mentioned datasets will
be utilized to create process traces. To this end, two courses were selected.
Since database logs contain numerous attributes, only handfull of key attributes
are required to create sufficient process traces. Key attributes for each course
(trace) are events taken, time and the resource who executed specific event.

```
$ python course-trace-csv-creation.py
```
### 2. step

With courses selected, we can perform analysis of student grades based on the
number of times they interacted with Moodle LMS. Students are devided into 
five groups. The first group is composed of students with final grade >= 90%,
the second 80% <= final grade < 90%, the third group 65% <= final grade < 80% 
the fourth group are students with 50% <= final grade < 65% and the last group
are students who failed the course, they had final grad < 50%.

```
$ python mid-step-grade-csv-creation.py
```

```
$ python user-total-grade-csv-creation.py
```

```
$ python user-groups-csv-creation.py
```

#### 2.1. step

Before performing analysis based on the number of times students
interacted with LMS, visuzalition of different groups has been done. 
Data visualization, as one of the crucial step in every data analysis, allows 
a convenient way to observe data dispersion among different groups.

```
$ python visualizing-users-groups.py
```

#### 2.2 step

Visualizing groups interaction with LMS.

```
$ python trace-per-user-group-csv-creation.py
```

```
$ python visualizing-activity-per-user-groups.py
```

### 3. step

Process discovery per group.

```
$ python process-discovery-per-group.py
```
