from django.conf.urls import url
from .views import GrabnGoDetailView,GrabnGoListView,grabngo_detail_view

urlpatterns = [
  url(r'^$',GrabnGoListView.as_view(), name='list'),
  url(r'^(?P<pk>\d+)/$', GrabnGoDetailView.as_view(), name='detail'),
]
