from bs4 import BeautifulSoup

def count_figures(bs_data: BeautifulSoup) -> int:
    """Counting all the figures in the BeautifulSoup XML object"""

    fig_count = 0

    for img in bs_data.find_all('image'):
        for tag in img.contents:
            if tag.name:
                fig_count += 1

    return fig_count
