#!/usr/bin/env python3
"""
A script to read a CSV file and put the
data into a SQL table
"""

import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="BoomTown"
)
mycursor = mydb.cursor()
sql = "INSERT INTO ok_jobs (title, company, location, job_link) VALUES (%s, %s, %s, %s)"

with open('developer_v2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        elif '<header class="card__header">' in row[2]:
            line_count += 1
        else:
            title = row[3]
            job_link= row[4]
            comp_loc = row[6].split('in')
            company = comp_loc[0].replace('at ', '')
            location = comp_loc[1]
            line_count += 1
            val = (str(title), str(company, str(location), str(job_link))
            mycursor.execute(sql, val)
    print("All {} rows read".format(line_count))
