from django.urls import path
from .views import HomePageView,SnackListView, SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('home/',HomePageView.as_view(),name='home'),
    path('snack/<pk>',SnackDetailView.as_view(),name='snack'),
]
