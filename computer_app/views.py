from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import  ListView, DetailView, CreateView, UpdateView
from .models import ComputerBrands, ComputerSpecification, Computer

# def home(request):
#     context = {
#         'brands': ComputerBrands.objects.all()
#     }
#     return render(request, 'computer_app/home.html', context)

class ComputersListView(ListView):
    model = Computer
    context_object_name = 'computer_list'
    # template_name = 'computer_app/home.html'
    # ordering = ['-id']


class ComputerCreateView(CreateView):
    model = Computer
    fields = ['computer', 'computer_code', 'quantity', 'unit_rate']


class ComputerUpdateView(UpdateView):
    model = Computer
    fields = ['computer', 'computer_code', 'quantity', 'unit_rate']
