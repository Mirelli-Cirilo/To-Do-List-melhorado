from django.shortcuts import render

def loginPage(request):
    return render(request, 'base/home.html')

