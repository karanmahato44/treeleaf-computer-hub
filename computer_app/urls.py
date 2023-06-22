from django.urls import path
from . import views as computer_app_views
from .views import ComputerBrandsListView, ComputerSpecsDetailView

urlpatterns = [
    path('', ComputerBrandsListView.as_view(), name='home'),
    path('brand/<int:pk>', ComputerSpecsDetailView.as_view(), name='brand-detail')
]
