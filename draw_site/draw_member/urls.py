# draw_member/urls.py
from django.conf.urls import include, url
from .views import home,draw,history  # explicit relative import

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^draw/$', draw, name="draw"),
    url(r'^history/$', history, name="history")
]
