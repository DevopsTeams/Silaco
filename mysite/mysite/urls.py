from django.conf.urls import url

from mysite.views import MyView

urlpatterns = [
    url(r'^hello/$', MyView.as_view(), name='my-view'),
]

