from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import TrackListView, TrackYearListView

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('data/', TrackListView.as_view(), name='track-data'),
    path('data/<int:year>/', TrackYearListView.as_view(), name='track-year')

    ]