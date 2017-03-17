## Installing and Running

### Essential Dependencies

- python 3
- django 1.9

Check if django 1.9 is installed

`$ python -m django version`

If the result is `1.9.1`, then you're all set.

If not, run this command:

`$ pip install -r requirements.txt`

### Other Dependencies
None so far.

### Running

* To get the server running, download the code and extract it (or pull it)

* In any console, navigate to the top directory of the project. There
should be a file called manage.py in the folder.

* Then start the server by running the command in cmd:

```
cd PiedPiper
$ python manage.py runserver 8000
```

You can now access the server at http://127.0.0.1:8000

## USAGE
Input artist's name in the homepage's form, and submit the form.

`Ex: ed sheeran`

* Data from Apple's API is loaded in the homepage from a POST request to url: `/artist/<ed sheeran>`
   
    - http://127.0.0.1:8000/api/artist/ed%20sheeran
    
    - Internally makes a call to: `https://itunes.apple.com/search?term=ed+sheeran&entity=musicTrack`


* Retrieve details about a particular track `/details/<track-id>`

    - ex: http://127.0.0.1:8000/details/858518134
    
    - Internally makes a call to: `https://itunes.apple.com/lookup?id=858518134`

