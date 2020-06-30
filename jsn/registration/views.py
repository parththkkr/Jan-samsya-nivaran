from django.shortcuts import render,redirect
from django.http import HttpResponse  
from jsn import settings  
from django.core.mail import send_mail  
from registration.models import Registration
from django.template import loader

# Create your views here.
def reg(request):
    return render(request,'registration.html')

def saveReg(request):

    if request.method == "POST":  

        firstname=request.POST.get('firstname','')
        lastname=request.POST.get('lastname','')
        username=request.POST.get('username','')
        emailid=request.POST.get('emailid','')
        password=request.POST.get('password','')
        rpassword=request.POST.get('Rpassword','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zip','')

        context={'firstname':firstname,'lastname':lastname,'emailid':emailid,'password':password,'city':city,'zip':zipcode,'state':state,'username':username,'id':id}
        
    
        if password==rpassword:
            Registrations=Registration(firstname=firstname,lastname=lastname,
            username=username,emailid=emailid,password=password,city=city,
            state=state,zipcode=zipcode)
            Registrations.save()
            mail(context)
        else:
             return render(request,'login.html',context) 
    
    return redirect('/login/login') 

def mail(context):
    subject = "Registration"  
    
    html_message = loader.render_to_string(
            'mail.html',
            {          
                'firstname':context['firstname'],
                'lastname':context['lastname']    
            }
        )
    msg=""

    
    to      = context['emailid']  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to],html_message=html_message)  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)      