from django.shortcuts import render
from django.http import HttpResponse
from registration.models import Registration
from login.models import Login
import random
import math
import datetime
from jsn import settings  
from django.core.mail import send_mail  
from django.template import loader

# Create your views here.
def login(request):
    return render(request,'login.html')

def checklogin(request):
    print("hiii")
    if request.method == "POST":  
        emailid=request.POST.get('emailid','')
        password=request.POST.get('password','')
        id=request.POST.get('id','')
        #print(emailid,password)
        Registrations_E=Registration.objects.get(emailid=emailid)
        #print(Registrations_E.emailid)
        if(Registrations_E.password==password and Registrations_E.emailid==emailid):
            o=random.randrange(100000,999999)
            otp=str(o)
            print(otp)  
            
            logins=Login(emailid=emailid,password=password,otp=otp,activeotp=True)
            logins.save()
            context={'otp':otp,'emailid':emailid}
            mail(context)
            
        else:
            return render(request,'login.html')
    return render(request,'otp.html',context)

def mail(context):
    subject = "OTP For Login into JAN SAMSYA NIAVARAN"  
    msg=""
    html_message = loader.render_to_string(
            'sendotp.html',
            {          
                
                'otp':context['otp']
            }
        )    
    to      = context['emailid']  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to],html_message=html_message)  
    
def checkotp(request):
    emailid=request.POST.get('emailid','')
    otp=request.POST.get('otp','')
    print(emailid)
    logins=Login.objects.get(emailid=emailid)

    
    if(logins.activeotp==True and logins.otp==otp):
        logins.activeotp=False
        time=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        #print(time)
        logins.lastlogin=str(time)
        logins.save()
        
        subject = "Login detected"  
        html_message = loader.render_to_string(
            'logindetect.html',
            {          
                
                'lastlogin':logins.lastlogin
            }   
        )
        msg="Your last login is done on "+logins.lastlogin+" Not done by you contact us "

    
        to      = emailid  
        res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to],html_message=html_message)  
    
        msg="login succesfully"
        return HttpResponse(msg)
    else:
        context={'emailid':emailid}
        return render(request,'otp.html',context)
        