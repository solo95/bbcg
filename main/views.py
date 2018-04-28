from django.shortcuts import render
from django.views import generic
from .models import Complements

# Create your views here.


	
class DetailView(generic.ListView):
	template_name = 'main/index.html'
	def get_queryset(self):
		data = Complements.objects.all()
		return data