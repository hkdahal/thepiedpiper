from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import ArtistForm
from .search_api import SearchAPI

import json
import MainApp.api as my_api


def index(request):
    """
    Homepage that handles sending and showing search result table
    :param request: request object
    :return: page either with an empty form or with a search result table
    """
    url, term = None, None

    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            term = form.cleaned_data['name']  # artist's name
            url = '/api/artist/'+term         # setup url that gives json
    else:
        form = ArtistForm()

    saved_artists = my_api.lookup_saved_files()  # get saved artists' names

    return render(request, 'MainApp/pages/index.html',
                  {
                      'form': form,
                      'url': url,
                      'term': term,
                      'saved_artists': saved_artists,
                      'current': 'Homepage'
                   })


def details(request, id):
    """
    Provides details of a selected track
    :param request: request object
    :param id: trackId for selected track
    :return: page that shows track's details
    """
    data = SearchAPI().lookup_id(id)
    return render(request, 'MainApp/pages/details.html', {'data': data})


def save_data(request, term):
    """
    Saves json data for a given term to '/saved-data' directory
    :param request: request object
    :param term: an artist's name
    :return: just a response
    """
    data = SearchAPI().search_artist(term)

    # Writing JSON data
    with open('MainApp'+my_api.DATA_DIRECTORY+term+'.json', 'w') as f:
        json.dump(data, f)

    return HttpResponse('Saved ' + term + ' file.')


def show_saved_result(request, artist):
    """
    Given an artist's name, initialize the form with artist's name
    Has a url to make proper call to see saved search result for an artist
    :param request: request object
    :param artist: artist's name
    :return: similar to index
    """
    form = ArtistForm(initial={'name': artist})
    return render(request, 'MainApp/pages/index.html',
                  {
                      'form': form,
                      'url': '/api/saved/'+artist,
                      'saved_artists': my_api.lookup_saved_files(),
                      'saved_data': True,
                      'current': 'Homepage'
                   })


def load_file(request):
    """
    GET: Provide an empty form to browse and upload json file
    POST: Handle uploaded file by saving to proper directory,
          and redirect to show the result data
    :param request: request object
    :return: upload page or result table page
    """
    if request.method == 'POST':
        file = request.FILES.getlist('my_file')[0]
        file_name = request.POST['file_name']
        if my_api.handle_uploaded_file(file, file_name):
            # redirect to result page --> (show_saved_result function)
            return HttpResponseRedirect('/show/'+file_name)
    else:
        return render(request, 'MainApp/pages/upload_file.html',
                      {'current': 'LoadFile'})


def usage_guide(request):
    """
    Show usage guide on how certain actions can be done in this website
    :param request: request object
    :return: usage guide page
    """
    return render(request, 'MainApp/pages/usage_guide.html',
                  {'current': 'UsageGuide'})

