from bs4 import BeautifulSoup
from general_statistics import get_figures_set


def unmarked_images(bs_data: BeautifulSoup) -> int:
    """Counting all the <images> without any figures (<box>, <polygon>, etc)"""

    figures = get_figures_set(bs_data)

    return sum(1 for img in bs_data.find_all('image')
               if all([not img.find(figure) for figure in figures]))