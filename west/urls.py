from django.conf.urls import patterns,include,url

urlpatterns = [
    url(r'^$', 'west.views.first_page'),
]