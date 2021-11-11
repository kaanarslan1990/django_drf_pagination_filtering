from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Student
from .forms import StudentForm
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
import json

# def home(request):
#     return HttpResponse("hello world !!!! ")

#!------------------------------------------ API Views
def manuel_api(request):
    data = {
        "first_name": "victor",
        "last_name": "H",
        "number" : 234
    }
    return JsonResponse(data)

def student_list_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_count = Student.objects.count()
        student_list = []
        for student in students:
            student_list.append({
                "first_name" : student.first_name,
                "last_name" : student.last_name,
                "number" : student.number
            })
        data = {
            'students':student_list,
            'student_count': student_count
        }
        return JsonResponse(data)

def student_list_api_2(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_count = Student.objects.count()
        student_data = serialize("python", students)
        data = {
            'students':student_data,
            'student_count': student_count
        }
        return JsonResponse(data)
    
@csrf_exempt
def student_add_api(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        student_data = {}
        student_data['first_name'] = post_body.get('first_name')
        student_data['last_name'] = post_body.get('last_name')
        student_data['number'] = post_body.get('number')
        # validation required
        student = Student.objects.create(**student_data)
        data = {
            'message': f"Student {student.last_name} added successfully"
        }
        return JsonResponse(data, status=201)
    
    
#!--------------------------------------------- Template Views

def home_page(request):
    return render(request, 'fscohort/home.html')

def student_list(request):
    students  = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'fscohort/student_list.html', context)

def student_add(request):
    form = StudentForm() # boş form render edeceğiz
    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form' : form
    }
    return render(request, 'fscohort/student_add.html', context)

def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)

def student_delete(request, id):
    # student = get_object_or_404(Student, id=id)
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("list")
    return render(request, "fscohort/student_delete.html") 
    
def student_update(request, id):
    student =Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form':form,
        }
    return render(request, 'fscohort/student_update.html', context)