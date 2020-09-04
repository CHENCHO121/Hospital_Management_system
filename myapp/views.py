from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Doctor,Patient,Appointment


def index(request):
    doc=Doctor.objects.count()
    pat = Patient.objects.count()
    appoint = Appointment.objects.count()
    if not request.user.is_staff:
        return redirect('/admin_login')
    context={"doc":doc,"pat":pat,"appoint":appoint}
    return render(request, 'index.html',context)


def contact(request):
   return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def admin_login(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
                return redirect('/')
            else:
                error = "yes"
        except:
            error = "yes"
    context = {"error": error}
    return render(request, 'admin_login.html', context)


def logout_admin(request):
    logout(request)
    return redirect('/admin_login')

def view_doctor(request):
    doctor=Doctor.objects.all()
    context={"doctor":doctor}
    return render(request,'view_doctor.html',context)

def view_patient(request):
    patient=Patient.objects.all()
    context={"pat":patient}
    return render(request,'view_patient.html',context)

def view_appointment(request):
    appoint=Appointment.objects.all()
    context={"appoint":appoint}
    return render(request,'view_appointment.html',context)

def add_doctor(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        special= request.POST['special']
        try:
            Doctor.objects.create(name=name,mobile=mobile,special=special)
            error="no"
        except:
            error="yes"

    context = {"error": error}
    return render(request,'add_doctor.html',context)

def add_patient(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        address= request.POST['address']
        try:
            Patient.objects.create(name=name,mobile=mobile,gender=gender,address=address)
            error="no"
        except:
            error="yes"

    context = {"error": error}
    return render(request,'add_patient.html',context)

def add_appointment(request):
    error = ""
    doc1 = Doctor.objects.all()
    pat1 = Patient.objects.all()
    if request.method == 'POST':
        doctor = request.POST['doctor']
        patient = request.POST['patient']
        date1 = request.POST['date1']
        time1= request.POST['time1']
        doc=Doctor.objects.filter(name=doctor).first()
        pat = Patient.objects.filter(name=patient).first()
        try:
            Appointment.objects.create(doctor=doc,patient=pat,date1=date1,time1=time1)
            error="no"
        except:
            error="yes"

    context = {
        "error": error,"doctor":doc1,"pat":pat1
    }
    return render(request,'add_appointment.html',context)

def delete_doctor(request,pk):
    item = Doctor.objects.get(pk=pk)
    item.delete()
    return redirect('/view_doctor')

def delete_patient(request,pk):
    item = Patient.objects.get(pk=pk)
    item.delete()
    return redirect('/view_patient')

def delete_appointment(request,pk):
    item = Appointment.objects.get(pk=pk)
    item.delete()
    return redirect('/view_appointment')

def edit_doctor(request,pk):
    data = Doctor.objects.get(pk=pk)
    error = ""
    try:
        if request.method == "POST":
            name = request.POST["name"]
            mobile = request.POST["mobile"]
            special = request.POST["special"]

            data.name = name
            data.mobile = mobile
            data.special = special

            data.save()
            error = "no"
            return redirect('/view_doctor')
    except:
        error="yes"

    context = {
        "data": data,
        "error": error
    }
    return render(request, 'edit_doctor.html', context)

def edit_patient(request,pk):
    data = Patient.objects.get(pk=pk)
    error = ""
    try:
        if request.method == "POST":
            name = request.POST["name"]
            gender=request.POST["gender"]
            mobile = request.POST["mobile"]
            address = request.POST["address"]

            data.name = name
            data.gender=gender
            data.mobile = mobile
            data.address = address

            data.save()
            error = "no"
            return redirect('/view_patient')
    except:
        error="yes"

    context = {
        "data": data,
        "error": error
    }
    return render(request, 'edit_patient.html', context)
