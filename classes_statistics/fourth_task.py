from bs4 import BeautifulSoup
from classes_statistics import get_classes_set

def statistics_by_classes(bs_data: BeautifulSoup) -> dict:
    """Calculating all the figures (<box>, <polygon>, etc) by classes"""

    page_classes_set = get_classes_set(bs_data)

    cls_d = {cls: 0 for cls in page_classes_set}

    for element in bs_data.find_all('image'):
        for cl in page_classes_set:
            fig = element.find_all(attrs={'label': cl})
            if fig:
                cls_d[cl] += len(fig)

    return cls_d
