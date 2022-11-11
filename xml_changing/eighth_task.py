from xml.etree.ElementTree import ElementTree
from bs4 import BeautifulSoup


def change_img_png(tree: ElementTree, bs_data: BeautifulSoup, output):
    """Changing <image> tag name format «.jpg => .png»"""

    root = tree.getroot()

    for img in root.iter('image'):
        img.attrib['name'] = f"{img.attrib['name'][:-4]}.png"

    if '/' in output:
        *_, file_name = output.split('/')
    elif '\\' in output:
        *_, file_name = output.split('\\')
    tree.write(f'xml_result/{file_name}', encoding='utf-8')
