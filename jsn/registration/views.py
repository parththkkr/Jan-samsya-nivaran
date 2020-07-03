from django.shortcuts import render,redirect
from django.http import HttpResponse  
from jsn import settings  
from django.core.mail import send_mail  
from registration.models import Registration
from django.template import loader

# Create your views here.
def reg(request): 
    return render(request,'registration.html',{'display':'none'})

def saveReg(request):
    
    try:
        if request.method == "POST":  

            firstname=request.POST.get('firstname','')
            lastname=request.POST.get('lastname','')
            username=request.POST.get('username','')
            emailid=request.POST.get('emailid','')
            password=request.POST.get('password','')
            rpassword=request.POST.get('rpassword','')
            city=request.POST.get('city','')
            state=request.POST.get('state','')
            zipcode=request.POST.get('zip','')
            
            context={'firstname':firstname,'lastname':lastname,'emailid':emailid,'password':password,'city':city,'zip':zipcode,'state':state,'username':username}
            
            try:
                Registrations=Registration.objects.get(emailid=emailid,username=username)
                print(Registrations)
                print(username)
                print('hi')
                return redirect('/login/login')
            except:
                None

            try:
                Registrations=Registration.objects.get(username=username)
                print(Registrations.username)
                print(username)
                    
                if(Registrations.username==username):
                    print(Registrations.username)
                    print(username)
                    return render(request,'registration.html',{'display':""})
            except:
                print("hiii")
                None

            if password==rpassword:
                Registrations=Registration(firstname=firstname,lastname=lastname,
                username=username,emailid=emailid,password=password,city=city,
                state=state,zipcode=zipcode)
                Registrations.save()
                mail(context)
                return redirect('/login/login')
            else:
                return render(request,'registration.html',context) 
    except:
            return render(request,'registration.html',context) 

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
    