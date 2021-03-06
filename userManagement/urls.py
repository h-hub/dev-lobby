from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url('signup/', views.signup, name='signup'),
    url('account_activation_sent', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
        name='activate'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
