from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import csv, io
from .models import courseData


# Create your views here.
def index(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        if (username is not None and password is not None):
            
            user = auth.authenticate(username=username,password=password)

            if (user is not None):
                auth.login(request,user)
                return redirect('/home')       
            else:
                messages.error(request, "incorrect username or password!!!")
                return redirect('/login')
        else:
            messages.error(request, "All fields are mandatory")
            return redirect('/login')
    
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username,first_name=first_name, last_name=last_name,password=password,email=email)
        user.save()
        return redirect('/login')

def home(request):
    user1 = User.objects.get(username="jay")
    print(user1.email)
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/getLoginPage/')
def secret(request):
    return render(request, 'secret.html')

def about(request):
    return render(request, 'about.html')

# add decorator to restrict access to this page only to faculty group
@login_required(login_url='/getLoginPage/')
def upload_data(request):
    if request.method == 'POST':
        yr = request.POST['year']
        sm = request.POST['semester']
        csv_file = request.FILES.get('csvFile', False)
        data = csv_file.read().decode('UTF-8')
        string = io.StringIO(data)
        next(string)
        next(string)
        reader = csv.reader(string)
        for row in reader:
            new_row = []
            for x in row[1:]:
                if x == '-':
                    new_row.append(0)
                else:
                    new_row.append(int(x))
            courseData.objects.create(course_code = row[0], year = yr, sem = sm, grade_AA=new_row[0], grade_AP=new_row[1], grade_AB=new_row[2], grade_BB=new_row[3], grade_BC=new_row[4], grade_CC=new_row[5], grade_CD=new_row[6], grade_DD=new_row[7], grade_AU=new_row[8], grade_DX=new_row[9], grade_FF=new_row[10], grade_FR=new_row[11], grade_II=new_row[12], grade_NP=new_row[13], grade_PP=new_row[14], grade_S=new_row[15], grade_XX=new_row[16], total=new_row[17])
        messages.success(request, "File uploaded successfully")
        return redirect('/home')        
    else:
        group = request.user.groups.get()
        if group.name == 'faculty':
            return render(request, 'upload.html')
        else:
            messages.error(request, "You are not authorized to access this page")
            return redirect('/home')
    