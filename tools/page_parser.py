from bs4 import BeautifulSoup


# Filter with BeautifulSoup
def filter_content(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Example: keep only article text, drop nav/ads/scripts.
    for tag in soup(["script", "style", "nav", "footer", "aside"]):
        tag.decompose()

    # You can target specific containers:
    main_content = soup.find("div", {"class": "jd__main"}) or soup.body
    text = main_content.get_text(separator="\n", strip=True)
    
    return text