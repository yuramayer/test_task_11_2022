from bs4 import BeautifulSoup


def statistics_by_figures(bs_data: BeautifulSoup) -> dict:
    """Summing and grouping the figures by categories ('boxes', 'polygons', etc)"""

    fig_d = {}

    for img in bs_data.find_all('image'):
        for tag in img.contents:
            if tag.name:
                fig_d[tag.name] = fig_d[tag.name] + 1 if tag.name in fig_d else 1

    return fig_d
