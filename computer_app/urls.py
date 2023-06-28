from django.urls import path
from .views import ComputersListView, ComputerCreateView, ComputerUpdateView

urlpatterns = [
    path('', ComputersListView.as_view(), name='home'),
    path('add-computer/', ComputerCreateView.as_view(), name='add-computer'),
    path('computer/<int:pk>/update/', ComputerUpdateView.as_view(), name='update-computer'),
]
