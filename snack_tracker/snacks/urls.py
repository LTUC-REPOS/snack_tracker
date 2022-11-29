from django.urls import path
from .views import HomePageView,SnackListView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('home/',HomePageView.as_view(),name='home'),
]
