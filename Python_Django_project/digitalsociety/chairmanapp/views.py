
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from random import *
from django.core.mail import send_mail


# Create your views here.

"""
models.objects.get(fieldname = htmlname) = fetch data from database(model)

uid = models.object.get()
uid.fieldname = newvalue
uid.save() : for update data


# to store data in model(similar like insert query)
uid = model.objects.create(fieldname=pythonname,fieldname=pythonname)

# fetch all data from model(without any condition)

var = models.object.all()


# fetch all data from model but condition wise

filter() = queryset

var = models.objects.filter()

"""

def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "chairman":
            cid = Chairman.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'cid' : cid,
                }
            return render(request,"chairmanapp/index.html",context)

        else: 
            sid = Societymember.objects.get(user_id = uid)
            context = {
                        'uid' : uid,
                        'sid' : sid,
                    }
            return render(request,"societymemberapp/index.html",context) 
    else:
        return redirect("login")

def login(request):
    if "email" in request.session:
        return redirect('home')
    else:
        if request.POST:
            pemail = request.POST['email']
            ppassword = request.POST['password']
            print("------->email",pemail)
            try:
                uid = User.objects.get(email = pemail)
                if uid.password == ppassword:
                    if uid.role == "chairman":
                        cid = Chairman.objects.get(user_id = uid)

                        print("firstname",cid.firstname)
                        print("SIGN IN BUTTON PRESS-----> ",uid)
                        print(uid.role)
                        print(uid.password)
                        request.session['email'] = uid.email # session store
                        return redirect("home")

                    else:
                        sid = Societymember.objects.get(user_id = uid)
                        print("firstname",sid.firstname)
                        print("SIGN IN BUTTON PRESS-----> ",uid)
                        print(uid.role)
                        print(uid.password)
                        request.session['email'] = uid.email
                        #print("-----> puttting data in session",request.session['email'])
                        # context = {
                        #      'uid' : uid,
                        #      'sid' : sid,
                        # }
                        # return render(request,"societymemberapp/index.html",context)
                        return redirect("home")
                        #print("SOCIETY MEMBER")
                else:
                    context = {
                        'emsg' : "invalid password"
                    }
                print("something went wrong")
                return render(request,"chairmanapp/login.html",context)
            except:
                 context = {
                         'emsg' : "invalid email address"
                 }
                 print("something went wrong")
                 return render(request,"chairmanapp/login.html",context)
        else:
           print("===> login page refresh")
           return render(request,"chairmanapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect("login")
    else:
        return redirect("login")

def chairman_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            
            cid.firstname = firstname
            cid.lastname = lastname
            if "picture" in request.FILES:
                cid.pic = request.FILES['picture']
                
            cid.save()
            
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context)
        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context) 
    else:
       return redirect("login") 
def chairman_change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        if request.POST:
            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']

            if uid.password == currentpassword:
                uid.password = newpassword
                uid.save()
                return redirect("logout")
            else:
                pass
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context)
        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context)

def add_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            blockno = request.POST['blockno']
            contactno = request.POST['contactno']
            # city = request.POST['city']
            occupation = request.POST['occupation']
            nooffamilymembers = request.POST['nooffamilymembers']
            dateofbirth = request.POST['dateofbirth']
            owner = request.POST['owner/rent']
            vehicledetails = request.POST['vehicledetails']
            bloodgroup = request.POST['bloodgroup']
            

            l1 = ['asd782d','sd784','sd7342c','8dj43','s78sd432','9a8s12']
            password = email[4:7]+contactno[3:7]+choice(l1)

            uid = User.objects.create(email = email,password = password,role = "societymember")
            sid = Societymember.objects.create(user_id = uid,firstname = firstname,lastname = lastname,contact_no = contactno,block_no = blockno,occupation = occupation,no_of_familymembers = nooffamilymembers,dob = dateofbirth,vehicle_details = vehicledetails,blood_group = bloodgroup,house_ownership = owner)

            if sid:
                send_mail("Digital Society Password","Your password is : "+str(password),"urvashikanala@gmail.com",[email])
                msg = "successfully societymember created !! plz check gmail account or password"
                context = {
                     'msg' : msg,
                     'uid' : uid,
                     'cid' : cid,
                }
                return render(request,"chairmanapp/add-member.html",context)
        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/add-member.html",context)
    else:
        return redirect("login")

def all_societymembers(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)

       sall = Societymember.objects.all()
       context = {
                'uid' : uid,
                'cid' : cid,
                'sall' : sall,
            }
       return render(request,"chairmanapp/all-societymembers.html",context)
    

def add_notice(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)

       if request.POST:
          nid = Notice.objects.create(
            user_id = uid,
            title = request.POST['title'],
            description = request.POST['description'],
          )

          nall = Notice.objects.all()
          context = {
                'uid' : uid,
                'cid' : cid,
                'nall' : nall,
            }
          return render(request,"chairmanapp/notice-list.html",context)
       else:
        context = {
                'uid' : uid,
                'cid' : cid,
            }
        return render(request,"chairmanapp/add-notice.html",context)

    else:
        return redirect("login")

