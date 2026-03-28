from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    all_Person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_Person})

def about(request):
    return render(request, "about.html")

def form(request):
    return render(request, 'form.html')

def contact(request):
    return HttpResponse("<h1>ติดต่อ 68115415 ณัฐวัสส์ ปริญญาประเสริฐ</h1>")