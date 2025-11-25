from tools.job_urls_scraper import fetch_job_search_data, get_job_info
from tools.job_ad_page_render import render_page
from tools.page_parser import filter_content
from tools.render_extract_page import JobExtractor

from pprint import pprint

import os
from dotenv import load_dotenv

load_dotenv()


# main program.
def main():

    # load environment variables - Ollama model name for job data extraction.
    OLLAMA_EXTRACTION_MODEL = os.getenv("OLLAMA_EXTRACTION_MODEL")
    extractor = JobExtractor(model_name=OLLAMA_EXTRACTION_MODEL)

    # chat loop
    while True:

        # search by keyword in careertimes.com.hk.
        question = input("Please input the search keyword in careertimes (type 'q' for quit): ")
        if question.lower() == 'q':
            break
        
        # fetch the search results from careertimes.com.hk and then get the job information.
        results = fetch_job_search_data(keyword=question)
        job_dicts = get_job_info(jobs=results["data"]["jobs"])
        print(f"Total No. of job scraped: {len(job_dicts)}\n")

        job_ad_urls = [job["jobUrl"] for job in job_dicts]

        for url in job_ad_urls:
            print(f"Processing job ad page: {url}")

           
            pprint(job_extracted_data)
           
    return


# main program entry point.
if __name__ == "__main__":
    main()
