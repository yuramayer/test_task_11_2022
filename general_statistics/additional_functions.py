from dataclasses import dataclass
from bs4 import BeautifulSoup


def get_figures_set(bs_data: BeautifulSoup) -> set:
    """Getting all the figures (<box>, <polygon>, etc) set"""
    figures = set()

    for img in bs_data.find_all('image'):
        for tag in img.contents:
            if tag.name:
                figures.add(tag.name)
    return figures


def get_image_list(bs_data: BeautifulSoup) -> list:
    """Getting list of <image> tags from BS object with tag attrs as class attributes"""
    @dataclass
    class Image:
        """<image> tag class for looping"""
        square: int
        width: int
        height: int
        image_id: str
        name: str

    return [Image(int(img['width']) * int(img['height']), int(img['width']),
                        int(img['height']), img['id'], img['name'])
            for img in bs_data.find_all('image')]
