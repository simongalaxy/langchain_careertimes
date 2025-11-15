from tools.job_urls_scraper import fetch_job_search_data, get_job_info
from tools.job_ad_page_render import render_page
from tools.page_parser import filter_content

from pprint import pprint


# function to display list item.
def show_list_items(items: list) -> None:

    for i, item in enumerate(items):
        print(f"No. {i}:")
        print(item)
        print("_____________________________________")

    return




# main program.
def main():

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

        upper_limit = 20

        # render the job advertisement page and then parse the information from job ad page.
        for i, dict in enumerate(job_dicts):
            if i < upper_limit:
                url = dict["jobUrl"]
                html = render_page(url=url)
                content = filter_content(html=html)
                print("-------------------------------------------------------------\n")
                print(f"url: {url}")
                print(content)
                print("--------------------------------------------------------------\n")
    
        

        

    return


# main program entry point.
if __name__ == "__main__":
    main()
