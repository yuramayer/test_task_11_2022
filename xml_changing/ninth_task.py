from xml.etree.ElementTree import ElementTree
from bs4 import BeautifulSoup


def change_img_path(tree: ElementTree, bs_data: BeautifulSoup, output):
    """Removing the path to the file from <image> tag name"""

    root = tree.getroot()

    for img in root.iter('image'):
        img_name = img.attrib['name']
        *_, path = img_name.split('/')
        img.attrib['name'] = path

    if '/' in output:
        *_, file_name = output.split('/')
    elif '\\' in output:
        *_, file_name = output.split('\\')
    tree.write(f'xml_result/{file_name}', encoding='utf-8')
