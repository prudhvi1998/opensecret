from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

from opensecretapp.views import *
from django.conf.urls import url

app_name="opensecretapp"

urlpatterns = [
    url(r'^signup/$', SignUp.as_view(), name='signup'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout, name="logout"),
    # url(r'^password/$', change_password, name='change_password'),
    url(r'^home/$', HomeView.as_view(), name="home"),
    url(r'^viewprofile/(?P<value>\w+)/$', UserProfileView.as_view(), name="viewprofile"),
    url(r'^messages/$', MessagesListView.as_view(), name='messages'),
    url(r'^outbox/$', OutBoxListView.as_view(), name='outbox'),
    url(r'^updateprofile/(?P<pk>\d+)/$', UpdateProfileView.as_view(), name='updateprofile'),
]