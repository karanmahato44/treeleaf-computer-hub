from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from .models import ComputerBrands, ComputerSpecification


# def home(request):
#     context = {
#         'brands': ComputerBrands.objects.all()
#     }
#     return render(request, 'computer_app/home.html', context)


class ComputerBrandsListView(ListView):
    model = ComputerBrands
    template_name = 'computer_app/home.html'
    context_object_name = 'brands'
    # ordering = ['-id']


class ComputerSpecsDetailView(DetailView):
    model = ComputerSpecification
