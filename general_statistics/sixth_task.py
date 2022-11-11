from dataclasses import dataclass
from general_statistics import get_image_list
from bs4 import BeautifulSoup

def max_min_image(bs_data: BeautifulSoup) -> tuple:
    """Finding the max & min image by square (width * height)"""

    images_lst = get_image_list(bs_data)

    images_lst.sort(key=lambda x: x.square, reverse=True)

    max_images_count = sum(i.square == images_lst[0].square for i in images_lst)
    min_images_count = sum(i.square == images_lst[-1].square for i in images_lst)

    return ((max_images_count, images_lst[0].name, images_lst[0].width, images_lst[0].height),
            (min_images_count, images_lst[-1].name, images_lst[-1].width, images_lst[-1].height))
