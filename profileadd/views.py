from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def profile(request):
    from profileadd.read_spreadsheet_server import data
    data()
    return render(request, 'profileadd/profileform.html')
