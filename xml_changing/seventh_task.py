from xml.etree.ElementTree import ElementTree
from bs4 import BeautifulSoup


def change_img_id(tree: ElementTree, bs_data: BeautifulSoup, output):
    """Changing <image> id attribute in a reverse order"""

    img_id_lst = [img['id'] for img in bs_data.find_all('image')]

    root = tree.getroot()

    for ix, img in enumerate(root.iter('image')):
        img.attrib['id'] = str(img_id_lst[-1 - ix])

    *_, file_name = output.split('/')
    tree.write(f'xml_result/{file_name}', encoding='utf-8')
