

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login



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


def delete(request,id):
    deletedcontact=Contact.objects.get(id=id)
    deletedcontact.delete()
    return redirect('/view')


def viewedit(request,id):
    vieweditinfo = get_object_or_404(Contact,id=id)
    if request.method == 'POST':
        vieweditinfo.name = request.POST.get('name')
        vieweditinfo.email = request.POST.get('email')
        vieweditinfo.subject = request.POST.get('subject')
        vieweditinfo.message = request.POST.get('message')

        vieweditinfo.save()
        return redirect('/view')
    else:
        return render(request,'viewedit.html',{'vieweditinfo':vieweditinfo})

def register(request):

    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')




def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('/home')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')









