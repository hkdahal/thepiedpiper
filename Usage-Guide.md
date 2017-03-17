# Usage Guide Usage 
[Usage Guide](http://127.0.0.1:8000/usage-guide)
 
##Project Question
result table
- Enter Artist's name in the box, and click Search to look up search results.
- This can also be done by clicking on any saved artist
- it takes the artist's name, and makes a call to Apple's API
the returned json data is being processed to display the table
the table has pagination and you can `'save result'` and `'download result'`

demo: [127.0.0.1:8000/](http://127.0.0.1:8000)

##save result
- saving a result means saving processed json result as a file `<artist_name>.json` in `MainApp/saved-data` directory
- a data is saved after clicking on 'save result' and click on 'yes'
- with an ajax call, animation for downloading and saving is shown
it quickly adds the name of the artist to the saved_artists list

##download result
- just clicking on `'download result'`
- downloading a result means allowing a user to download the processed json
- result so that user can upload it later
- demo: [/api/artist/jack johnson](http://127.0.0.1:8000/api/artist/jack%20johnson)
- json: [/api/artist/jack johnson](http://127.0.0.1:8000/api/artist/jack%20johnson)


##upload result
- url -> `/load-file`
- click on browse and look for .json file
- then click upload (this button is disabled till a file is selected)
soon as upload is complete, it redirects users to home page with the result table
- demo: [/load-file](http://127.0.0.1:8000/load-file)

##track details
- ==> url -> `/details/<track_id>`
- ==> click on any track shown in the result table
- calls Apple's API with the selected track id
- shows details of selected track including artwork and preview audio
- demo: [/details/858518134](http://127.0.0.1:8000/details/858518134)