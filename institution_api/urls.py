from django.contrib import admin
from django.urls import path
from .views import FindProviderView, ListProviderView, SaveProviderView

urlpatterns = [
    #path('save_provider', SaveProviderView.as_view(), name='save_provider'),
    #path('list_provider', ListProviderView.as_view(), name='list_provider'),
    #path('find_provider/<int:id>', FindProviderView.as_view(), name='find_provider')
]
