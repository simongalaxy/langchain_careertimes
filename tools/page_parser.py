from bs4 import BeautifulSoup


# filter text after "Apply Now".
def filter_text_by_keyword(texts: str, keyword: str) -> str:
    
    count = 0
    list = texts.split("\n")
    for i, item in enumerate(list):
        # print(f"{i}: {item}")
        if keyword in item:
            count = i
            filtered_texts = "\n".join(list[:count-1])
            break
        
    return filtered_texts


# Filter with BeautifulSoup
def filter_content(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # You can target specific containers:
    main_content = soup.find("div", {"id": "jd__desc"})
    texts = main_content.get_text(separator="\n", strip=True)
    
    filtered_texts = filter_text_by_keyword(texts=texts, keyword="Apply Now")
    
    return filtered_texts