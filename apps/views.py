from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.conf import settings

# Create your views here.
def Home(request):
    return render(request, "apps/home.html")

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = UserAccount.objects.filter(email=email)
        if user:
            user = UserAccount.objects.get(email=email)
            encodepass = user.password
            user_email = user.email
            user_id = user.id
            user_name = user.name
            
            decodepass = check_password(password, encodepass)

            if user_email == email and decodepass == True:
                request.session['user_id']=user_id
                request.session['user_email']=email
                request.session['user_name']=user_name
                messages.success(request,"Login success")
                return redirect('/login')
            else:
                messages.warning(request, 'Invalid credentials')
                return redirect('/login')
        else:
            messages.warning(request, "User does't exists.")
            return redirect('/login')
    else:
        # Session already login
        if request.session.has_key('user_id'):
            return redirect('/')
        else:
            return render(request, 'apps/login.html')

#============= Register ========================
def Register(request):
    if request.session.has_key('user_id'):
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST['name']
            mobile = request.POST['mobile']
            email = request.POST['email']
            password = request.POST['password']
            
            e_password = make_password(request.POST['password'])
            
            if UserAccount.objects.filter(email=email).exists():
                messages.warning(request, "Email already exists")
                return redirect('register')
            else:
                user = UserAccount.objects.create(name=name,mobile=mobile,email=email,password=e_password)
                user.save()
                messages.success(request, "User created successfully")
                return redirect('login')
        else:
            return render(request, "apps/register.html")

def Report(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        location = request.POST['location']
        incident_department = request.POST['incident_department']
        date_time = request.POST['date_time']
        incidnt_location = request.POST['incidnt_location']
        incident_severity = request.POST['incident_severity']
        suspected_cause = request.POST['suspected_cause']
        immediate_action = request.POST['immediate_action']
        incident_type = request.POST.getlist("incident_type[]")

        Incident = IncidentMaster.objects.create(user_id_id=user_id,location=location,incident_department=incident_department,date_time=date_time,incidnt_location=incidnt_location,incident_severity=incident_severity,suspected_cause=suspected_cause,immediate_action=immediate_action)
        Incident.save()
        for i in incident_type:
            incident = SubIncidentType.objects.create(user_id_id=user_id,indcident_id_id=Incident.id,incident_type=i)
            incident.save()
        messages.success(request, "Report submitted")
        return redirect('login')
    else:
        # Session already login
        if request.session.has_key('user_id'):
            return render(request, 'apps/report.html')
        else:
            return redirect('/login')
    


def Logout(request):
    del request.session['user_email']
    del request.session['user_id']
    del request.session['user_name']
    messages.success(request, "Logout Success")
    return redirect('/login')