#!/usr/bin/env python3

def remote_jobs_get():
    import json
    import requests

    base_url = 'https://remotive.io/api/remote-jobs?'
    company = "" #this can be included as: 'company_name=<name>' to search for a specific company
    search = "" #this can be included as: 'search=front%20end' to look for a specific keyword(s)
    limit = "limit=50" #this can be included as: 'limit=5' to limit results
    category = "category=software-dev" #this can be included in the url as: 'category=software-dev' to search a catagory
    """
    The catagories that we can use are a specific list as follows:
    {"id": 19, "name": "Software Development", "slug": "software-dev"},
    {"id": 18, "name": "Customer Service", "slug": "customer-support"},
    {"id": 21, "name": "Design", "slug": "design"},
    {"id": 28, "name": "Marketing", "slug": "marketing"},
    {"id": 30, "name": "Sales", "slug": "sales"},
    {"id": 23, "name": "Product", "slug": "product"},
    {"id": 33, "name": "Business", "slug": "business"},
    {"id": 24, "name": "Data", "slug": "data"},
    {"id": 25, "name": "DevOps / Sysadmin", "slug": "devops"},
    {"id": 26, "name": "Finance / Legal", "slug": "finance-legal"},
    {"id": 27, "name": "Human Resources", "slug": "hr"},
    {"id": 29, "name": "QA", "slug": "qa"},
    {"id": 31, "name": "Teaching", "slug": "teaching"},
    {"id": 32, "name": "Writing", "slug": "writing"},
    {"id": 35, "name": "Medical / Health", "slug": "medical-health"},
    {"id": 22, "name": "All others", "slug": "all-others"}

    We can make buttons of these to select and in each instance we use the slug
    """

    # r is our main request and will hold the response code
    r = requests.get(base_url + limit)

    # payload holds the json payload from requests
    payload = r.json()

    # jobs is the specific list of jobs from the payload
    jobs = payload['jobs']

    # i will be an iterator to go through the jobs list
    i = 0

    # cleaned_jobs is a list of job dicts with only the basic relevant data
    cleaned_jobs = []

    # desired info are the things we want out of the raw jobs data, description is something we should add but it is a mess of html
    desired_info = ['title','url','category','job_type',
                    'company_name', 'publication_date',
                    'candidate_required_location']

    # print the response code to be sure
    print(r)

    #loop through the raw jobs list and gather the necessary info into a new dict and append to cleaned jobs
    while(i < len(jobs)):
        job_data = payload['jobs'][i]
        job = {}
        for k, v in job_data.items():
            if k in desired_info:
                job[k] = v
        cleaned_jobs.append(job)
        i += 1

#    for item in cleaned_jobs:
#        print(item)

    return (cleaned_jobs)

if __name__ == '__main__':
    remote_jobs_get()
