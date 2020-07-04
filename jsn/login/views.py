from django.shortcuts import render,redirect
from django.http import HttpResponse
from registration.models import Registration
from login.models import Login,Resetpassword

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
            login_mail(context)
            
        else:
            return render(request,'login.html')
    return render(request,'otp.html',context)

def login_mail(context):
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

def forget(request):
    return render(request,'forget.html')

def sendResetotp(request):
    if request.method == "POST":  
        emailid=request.POST.get('emailid','')
        password=request.POST.get('password','')
        cpassword=request.POST.get('cpassword','')
        #id=request.POST.get('id','')
        #print(emailid,password)
        try:
            if(password==cpassword):
                Registrations=Registration.objects.get(emailid=emailid)
                #print(Registrations_E.emailid)
                o=random.randrange(100000,999999)
                otp=str(o)
                print(otp)  
                Resetpass=Resetpassword(emailid=emailid,password=password,otp=otp,activeotp=True)
                Resetpass.save()
                context={'otp':otp,'emailid':emailid}
                resetpass_mail(context)
                print("yes yes")
                return render(request,'resetpassotp.html',context)
            else:
                return render(request,'forget.html')
            
        except:
            return redirect('login')
def resetpass_mail(context):
    subject = "OTP FOR RESET PASSWORD FROM JAN SAMSYA NIAVARAN"  
    msg=""
    html_message = loader.render_to_string(
            'sendresetpassotp.html',
            {          
                
                'otp':context['otp']
            }
        )    
    to      = context['emailid']  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to],html_message=html_message)  
    

def resetpassword(request):
    emailid=request.POST.get('emailid','')
    otp=request.POST.get('otp','')
    print(emailid)
    Resetpass=Resetpassword.objects.get(emailid=emailid)

    
    if(Resetpass.activeotp==True and Resetpass.otp==otp):
        Registrations=Registration.objects.get(emailid=emailid)
        Logins=Login.objects.get(emailid=emailid)

        Registrations.password=Resetpass.password
        Logins.password=Resetpass.password
        Registrations.save()
        Logins.save()
        Resetpass.activeotp=False
        time=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        #print(time)
        Resetpass.lastchange=str(time)
        Resetpass.save()
        
        subject = "Reset password detected"  
        html_message = loader.render_to_string(
            'resetpassdetect.html',
            {          
                
                'lastchange':Resetpass.lastchange
            }   
        )
        msg=""

    
        to      = emailid  
        res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to],html_message=html_message)  
    
        msg="Reset password succesfully"
        return HttpResponse(msg)
    else:
        context={'emailid':emailid}
        return render(request,'otp.html',context)
