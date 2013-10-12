from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'index.html')

# def base_example(request):
# 	return render(request, 'base_example.html')