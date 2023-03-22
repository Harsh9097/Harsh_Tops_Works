from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from chairmanapp.models import *

# Create your views here.

def societymember_profile(request):
    if "email" in request.session:
         uid = User.objects.get(email = request.session['email'])      
         sid = Societymember.objects.get(user_id = uid)
         if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']

            sid.firstname = firstname
            sid.lastname = lastname

            if "picture" in request.FILES:
                sid.pic = request.FILES['picture']

            sid.save()
            context = {
                        'uid' : uid,
                        'sid' : sid,
                    }
            return render(request,"societymemberapp/profile.html",context)
         else:
            context = {
                        'uid' : uid,
                        'sid' : sid,
                    }
            return render(request,"societymemberapp/profile.html",context)  
    else:
        return redirect("login")

def societymember_change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)

        if request.POST:
            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']

            if uid.password == currentpassword:
                uid.password = newpassword
                uid.save()
                return redirect("logout")
            else:
             
             context = {
                'uid' : uid,
                'sid' : sid,
            }
            return render(request,"societymember/profile.html",context)
        else:
            context = {
                'uid' : uid,
                'sid' : sid,
            }
            return render(request,"societymember/profile.html",context)

def view_notice_society(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       sid = Societymember.objects.get(user_id = uid)
       nall = Notice.objects.all()
       context = {
                'uid' : uid,
                'sid' : sid,
                'nall' : nall,
            }
       return render(request,"societymemberapp/notice-list.html",context)

def view_notice_society_details(request,pk):
    if "email" in request.session:
       print("--------->PK",pk)
       uid = User.objects.get(email = request.session['email']) 
       sid = Societymember.objects.get(user_id = uid)
       notice_id = Notice.objects.get(id = pk)

       nall = NoticeViewDetails.objects.filter(user_id = uid,notice_id = notice_id)
       if len(nall) == 0:
            nid = NoticeViewDetails.objects.create(user_id = uid,notice_id = notice_id)

       notice = Notice.objects.filter(id = pk)
       context = {
                'uid' : uid,
                'sid' : sid,
                'notice' : notice,
            }
       return render(request,"societymemberapp/notice-details.html",context)


def view_event_society(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       sid = Societymember.objects.get(user_id = uid)
       eall = Event.objects.all()
       context = {
                'uid' : uid,
                'sid' : sid,
                'eall' : eall,
            }
       return render(request,"societymemberapp/event-list.html",context)

def view_event_society_details(request,pk):
    if "email" in request.session:
       print("--------->PK",pk)
       uid = User.objects.get(email = request.session['email']) 
       sid = Societymember.objects.get(user_id = uid)
       event_id = Event.objects.get(id = pk)

       eall = EventViewDetails.objects.filter(user_id = uid,event_id = event_id)
       if len(eall) == 0:
            eid = EventViewDetails.objects.create(user_id = uid,event_id = event_id)

       event = Event.objects.filter(id = pk)
       context = {
                'uid' : uid,
                'sid' : sid,
                'event' : event,
            }
       return render(request,"societymemberapp/event-details.html",context)

       
def add_complaint(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       sid = Societymember.objects.get(user_id = uid)

       if request.POST:
          coid = Complaint.objects.create(
            user_id = uid,
            title = request.POST['title'],
            description = request.POST['description'],
          )

          call = Complaint.objects.all()
          context = {
                'uid' : uid,
                'sid' : sid,
                'call' : call,
            }
          return render(request,"societymemberapp/complaint-list.html",context)
       else:
        context = {
                'uid' : uid,
                'sid' : sid,
            }
        return render(request,"societymemberapp/add-complaint.html",context)

    else:
        return redirect("login")
    
def view_complaint(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       sid = Societymember.objects.get(user_id = uid)
       call = Complaint.objects.all()
       context = {
                'uid' : uid,
                'sid' : sid,
                'call' : call,
            }
       return render(request,"societymemberapp/complaint-list.html",context)

def view_complaint_details(request,pk):
    if "email" in request.session:
       print("--------->PK",pk)
       uid = User.objects.get(email = request.session['email']) 
       sid = Societymember.objects.get(user_id = uid)
       complaint = Complaint.objects.filter(id = pk)
       context = {
                'uid' : uid,
                'complaint' : complaint,
            }
       return render(request,"societymemberapp/complaint-details.html",context)