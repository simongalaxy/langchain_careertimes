import requests
import json
from pprint import pprint


# fetch jobs data based on searching keyword.
def fetch_job_search_data(keyword: str) -> list[dict]:
    
    url = "https://api01.ctgoodjobs.hk/job/api/jobs/search"

    payload = json.dumps({
        "pagingInputs": {
            "page": "1",
            "pageSize": "2000",
            "pageOneSize": "2000"
        },
        "sort": 2,
        "keyword": f"{keyword}",
        "searchTypeId": "Y",
        "jobIds": [],
        "jobcatareaIds": [],
        "companyIds": [],
        "industryIds": [],
        "employmentTypeIds": [],
        "locationIds": [],
        "educationIds": [],
        "gradeIds": [],
        "channelIds": []
        })
    
    headers = {
        'Cookie': 'culture=en-US; sid=705545600',
        'Content-Type': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6,zh;q=0.5',
        'channel-id': '001',
        'content-type': 'application/json',
        'device': 'd',
        'dnt': '1',
        'lang': 'en-US',
        'login': 'false',
        'origin': 'https://jobs.ctgoodjobs.hk',
        'priority': 'u=1, i',
        'referer': 'https://jobs.ctgoodjobs.hk/jobs/LLM-jobs',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sid': '304536280',
        'user-id': 'CT_14961845_CT',
        'visitor-id': 'v20251015142620896248304'
        }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


# get the job info.
def get_job_info(jobs: list[dict]) -> list[dict]:
    
    filtered_jobs = []
    
    for job in jobs:
        dict = {
            "jobId": job["jobId"],
            "jobTitle": job["jobTitle"],
            "highlight": job["highlights"],
            "experience": job["experience"],
            "location": job["locations"],
            "salary": job["salary"],
            "jobUrl": job["url"],
            "companyId": job["companyId"],
            "companyName": job["companyName"],
            "companyUrl": job["companyUrl"],
            "publishDate": job["publishTime"]["date"]
        }
        filtered_jobs.append(dict)
        
    return filtered_jobs