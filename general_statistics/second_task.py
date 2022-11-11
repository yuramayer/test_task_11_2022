from general_statistics import get_figures_set
from bs4 import BeautifulSoup

def marked_images(bs_data: BeautifulSoup) -> int:
    """Counting all the <images> with figures (<box>, <polygon>, etc)"""

    figures = get_figures_set(bs_data)

    return sum(1 for img in bs_data.find_all('image')
               if any([img.find(figure) for figure in figures]))
