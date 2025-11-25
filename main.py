from tools.job_urls_scraper import fetch_job_search_data, get_job_info
from tools.job_ad_page_render import render_page
from tools.page_parser import filter_content
from tools.extract_job_data_llm import job_data_extractor

from pprint import pprint

import os
from dotenv import load_dotenv

load_dotenv()


# main program.
def main():

    # load environment variables.
    OLLAMA_EXTRACTION_MODEL = os.getenv("OLLAMA_EXTRACTION_MODEL")
    print(f"Using Ollama extraction model: {OLLAMA_EXTRACTION_MODEL}")
    extractor = job_data_extractor(model_name=OLLAMA_EXTRACTION_MODEL)

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

        upper_limit = 10

        # render the job advertisement page and then parse the information from job ad page.
        for i, dict in enumerate(job_dicts):
            if i < upper_limit:
                url = dict["jobUrl"]
                html = render_page(url=url)
                html_text = filter_content(html=html)
                extracted_data = extractor.extract_job_data(job_content=html_text)
                
                print(f"Job No.: {i+1}")
                print(f"Raw data from rendered webpage: {html_text}")
                print("Extracted job data:")
                pprint(extracted_data)
                print("---------------------------------------------------------\n")

    return


# main program entry point.
if __name__ == "__main__":
    main()
