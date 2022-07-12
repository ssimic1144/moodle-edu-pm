# Process mining on Moodle dataset

## Purpose

The main purpose of this project is to discover and analyse business process
in a higher education institution based on students and professors interactions 
with Moodle LMS.

## Steps taken

### 1. step

To preform any kind of analysis, the first step is to create datasets, in csv 
format, from database logs. In later steps, the before mentioned datasets will
be utilized to create process traces. To this end, two courses were selected.
Since database logs contain numerous attributes, only handfull of key attributes
are required to create sufficient process traces. Key attributes for each course
(trace) are events taken, time and the resource who executed specific event.
