from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from django.http import HttpResponse   #เพิ่มHttpResponseเข้ามาคือคำสั่งตอบกลับ
from myapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    all_person = Person.objects.all()
    return render(request,"index.html",{"all_person": all_person})     
#เมื่อ request เข้ามาทาง index ก็จะแสดงข้อมูลใน index.html

def about(request):
    return render(request, "about.html")
#เมื่อ request เข้ามาทาง about ก็จะแสดงข้อมูลใน about.html 

def form(request):
    if request.method == "POST":
        #รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        
        #บันทึกข้อมูล
        person = Person.objects.create(
            name=name, 
            age=age
        )
        person.save()
        messages.success(request, "บันทึกข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/")
    else :
        return render(request, "form.html")
#เมื่อ request เข้ามาทาง form ก็จะแสดงข้อมูลใน form.html 

def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request,"อัพเดทเรียบร้อย")
    # ดึงข้อมูลมนุษย์โลกที่ต้องการแก้ไข
        return redirect("/")
    else:
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html", {"person":person})
    
def delete(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/")
