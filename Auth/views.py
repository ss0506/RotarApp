from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, EmailUpdateForm
from .models import Club, Account
from django.shortcuts import redirect
import csv

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
@login_required
def profile(request):
    if request.method == 'POST' :
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance= Club.objects.filter(account=request.user).first())
        e_form = EmailUpdateForm(request.POST, instance=request.user)
        if e_form.is_valid():
            e_form.save()
        if p_form.is_valid():
            p_form.save()
        return redirect('profile')
    else :
        p_form = ProfileUpdateForm(instance= Club.objects.filter(account=request.user).first())
        e_form = EmailUpdateForm(instance=request.user)

    return render(request, 'Auth/updateProfile.html',{'title':'Profile','tab':'profile','pform':p_form,'eform':e_form,'profile':request.user.club})

def createAccounts(request):
    csvFile='credentials.csv'
    with open(csvFile, encoding='utf8') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            try :
                p = Account(username=row['username'],
                name=row['Name2'],
                is_club = True,
                rotaryId = row['Club ID'])
                p.set_password(row['password'])
                p.save()

            except Exception as e:
                pass
                print(e)

    return redirect('login')

def email(request):
        try :
            subject = 'Testing'
            message = 'Thank you for being a part of this testing. Maine socha, time mila hai, benegit kar sakte hai, to mail ka feature add kar diya.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['pcpatil410@gmail.com','rtrmadhupimprikar@gmail.com']
            send_mail( subject, message, email_from, recipient_list )
            return redirect('home')
        except Exception as e: 
            print(e)