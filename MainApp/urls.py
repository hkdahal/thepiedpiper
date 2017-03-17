from django.conf.urls import url
import MainApp.views as v
import MainApp.api as api

urlpatterns = [
    # api urls that return json objects
    url(r'^api/artist/(?P<name>[a-zA-Z\s]+)', api.get_data),
    url(r'^api/saved/(?P<artist>[a-zA-Z\s]+)', api.load_saved_data),

    url(r'^details/(?P<id>\d+)', v.details),  # details of a track
    url(r'^save/(?P<term>[a-zA-Z\s]+)', v.save_data),  # save data
    url(r'^show/(?P<artist>[a-zA-Z\s]+)', v.show_saved_result),  # show saved
    url(r'^load-file', v.load_file),  # upload file and save it
    url(r'^usage-guide', v.usage_guide),  # show usage data
    url(r'^$', v.index),  # homepage
]
