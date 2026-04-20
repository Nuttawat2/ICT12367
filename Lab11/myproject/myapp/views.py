from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person

def index(request):
    all_Person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_Person})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        # รับข้อมูลจากฟอร์ม
        name = request.POST.get("name")
        age = request.POST.get("age")
        # บันทึกลงฐานข้อมูล
        Person.objects.create(
            name=name,
            age=age
        )
        # redirect กลับหน้าแรก
        return redirect("/")
    else:
        return render(request, 'form.html')

def contact(request):
    return HttpResponse("<h1>ติดต่อ 68115415 ณัฐวัสส์ ปริญญาประเสริฐ</h1>")