from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView


# Create your views here.


def upload(request):
	if request.method == 'POST':
		upload_file = request.FILES['document']
		print(upload_file.name)
		print(upload_file.size)
		return render(request, 'kcs_layout.html')