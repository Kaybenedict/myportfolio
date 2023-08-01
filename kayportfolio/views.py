from django.shortcuts import render
from .models import Contact

# Create your views here.


def index(request):
    contact1 = Contact()
    contact1.id=0
    contact1.mobile= '+234 810 743 7398'
    contact1.email = 'kayodaadetifa@gmail.com'
    return render(request,'index.html',{'contact':contact1})

