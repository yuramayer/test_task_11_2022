from bs4 import BeautifulSoup

def count_images(bs_data: BeautifulSoup) -> int:
    """Counting all the <images> in the BeautifulSoup XML object"""

    return len(bs_data.find_all('image'))
