from bs4 import BeautifulSoup


def get_classes_set(bs_data: BeautifulSoup) -> set:
    """Getting set with all the classes in the BeautifulSoup XML object"""
    page_classes = set()

    for img in bs_data.find_all('label'):
        page_classes.add(img.find('name').text)

    return page_classes
