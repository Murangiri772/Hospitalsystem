from tempfile import template

from django.shortcuts import render,redirect,get_object_or_404
from hospitalapp.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')
def starter(request):
    return render(request,'starter-page.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def departments(request):
    return render(request,'departments.html')
def doctors(request):
    return render(request,'doctors.html')
def appointment(request):
    if request.method == "POST":
        Myappoitnment=Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department=request.POST['department'],
            doctor =request.POST['doctor'],
            message = request.POST['message'],

        )
        Myappoitnment.save()
        return redirect('/show')
    else:
        return render(request, 'appointment.html')
def contact(request):
    if request.method == "POST":
        mycontact= Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )


        mycontact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')
def show(request):
    all = Appointment.objects.all()
    return render(request, 'show.html',{'all':all})
def view(request):
    all = Contact.objects.all()
    return render(request, 'view.html',{'all':all})


def delete(request,id):
    deletedappointment=Appointment.objects.get(id=id)
    deletedappointment.delete()
    return redirect('/show')
def edite(request,id):
    editeinfo = get_object_or_404(Appointment,id=id)
    if request.method == 'POST':
        editeinfo.name = request.POST.get('name')
        editeinfo.email = request.POST.get('email')
        editeinfo.phone = request.POST.get('phone')
        editeinfo.date = request.POST.get('date')
        editeinfo.department = request.POST.get('department')
        editeinfo.doctor = request.POST.get('doctor')
        editeinfo.message = request.POST.get('message')
        editeinfo.save()
        return redirect('/show')
    else:
        return render(request,'edite.html',{'editeinfo':editeinfo})