def view_notice(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)
       nall = Notice.objects.all()
       context = {
                'uid' : uid,
                'cid' : cid,
                'nall' : nall,
            }
       return render(request,"chairmanapp/notice-list.html",context)

def view_notice_details(request,pk):
    if "email" in request.session:
       print("--------->PK",pk)
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)
       notice = Notice.objects.filter(id = pk)
       context = {
                'uid' : uid,
                'cid' : cid,
                'notice' : notice,
            }
       return render(request,"chairmanapp/notice-details.html",context)

def societyspecification_profile(request,pk):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)
       sid = Societymember.objects.get(id = pk)

       context = {
                'uid' : uid,
                'cid' : cid,
                'sid' : sid,
                
            }
       return render(request,"chairmanapp/specific_profile.html",context)
    
def forgot_password(request):
    if request.POST:
        email = request.POST['email']
        otp = randint(1111,9999)

        try:
            uid = User.objects.get(email = email)
            uid.otp = otp
            uid.save()
            send_mail("Forgot password","Your otp is "+str(otp),"urvashikanala@gmail.com",[email])
            context = {
                'email' : email
            }
            return render(request,"chairmanapp/change-password.html",context)
        except:
            context = {
                'emsg' : "Invalid email address"
            }
            return render(request,"chairmanapp/forgot-password.html",context)
    return render(request,"chairmanapp/forgot-password.html")

def change_password(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']

        uid = User.objects.get(email = email)
        if str(uid.otp) == otp:
            if newpassword == confirmpassword:
                uid.password = newpassword
                uid.save()
                context = {
                    'email' : email,
                  'smsg' : "Password successfully changed" 
                }
                return render(request,"chairmanapp/login.html",context)
            else:
                emsg = "Invalid password"
                context = {
                  'email' : email,
                  'emsg' : emsg 
                }
                return render(request,"chairmanapp/change-password.html",context)
        else:
            emsg = "Invalid otp"
            context = {
                  'email' : email,
                  'emsg' : emsg 
                }
            return render(request,"chairmanapp/change-password.html",context)
        
def add_event(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)

       if request.POST:
          nid = Event.objects.create(
            user_id = uid,
            title = request.POST['title'],
            description = request.POST['description'],
          )

          eall = Event.objects.all()
          context = {
                'uid' : uid,
                'cid' : cid,
                'eall' : eall,
            }
          return render(request,"chairmanapp/event-list.html",context)
       else:
        context = {
                'uid' : uid,
                'cid' : cid,
            }
        return render(request,"chairmanapp/add-event.html",context)

    else:
        return redirect("login")
    
def view_event(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)
       eall = Event.objects.all()
       context = {
                'uid' : uid,
                'cid' : cid,
                'eall' : eall,
            }
       return render(request,"chairmanapp/event-list.html",context)

def view_event_details(request,pk):
    if "email" in request.session:
       print("--------->PK",pk)
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)
       event = Event.objects.filter(id = pk)
       context = {
                'uid' : uid,
                'cid' : cid,
                'event' : event,
            }
       return render(request,"chairmanapp/event-details.html",context)


def view_complaint_chairman(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)
       call = Complaint.objects.all()
       context = {
                'uid' : uid,
                'cid' : cid,
                'call' : call,
            }
       return render(request,"chairmanapp/complaint-list.html",context)

def view_complaint_chairman_details(request,pk):
    if "email" in request.session:
       print("--------->PK",pk)
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)
       complaint_id = Complaint.objects.get(id = pk)

       call = ComplaintViewDetails.objects.filter(user_id = uid,complaint_id = complaint_id)
       if len(call) == 0:
            coid = ComplaintViewDetails.objects.create(user_id = uid,complaint_id = complaint_id)

       complaint = Complaint.objects.filter(id = pk)
       context = {
                'uid' : uid,
                'cid' : cid,
                'complaint' : complaint,
            }
       return render(request,"chairmanapp/complaint-details.html",context)



def add_maintainance(request):
     if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)

       if request.POST:
            title = request.POST['title']
            amount = request.POST['amount']
            duedate = request.POST['duedate']

            sall = Societymember.objects.all()
            for i in sall:
                sid = Societymember.objects.get(id= i.id)
                print("=====>",sid )
                mid = Maintainance.objects.create(user_id = uid, 
                                                  member_id = sid,
                                                  title = title,
                                                  amount = amount,
                                                  duedate = duedate)
                                                
        
            context = {
                'status':"Successfully added",
                'uid':uid,
                'cid':cid,
            }
            return render(request,"chairmanapp/add-maintainance.html",context)        

       context={
                'uid':uid,
                'cid':cid,
       }
       return render(request,"chairmanapp/add-maintainance.html",context)        

def all_maintainance(request):
      if "email" in request.session:
       uid = User.objects.get(email = request.session['email']) 
       cid = Chairman.objects.get(user_id = uid)

       mall = Maintainance.objects.all()

       total_amount = 0
       for i in mall:
         total_amount += int(i.amount)
       
      context={
                'uid':uid,
                'cid':cid,
                'mall':mall,
                'total_amount': total_amount,
       }
      return render(request,"chairmanapp/all-maintainance.html",context)        

      
    
  
