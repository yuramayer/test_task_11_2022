import os
from bs4 import BeautifulSoup
from xml.etree import ElementTree
from classes_statistics.fourth_task import statistics_by_classes
from figure_statistics.fifth_star_task import statistics_by_figures
from general_statistics import marked_images, unmarked_images, count_figures, max_min_image
from general_statistics.first_task import count_images
from setuptools import logging
import logging

from xml_changing.eighth_task import change_img_png
from xml_changing.ninth_task import change_img_path
from xml_changing.seventh_task import change_img_id


def script_start():
    if path_isnot_empty('xml_files'):
        path = 'xml_files'
        files_lst = get_files_from_path(path)
    else:
        files_lst = get_path()

    command = get_command()

    if command == 1:
        start_first_command(files_lst)

    elif command == 2:
        start_second_command(files_lst)

    elif command == 3:
        start_third_command(files_lst)

    elif command == 4:
        start_fourth_command(files_lst)



def path_isnot_empty(path):
    dir = os.listdir(path)
    if dir:
        return True


def get_path() -> list:
    n = input('How many files? ')
    path_lst = list()
    if n.isdigit():
        path_lst = [input(f'Type the absoulte path of #{i+1} file: ') for i in range(int(n))]
        return path_lst
    else:
        print('Only integers, please!')
        return get_path()

def get_files_from_path(path):
    dir = os.listdir(path)
    return [f'{path}/{file}' for file in dir]


def get_command() -> int:
    command = input('Please, type the script number!'
                    '\n\nThe first script: 1'
                    '\nThe second script: 2'
                    '\nThe third script: 3'
                    '\nThe fourth script: 4\n')
    if command.isdigit() and command in ('1', '2', '3', '4'):
        return int(command)
    else:
        print('Command id should be digit from 1 to 4!')
        return get_command()



def start_first_command(files_lst):

    for ix, file in enumerate(files_lst):

        ix += 1

        print(f'General statistics for #{ix} file with path: {file}')

        try:
            with open(file, 'rb') as f:
                data = f.read()
            bs_data = BeautifulSoup(data, 'xml')

            file_the_images = count_images(bs_data)
            print(f'All the images for the #{ix} file: {file_the_images}')
            file_marked_images = marked_images(bs_data)
            print(f'All the marked images for the #{ix} file: {file_marked_images}')
            file_unmarked_images = unmarked_images(bs_data)
            print(f'All the unmarked images for the #{ix} file: {file_unmarked_images}')
            file_count_figures = count_figures(bs_data)
            print(f'All the figures for the #{ix} file: {file_count_figures}')
            max_image, min_image = max_min_image(bs_data)
            print(f'The max image for the #{ix} file:\n'
                  f'- count: {max_image[0]}\n'
                  f'- file_name: {max_image[1]}\n'
                  f'- file_width: {max_image[2]}\n'
                  f'- file_height: {max_image[3]}')
            print(f'The min image for the #{ix} file:\n'
                  f'- count: {min_image[0]}\n'
                  f'- file_name: {min_image[1]}\n'
                  f'- file_width: {min_image[2]}\n'
                  f'- file_height: {min_image[3]}\n')
            print('-'*75)

        except Exception as err:

            print(f'ERROR: The #{ix} file with the path: {file} is corrupted.'
                  f'\nPlease, check your XML-file.')
            logging.exception(err)


def start_second_command(files_lst):

    for ix, file in enumerate(files_lst):

        ix += 1

        print(f'Classes statistics for #{ix} file with path: {file}')

        try:
            with open(file, 'rb') as f:
                data = f.read()
            bs_data = BeautifulSoup(data, 'xml')

            classes_dict = statistics_by_classes(bs_data)
            print(f'All the figures by classes for the #{ix} file:')
            for key, value in classes_dict.items():
                print(f'Class "{key}" - {value} figures')

            print('-' * 75)

        except Exception as err:

            print(f'ERROR: The #{ix} file with the path: {file} is corrupted.'
                  f'\nPlease, check your XML-file.')
            logging.exception(err)


def start_third_command(files_lst):

    for ix, file in enumerate(files_lst):

        ix += 1

        print(f'Figures statistics for #{ix} file with path: {file}')

        try:
            with open(file, 'rb') as f:
                data = f.read()
            bs_data = BeautifulSoup(data, 'xml')

            classes_dict = statistics_by_figures(bs_data)
            print(f'Figures by categories for the #{ix} file:')
            for key, value in classes_dict.items():
                print(f'Category "{key}" - {value} figures')

            print('-' * 75)

        except Exception as err:

            print(f'ERROR: The #{ix} file with the path: {file} is corrupted.'
                  f'\nPlease, check your XML-file.')
            logging.exception(err)



def start_fourth_command(files_lst):

    for ix, file in enumerate(files_lst):

        ix += 1

        print(f'XML changing for #{ix} file with path: {file}\n')

        try:
            with open(file, 'rb') as f:
                data = f.read()
            bs_data = BeautifulSoup(data, 'xml')
            tree = ElementTree.parse(file)

            print(f'Reversing id\'s in the #{ix} XML file.\n'
                  f'The result is in the "xml_files" directory.\n')

            change_img_id(tree, bs_data, file)

            print(f'Changing .img to .png in the #{ix} XML file.\n'
                  f'The result is in the "xml_files" directory.\n')

            change_img_png(tree, bs_data, file)

            print(f'Changing name tags in the #{ix} XML file.\n'
                  f'The result is in the "xml_files" directory.\n')

            change_img_path(tree, bs_data, file)

            print('-' * 75)

        except Exception as err:

            print(f'ERROR: The #{ix} file with the path: {file} is corrupted.'
                  f'\nPlease, check your XML-file.')
            logging.exception(err)



script_start()


