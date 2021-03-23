#!/usr/bin/env python3
"""
This script will pull in remote jobs and
then load them into a SQL table remote_jobs
"""


def refresh_remote(jobs=""):
    import MySQLdb

    """
    First we will connect to our database dB
    Next we set up a cursor to access the database with
    Finally we clear out any data in the table from the last
    time we ran the script.
    """
    dB = MySQLdb.connect("localhost", "root", "root", "BoomTown")
    cursor = dB.cursor()
    cursor.execute("TRUNCATE TABLE remote_jobs");

    """
    From our other script getRemoteJobs we have a list of
    job objects (dicts), we will cycle through this one job at
    a time.
    """
    for job in jobs:
        """
        The first thing we do is set a number of placeholdes according to
        dict length this is so we can fill in the values later
        Next we set the columns equal to a string made up of all
        the keys in ouf job dict
        Finally we add our columns and our placeholders to a premade SQL
        statement
        """
        placeholders = ', '.join(['%s'] * len(job))
        columns = ', '.join(job.keys())
        sql = "INSERT INTO remote_jobs (%s) VALUES (%s)" % (columns,
                                                            placeholders)
        """
        VLS will be a list of values that will take the place of our
        placeholders
        We will cycle through our job dict values and make sure there are no
        non-ascii characters as this can break our MySQLdb parser.
        If we hit a non ASCII string or empty string we'll count it as a None.
        it would be good to fix this in a future version as this is not a good
        or fair solution going with english/arabic alphabet only.
        """

        vls = []
        for v in job.values():
            try:
                str(v).encode(encoding='utf-8').decode('ascii')
                if str(v) == "" or v is None:
                    v = None
                else:
                    v = str(v)
            except UnicodeDecodeError:
                v = None
            vls.append(v)

        """
        Finally we use our premade SLQ statment and the values
        as a tuple to push everything to the DB and commit to
        make sure we get there.
        """
        cursor.execute(sql, tuple(vls))
        dB.commit()

    dB.close()

    print("All done with remote jobs table")


def refresh_ok():
    """
    A script to read a CSV file and put the
    data into a SQL table
    """
    import csv
    import MySQLdb
    """
    First we will connect to our database dB
    Next we set up a cursor to access the database with
    Finally we clear out any data in the table from the last
    time we ran the script.
    """
    dB = MySQLdb.connect("localhost", "root", "root", "BoomTown")
    cursor = dB.cursor()
    cursor.execute("TRUNCATE TABLE ok_jobs");
    mycursor = dB.cursor()
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
                job_link = row[4]
                comp_loc = row[6].split('in ')
                company = comp_loc[0].replace('at ', '')
                location = comp_loc[1]
                line_count += 1
                val = (str(title), str(company), str(location), str(job_link))
                mycursor.execute(sql, val)
                dB.commit()
    dB.close()
    print("All {} rows read".format(line_count))

if __name__ == '__main__':
    """
    This will be our main guard which will import
    gaurd our methods for dropping and refreshing the
    tables in the SQL DB
    """
    from getRemoteJobs import remote_jobs_get

    """
    First we'll need to get remote jobs via the API
    call to remotework, then we will send the data
    as a list of dicts to refresh_remote to be put
    into a SQL table
    """
    remote_jobs = remote_jobs_get()
    refresh_remote(remote_jobs)
    refresh_ok()
    print("BoomTown jobs tables refreshed")
