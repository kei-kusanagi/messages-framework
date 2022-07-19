from django.contrib import messages
from django.shortcuts import render

def index(request):
    if request.method== 'POST':
        messages.success(request, 'Profile details updated.', extra_tags='notification')

    return render(request, 'core/index.html')
