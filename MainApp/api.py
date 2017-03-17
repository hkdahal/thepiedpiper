from django.shortcuts import HttpResponse

from .search_api import SearchAPI

import glob
import json
import ntpath
import os

import MainApp

DATA_DIRECTORY = '/saved-data/'


def get_data(request, name):
    """
    Given an artist's name, get the search result and dump it to json
    :param request: request object
    :param name: artist's name
    :return: HttpResponse as a json object
    """
    result = SearchAPI().search_artist(name)
    return HttpResponse(json.dumps(result), content_type="application/json")


def load_saved_data(request, artist):
    """
    Given an artist's name, look up
    :param request: request object
    :param artist: artist's name
    :return: HttpResponse as a json object
    """
    file = os.path.dirname(MainApp.__file__) + DATA_DIRECTORY + artist + '.json'

    # Reading data back
    with open(file, 'r') as f:
        data = json.load(f)
    return HttpResponse(json.dumps(data), content_type="application/json")


def lookup_saved_files():
    """
    Lookup saved data files in 'saved-data' directory and return the file names,
    which are artists' names
    :return: file(artist) names
    """
    path = os.path.dirname(MainApp.__file__)
    file_paths = glob.glob(path+DATA_DIRECTORY+'*.json')
    return [path_leaf(path).split('.')[0] for path in file_paths]


def path_leaf(path):
    """
    Given a path, extract file name without extension
    :param path: a file path
    :return: filename without extension
    """
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def handle_uploaded_file(file, file_name):
    """
    Save an uploaded file with given filename to 'saved-data' directory
    :param file: uploaded file
    :param file_name: file name
    :return: True if saved, or False if any error
    """
    try:
        file_path = os.path.dirname(
            MainApp.__file__) + DATA_DIRECTORY + file_name
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return True
    except:
        return False



