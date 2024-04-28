# from _update=nonesing import send

import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from app.models import *

# create your views here.


def first(request):
    return render(request,"main_index.html")

def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        data = data[0]
        request.session['lid']=data.id
        request.session['lin'] = "1"
        if data.usertype == 'admin':
            return HttpResponse("<script>alert('login success');window.location='/adminhome'</script>")
        elif data.usertype =='worker':
                return HttpResponse("<script>alert('login success');window.location='/worker_home'</script>")
        elif data.usertype =='user':
                return HttpResponse("<script>alert('login success');window.location='/user_home'</script>")
        elif data.usertype =='pending':
                return HttpResponse("<script>alert('Your account is under verification');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('invalid');window.location='/'</script>")
    else:
            return HttpResponse("<script>alert('invalid');window.location='/'</script>")

def logout(request):
    request.session['lid']=''
    return HttpResponse("<script>alert('Logout');window.location='/'</script>")

def complaintsend(request):
    if request.session['lid'] == '':
         return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        return render(request,"admin/complaint send.html")

def complaint_view(request):
    if request.session['lid'] == '':
         return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        res =Complaint.objects.all()
        return render(request,"admin/complaint.html",{'data':res})

def admin_send_reply(request,id):
    return render(request,'admin/complaint send.html',{'id':id})

def admin_send_reply_post(request,id):
    rpl=request.POST['textarea']
    date=datetime.datetime.now().date()
    Complaint.objects.filter(id=id).update(reply=rpl,reply_date=date)
    return HttpResponse("<script>alert('send');window.location='/adminhome'</script>")

def feedbacks(request):
    if request.session['lid'] == '':
         return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        ed = feedback.objects.all()
        return render(request,"admin/feedback.html",{'data':ed})

def view_rating(request,id):
    if request.session['lid'] == '':
         return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        dg = rating.objects.filter(WORKER=id)
        return render(request,"admin/rating.html",{'data':dg})

def viewuser(request):
    if request.session['lid'] == '':
         return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        df = user.objects.all()
        return render(request,"admin/view user.html",{'data':df})

def workers(request):
    if request.session['lid'] == '':
         return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        es =worker.objects.filter(LOGIN__usertype='pending')
        return render(request,"admin/worker.html",{'data':es})

def adminhome(request):
    return render(request,"admin/admin_index.html")

def approvedworker(request):
    if request.session['lid'] == '':
         return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        es = worker.objects.filter(LOGIN__usertype='worker')
        return render(request,"admin/approved worker.html",{"data":es})

def change(request):
    if request.session['lid'] == '':
         return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        return render(request,"admin/change.html")

def change_post(request):
    oldpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    p=login.objects.filter(password=oldpassword,id=request.session['lid'])
    if p.exists():
        if newpassword==confirmpassword:
            login.objects.filter(id=p[0].id).update(password=confirmpassword)
            return HttpResponse("<script>alert('changed');window.location='/adminhome'</script>")
        else:
            return HttpResponse("mismatch")
    else:
        return HttpResponse("not found")


def Viewcategory(request):
    if request.session['lid'] == '':
         return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        res = category.objects.all()
        return render(request,"admin/view category.html",{'data':res})

def Categoryadd(request):
    if request.session['lid'] == '':
         return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        return render(request,"admin/category add.html")

def addcategory_POST(request):
    categorys =request.POST['input']
    obj = category()
    obj.name= categorys
    obj.save()
    return HttpResponse("<script>alert('category added');window.location='/Categoryadd'</script>")

def categoryupdate(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        data=category.objects.get(id=id)
        return render(request,"admin/edit_category.html",{"data":data,"id":id})


def categoryupdate_post(request,id):
    categorys = request.POST['input']
    category.objects.filter(id=id).update(name=categorys)
    return HttpResponse("<script>alert('category updated');window.location='/Viewcategory#hom'</script>")


def Approveworkers(request,id):
    login.objects.filter(id=id).update(usertype='worker')
    return HttpResponse("<script>alert('approved');window.location='/workers'</script>")

def Rejectworkers(request,id):
    login.objects.filter(id=id).update(usertype='rejected')
    return HttpResponse("<script>alert('rejected');window.location='/workers'</script>")

def categorydelete(request,id):
    category.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/Viewcategory'</script>")

######################################################################################################

def add_service(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        res=category.objects.all()
        return render(request,"worker/add service.html",{'data':res})

def add_service_post(request):
    ca=request.POST['select']
    am=request.POST['textfield']
    nam=request.POST['textfield2']
    obj=service()
    obj.CATEGORY_id=ca
    obj.amount=am
    obj.service=nam
    obj.WORKER=worker.objects.get(LOGIN=request.session['lid'])
    obj.save()

    return HttpResponse("<script>alert('added');window.location='/worker_home'</script>")


def register(request):
    return render(request,"worker/register.html")

def register_post(request):
    nm=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    experience=request.POST['textfield4']
    latitude=request.POST['textfield5']
    longitude=request.POST['textfield6']
    password=request.POST['textfield7']
    age=request.POST['textfield8']
    idproof = request.FILES['fileField']
    d=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\Mottuz\Downloads\TN\TN\app\static\images\\"+d+'.pdf',idproof)
    path='/static/images/'+d+'.pdf'

    if login.objects.filter(username=email):
        return HttpResponse("<script>alert('Email already exists');window.location='/'</script>")

    obj=login()
    obj.username=email
    obj.password=password
    obj.usertype="pending"
    obj.save()


    obj1=worker()
    obj1.name=nm
    obj1.email=email
    obj1.phone=phone
    obj1.experience=experience
    obj1.age=age
    obj1.idproof=path
    obj1.lattitude=latitude
    obj1.longitude=longitude
    obj1.LOGIN=obj
    # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    # s.starttls()
    # s.login("smartfuddonation@gmail.com", "smart@789")
    # msg = MIMEMultipart()  # create a message.........."
    # msg['From'] = "smartfuddonation@gmail.com"
    # msg['To'] = email
    # msg['Subject'] = "Your Password is"
    # body = "Your Password is:- - " + str(password)
    # msg.attach(MIMEText(body, 'plain'))
    # s.send_message(msg)
    obj1.save()


    return HttpResponse("<script>alert('Registered successfully');window.location='/'</script>")


def View_bookings(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        fd=Bookings.objects.filter(SERVICE_id=id)
        return render(request,"worker/view bookings.html",{'data':fd})

def View_category(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        res=category.objects.all()
        return render(request,"worker/view category.html",{'data':res})

# def View_payment(request):
#     se = Bookingsub.objects.filter(BOOKING__WORKER__LOGIN=request.session['lid'],BOOKING__paymentstatus='online')
#     return render(request,"worker/view payment.html",{'data':se})

def View_service(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        re=service.objects.filter(WORKER__LOGIN=request.session['lid'])
        return render(request,"worker/view service.html",{'data':re})

def Upload_works(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        return render(request,"worker/upload works.html")

def Upload_works_POST(request):
    image=request.FILES['fileField']
    details=request.POST['textfield']
    date=request.POST['textfield1']
    d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs = FileSystemStorage()
    fs.save(r"C:\Users\Mottuz\Downloads\TN\TN\app\static\images\\" + d + '.pdf', image)
    path = '/static/images/' + d + '.pdf'

    obj = work()
    obj.work_image= path
    obj.details = details
    obj.date = date
    obj.WORKER = worker.objects.get(LOGIN=request.session['lid'])
    obj.save()

    return HttpResponse("<script>alert('work uploaded');window.location='/worker_home'</script>")


def Upcoming_works(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        dt = datetime.datetime.now().strftime("%Y-%m-%d")
        data = work.objects.filter(date__gt=dt)
        print("okkkkkkk", data)
        return render(request,"worker/upcoming works.html",{"data":data})

def worker_home(request):
    return render(request,"worker/worker_index.html")

def Approvebookings(request,id):
    worker.objects.filter(id=id).update(workerstatus='approved')
    return HttpResponse("<script>alert('approved');window.location='/workers'</script>")

def Rejectbookings(request,id):
    worker.objects.filter(id=id).update(workerstatus='rejected')
    return HttpResponse("<script>alert('rejected');window.location='/workers'</script>")

def View_servicedelete(request,id):
    service.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_service'</script>")

def View_serviceupdate(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        res = category.objects.all()
        d =service.objects.get(id=id)
        return render(request,"worker/update service.html",{'data1':d,'data':res})

def update_service_post(request,id):
    ca=request.POST['select']
    am=request.POST['textfield']
    nam=request.POST['textfield']
    service.objects.filter(id=id).update(amount=am,CATEGORY=ca,service=nam)

    return HttpResponse("<script>alert('updated');window.location='/View_service'</script>")

# def view_servicedelete(request,id):

def View_uploadworks(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        res = work.objects.filter(WORKER__LOGIN_id=request.session['lid'])
        return render(request, "worker/view upload works.html", {'data': res})

def Delete_uploadworks(request,id):
    work.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_uploadworks'</script>")

def Update_uploadworks(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        h =work.objects.get(id=id)
        return render(request, "worker/update _upload works.html", {'data': h})

def Update_uploadworksPOST(request,id):

    try:
        details = request.POST['textfield']
        date = request.POST['textfield1']
        image = request.FILES['fileField']
        d = datetime.datetime.now().strftime("%y%m%d-%h%m%s")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\Mottuz\Downloads\TN\TN\app\static\images\\" + d + '.pdf', image)
        path = '/static/images/' + d + '.pdf'
        work.objects.filter(id=id).update(date=date,details=details,work_image=path)
        return HttpResponse("<script>alert('updated');window.location='/View_uploadworks'</script>")
    except:
        details = request.POST['textfield']
        date = request.POST['textfield1']
        work.objects.filter(id=id).update(date=date,details=details)
        return HttpResponse("<script>alert('updated');window.location='/View_uploadworks'</script>")

def  Viewpayment(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
    # t =Booking.objects.filter(id=id,paymentstatus='paid')
        t = Bookings.objects.filter(BOOKING_id=id,BOOKING__paymentstatus='paid')
        return render(request,"worker/View payment.html",{"data":t})


def Viewapprovedbookings(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        data = Bookings.objects.filter(status='approve',SERVICE__WORKER__LOGIN=request.session['lid'])
        return render(request,"worker/approvedbookings.html",{"data":data})

def view_profile(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        data=worker.objects.get(LOGIN=request.session['lid'])
        return render(request,'worker/view_profile.html',{'data':data})
def worker_view_payment(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        data=Bookings.objects.filter(SERVICE__WORKER__LOGIN__id = request.session['lid'])
        return render(request,"worker/view_payment.html",{"data":data})

def approve_booking(request,id):
    Bookings.objects.filter(id=id).update(status='approve')
    return HttpResponse("<script>alert('approved');window.location='/View_service'</script>")

def reject_booking(request,id):
    Bookings.objects.filter(id=id).update(status='reject')
    return HttpResponse("<script>alert('approved');window.location='/View_service'</script>")

def update_work_status(request,id):
   if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
   else:
       return render(request,'worker/update_status.html',{'id':id})

def update_work_status_post(request,id):
    selct = request.POST['select']
    Bookings.objects.filter(id=id).update(workerstatus=selct)
    return HttpResponse("<script>alert('updated');window.location='/Viewapprovedbookings'</script>")

def chatt(request,u):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        request.session['head']="CHAT"
        request.session['uid'] = u
        return render(request,'worker/chat.html',{'u':u})


def chatsnd(request,u):
        d=datetime.datetime.now().strftime("%Y-%m-%d")
        # t=datetime.datetime.now().strftime("%H:%M:%S")
        c = request.session['lid']
        b=request.POST['n']
        print(b)
        print(u,"userrrrrrrrrr")
        m=request.POST['m']
        cc = worker.objects.get(LOGIN__id=c)
        uu = user.objects.get(id=request.session['uid'])
        obj=chat()
        obj.date=d
        obj.type='worker'
        obj.WORKER=cc
        obj.USER=uu
        obj.chat=m
        obj.save()
        print(obj)
        v = {}
        if int(obj) > 0:
            v["status"] = "ok"
        else:
            v["status"] = "error"
        r = JsonResponse.encode(v)
        return r
    # else:
    #     return redirect('/')

def chatrply(request):
    c = request.session['lid']
    cc=worker.objects.get(LOGIN=request.session['lid'])
    uu=user.objects.get(id=request.session['uid'])
    res = chat.objects.filter(WORKER=cc,USER=uu)
    print(res)
    v = []
    if len(res) > 0:
        print(len(res))
        for i in res:
            v.append({
                'type':i.type,
                'chat':i.chat,
                'nam':i.USER.username,
                # 'upic':i.USER.photo,
                'dtime':i.date,
                'tname':i.WORKER.name,
            })
        # print(v)
        return JsonResponse({"status": "ok", "data": v, "id": cc.id})
    else:
        return JsonResponse({"status": "error"})

# ===============================================================================================================
def user_home(request):
    return render(request,'user/user_index.html')
def user_register(request):
    return render(request,"user/user_register.html")

def user_register_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    email = request.POST['textfield5']
    contact = request.POST['textfield6']
    password = request.POST['textfield7']

    lob = login.objects.filter(username=email)
    if lob.exists():
        return HttpResponse("<script>alert('Already Exist');window.location='/user_register'</script>")
    else:
        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.usertype = 'user'
        log_obj.save()

        user_obj = user()
        user_obj.username = name
        user_obj.place = place
        user_obj.post = post
        user_obj.pincode = pin
        user_obj.email = email
        user_obj.phone = contact
        user_obj.LOGIN = log_obj
        # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        # s.starttls()
        # s.login("smartfuddonation@gmail.com", "smart@789")
        # msg = MIMEMultipart()  # create a message.........."
        # msg['From'] = "smartfuddonation@gmail.com"
        # msg['To'] = email
        # msg['Subject'] = "Your Password is"
        # body = "Your Password is:- - " + str(password)
        # msg.attach(MIMEText(body, 'plain'))
        # s.send_message(msg)
        user_obj.save()
        return HttpResponse("<script>alert('Registered Successfully');window.location='/user_register'</script>")
def user_view_profile(request):
    data=user.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/view_profile.html',{'data':data})
def user_view_category(request):
    data=category.objects.all()
    # data = Category.objects.filter(id=wid)
    return render(request,"user/view_categories.html",{"data":data})



def user_view_service(request,id):
    data = service.objects.filter(CATEGORY=id)
    return render(request,"user/view_services.html",{"data":data,"id":id})

def user_view_worker(request,id):
    data=service.objects.filter(id=id)
    return render(request,'user/view_workers.html',{'data':data})

def user_booking_map(request,id):
    return render(request,"user/booking_map.html",{"id":id})

def user_send_request(request,id):
    la = request.POST['textfield9']
    lo = request.POST['textfield10']
    obj=service.objects.get(id=id)
    booking_obj = Bookings()
    booking_obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    booking_obj.amount = obj.amount
    booking_obj.lattitude = la
    booking_obj.longitude = lo
    booking_obj.status = 'pending'
    booking_obj.payment_status = 'pending'
    booking_obj.workerstatus = 'pending'
    booking_obj.USER = user.objects.get(LOGIN=request.session['lid'])
    booking_obj.SERVICE_id =obj.id
    booking_obj.save()
    return HttpResponse("<script>alert('Request sended');window.location ='/user_view_category'</script>")
    # return render(request,"user/booking_map.html")

def user_view_request(request):
    data = Bookings.objects.filter(USER=user.objects.get(LOGIN=request.session['lid']),status='approve')
    return render(request,"user/view_request.html",{"data":data})

def user_view_booking(request):
    data = Bookings.objects.filter(USER=user.objects.get(LOGIN=request.session['lid']), status='pending')
    return render(request, "user/view_booking.html", {"data": data})

def user_view_bill(request,id):
    data = Bookings.objects.filter(id=id, payment_status__in=["online", "offline"])
    return render(request,"user/view_bill.html",{"data":data})

def user_add_rating(request,rid):
    return render(request,"user/rate.html",{"rid":rid})

def user_add_rate_post(request,rid):
    rate = request.POST['star']
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    review = request.POST['textarea']
    rate_obj = rating()
    rate_obj.rating = rate
    rate_obj.date = date
    rate_obj.review = review
    rate_obj.BOOKINGS= Bookings.objects.get(id=rid)
    rate_obj.USER = user.objects.get(LOGIN_id=request.session['lid'])
    rate_obj.save()
    return HttpResponse("<script>alert('Rate added');window.location='/user_view_request'</script>")

def user_view_service_worker(request,id):
    data=service.objects.filter(id=id)
    return render(request,'user/view_service_workers.html',{'data':data})


def user_chat(request, u):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logout');window.location='/'</script>")
    else:
        request.session['head'] = "CHAT"
        request.session['uid'] = u
        return render(request, 'user/chat.html', {'u': u})

def user_chatsnd(request, u):
    d = datetime.datetime.now().strftime("%Y-%m-%d")
    # t=datetime.datetime.now().strftime("%H:%M:%S")
    c = request.session['lid']
    b = request.POST['n']
    print(b)
    print(u, "userrrrrrrrrr")
    m = request.POST['m']
    cc = user.objects.get(LOGIN__id=c)
    uu = worker.objects.get(id=request.session['uid'])
    obj = chat()
    obj.date = d
    obj.type = 'user'
    obj.USER = cc
    obj.WORKER = uu
    obj.chat = m
    obj.save()
    print(obj)
    v = {}
    if int(obj) > 0:
        v["status"] = "ok"
    else:
        v["status"] = "error"
        r = JsonResponse.encode(v)
        return r
        # else:
        #     return redirect('/')

def user_chatrply(request):
        # if request.session['log']=="lo":
    c = request.session['lid']
    cc = user.objects.get(LOGIN=request.session['lid'])
    uu = worker.objects.get(id=request.session['uid'])
    res = chat.objects.filter(USER=cc, WORKER=uu)
    v = []
    if len(res) > 0:
        print(len(res))
        for i in res:
            v.append({
                'type': i.type,
                'chat': i.chat,
                'nam': i.WORKER.name,
                # 'upic':i.USER.photo,
                'dtime': i.date,
                'tname': i.USER.username,
            })
        print(v)
        return JsonResponse({"status": "ok", "data": v, "id": cc.id})
    else:
        return JsonResponse({"status": "error"})

def user_view_uploads(request,id):
    data=work.objects.filter(WORKER=id)
    return render(request,'user/View upload works.html',{'data':data})




            # def user_view_rating(request,rid):
    #     data = rating.objects.filter(BOOKINGS__SERVICE__WORKER = Worker.objects.get(LOGIN=request.session['lid']))
    #     lis=[]
    #     for i in data:
    #         rt=[]
    #         nrt=[]
    #         for j in range(int(i.rate)):
    #             rt.append(j)
    #         for j in range(5-int(i.rate)):
    #             nrt.append(j)
    #             dict = {'name': i.BOOKINGS.USER.name, 'date': i.date, 'rate': rt, 'norate': nrt, 'review': i.review}
    #         lis.append(dict)
    #     return render(request,"User/view_rate.html",{"data":lis,"rid":rid})
    #
    # def user_view_credit_point(request):            # Credit Point View
    #     data = Credit_point.objects.filter(LOGIN = Login.objects.get(id=request.session['lid']))
    #     return render(request,"user/view_credit_point.html",{"data":data})
    #
    # def list_worker_chat(request):
    #     data = Worker.objects.all()
    #     return render(request,"user/chat_with_worker.html",{"data":data})
    #
    # def user_chat_worker(request,i):
    #     data = Chat.objects.filter(USER=User.objects.get(LOGIN=request.session['lid']))
    #     data1=Chat.objects.filter(WORKER=Worker.objects.get(id=i))
    #     print(data1)
    #     return render(request,"user/chat.html",{"i":i,"data":data,"data":data1})
    #
    # def user_chat_worker_post(request,i):
    #     chat = request.POST['textfield']
    #     date = datetime.datetime.now().strftime("%Y-%m-%d")
    #     chat_obj = Chat()
    #     chat_obj.chat = chat
    #     chat_obj.date = date
    #     chat_obj.type = 'user'
    #     chat_obj.USER = User.objects.get(LOGIN=request.session['lid'])
    #     chat_obj.WORKER = Worker.objects.get(id=i)
    #     chat_obj.save()
    #     return HttpResponse("<script>alert('Chat send');window.location='/user_chat_worker/"+i+"'</script>")
    #
def user_send_complaint(request):
    return render(request,"user/send_complaint.html")

def user_send_complaint_post(request):
    complaint = request.POST['textarea']
    complaint_date = datetime.datetime.now().strftime("%Y-%m-%d")
    complaint_obj=Complaint()
    complaint_obj.complaint = complaint
    complaint_obj.complaint_date = complaint_date
    complaint_obj.reply = 'pending'
    complaint_obj.reply_date = '0000-00-00'
    complaint_obj.USER = user.objects.get(LOGIN=request.session['lid'])
    complaint_obj.save()
    return HttpResponse("<script>alert('complaint send');window.location='/user_send_complaint'</script>")

def user_view_reply(request):
    data = Complaint.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,"User/view_reply.html",{"data":data})
    #
    # def user_change_password(request):
    #     return render(request,"user/change_password.html")
    #
    # def user_change_password_post(request):
    #     old_password = request.POST['textfield2']
    #     new_password = request.POST['textfield3']
    #     confirm_password = request.POST['textfield3']
    #
    #     Login.objects.get(password=old_password,id=request.session['lid'])
    #
    #     if new_password == confirm_password:
    #         if Login.objects.filter(password=new_password).exists():
    #             return HttpResponse("<script>alert('Password already exist');window.location='/user_change_password'</script>")
    #         else:
    #             Login.objects.filter(id=request.session['lid']).update(password=confirm_password)
    #             return HttpResponse("<script>alert('password updated');window.location='/user_change_password'</script>")
    #     else:
    #         return HttpResponse("<script>alert('password mismatch');window.location='/user_change_password'</script>")
    #
    #     # return redirect('/admin_change_password')
    #
    # # Worker Bank Management
    #
    # def worker_add_bank(request):
    #     return render(request,"worker/worker_bank.html")
    #
    # def worker_add_bank_post(request):
    #     bank_name = request.POST['textfield']
    #     account_no = request.POST['textfield2']
    #     IFSC_code = request.POST['textfield3']
    #
    #
    #     amount = random.randint(500,100000)             # To add random values for amount
    #     data = Bank.objects.filter(LOGIN=Login.objects.get(id=request.session['lid']))
    #     if data.exists():
    #         return HttpResponse("<script>alert('Could not add Bank');window.location='/worker_view_bank#aa'</script>")
    #     else:
    #
    #         bank_obj = Bank()
    #         bank_obj.bank_name = bank_name
    #         bank_obj.account_no = account_no
    #         bank_obj.IFSC_code = IFSC_code
    #         bank_obj.amount = amount
    #         bank_obj.LOGIN = Login.objects.get(id=request.session['lid'])
    #         bank_obj.save()
    #         return HttpResponse("<script>alert('Bank details added');window.location='/worker_add_bank#aa'</script>")
    #
    # def worker_view_bank(request):
    #     data = Bank.objects.filter(LOGIN=Login.objects.get(id=request.session['lid']))
    #     return render(request,"worker/view_bank.html",{"data":data})
    #
    # def worker_delete_bank(request,bid):
    #     Bank.objects.get(id=bid).delete()
    #     return HttpResponse("<script>alert('Bank details removed');window.location='/worker_view_bank#aa'</script>")
    #
    # # User Bank Management
    #
    # def user_add_bank(request):
    #     return render(request,"user/bank.html")
    #
    # def user_add_bank_post(request):
    #     bank_name = request.POST['textfield']
    #     account_no = request.POST['textfield2']
    #     IFSC_code = request.POST['textfield3']
    #     # amount = ''
    #
    #     amount = random.randint(500,100000)             # To add random values for amount
    #     bank_obj = Bank()
    #     bank_obj.bank_name = bank_name
    #     bank_obj.account_no = account_no
    #     bank_obj.IFSC_code = IFSC_code
    #     bank_obj.amount = amount
    #     bank_obj.LOGIN = Login.objects.get(id=request.session['lid'])
    #     bank_obj.save()
    #     return HttpResponse("<script>alert('Bank details added');window.location='/user_add_bank#aa'</script>")
    #
    # def user_view_bank(request):
    #     data = Bank.objects.filter(LOGIN=Login.objects.get(id=request.session['lid']))
    #     return render(request,"user/view_bank.html",{"data":data})
    #
    # def user_delete_bank(request,bid):
    #     Bank.objects.get(id=bid).delete()
    #     return HttpResponse("<script>alert('User Bank details removed');window.location='/user_view_bank'</script>")
    #
def user_make_payment(request,rid):
    bobj = Bookings.objects.get(id=rid)
    request.session['orginalamount'] = bobj.amount
    request.session['requestid'] = rid
    return render(request,"user/payment.html",{"rid":rid})
    #
def user_make_payment_post(request,rid):
    payment = request.POST['RadioGroup1']
    bbb = Bookings.objects.filter(id=rid)

    if payment == 'Offline':
        bbb.update(payment_status='offline')
        return HttpResponse("<script>alert('payment process is offline');window.location='/user_view_request'</script>")
    else:

        import razorpay

        razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
        razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

        razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

        amount = float(bbb[0].amount)*100
        # amount = float(amount)

        # Create a Razorpay order (you need to implement this based on your logic)
        order_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': 'order_rcptid_11',
            'payment_capture': '1',  # Auto-capture payment
        }

        # Create an order
        order = razorpay_client.order.create(data=order_data)

        context = {
            'razorpay_api_key': razorpay_api_key,
            'amount': order_data['amount'],
            'currency': order_data['currency'],
            'order_id': order['id'],
            'rid': rid
        }

        return render(request, 'user/pay.html', context)

def payment_success(request, id):
    Bookings.objects.filter(id=id).update(payment_status="online")
    return redirect('user_view_request#hom')

    # def user_bank_details(request,rid,wid,amount):
    #     return render(request,"user/bank_details.html",{"rid":rid,"wid":wid,"amount":amount})
    #
    # def user_bank_details_post(request,rid,wid,amount):
    #     bank_name = request.POST['textfield']
    #     account_no = request.POST['textfield2']
    #     IFSC_code = request.POST['textfield3']
    #     amount = request.POST['textfield4']
    #     data = Bank.objects.filter(bank_name = bank_name,account_no = account_no,IFSC_code = IFSC_code,     # Checking the account already exist
    #                             LOGIN=request.session['lid'])
    #
    #     if data.exists():
    #         if int(data[0].amount)  >= int(amount):
    #             userbank = Bank.objects.filter(LOGIN = Login.objects.get(id=request.session['lid']))
    #             balance = int(userbank[0].amount) - int(amount)
    #             userbank = Bank.objects.filter(id = userbank[0].id)
    #             userbank.update(amount = balance)
    #             Bookings.objects.filter(id=rid).update(payment_status ='Online')
    #
    #             workerbank = Bank.objects.filter(LOGIN = Login.objects.get(id=wid))
    #             balance = int(workerbank[0].amount) + int(amount)
    #             workerbank.update(amount = balance)
    #
    #             if request.session['paymode'] == 'using credit point':
    #                 ucredit = Credit_point.objects.filter(LOGIN=Login.objects.get(id=request.session['lid']))
    #                 if ucredit.exists():
    #                     cr = int(ucredit[0].credit_point) - int(request.session['credit'])
    #                     ucredit.update(credit_point=cr)
    #
    #             if int(amount) >= 1000:
    #
    #                 ucredit = Credit_point.objects.filter(LOGIN = Login.objects.get(id=request.session['lid']))
    #                 if ucredit.exists():
    #                     cr = int(ucredit[0].credit_point) + 10
    #                     ucredit.update(credit_point = cr)
    #                 else:
    #
    #                     cobj = Credit_point()  # Adding Credit point
    #                     cobj.credit_point = 10
    #                     cobj.LOGIN = Login.objects.get(id=request.session['lid'])
    #                     cobj.save()
    #
    #                 bobj = Bookings.objects.get(id=rid)
    #                 wcredit = Credit_point.objects.filter(LOGIN=Login.objects.get(id=bobj.SERVICE.WORKER.LOGIN.id))
    #                 if wcredit.exists():
    #                     cr = int(wcredit[0].credit_point) + 10
    #                     wcredit.update(credit_point=cr)
    #                 else:
    #                     crobj = Credit_point()
    #                     crobj.credit_point = 10
    #                     crobj.LOGIN = Login.objects.get(id=bobj.SERVICE.WORKER.LOGIN.id)
    #                     crobj.save()
    #
    #                 return HttpResponse("<script>alert('Bank amount added');window.location='/user_view_request'</script>")
    #         else:
    #             return HttpResponse("<script>alert('Inefficient balance');window.location='/user_view_request'</script>")
    #     else:
    #         return HttpResponse("<script>alert('Does not have account');window.location='/user_view_request'</script>")
    # #
    # # def worker_view_credit_point(request):
    # #     data = Credit_point.objects.filter(LOGIN = Login.objects.get(id=request.session['lid']))
    # #     return render(request,"worker/view_credit_point.html",{"data":data})
    # #
    # # def worker_credit_convert(request,cid):                 # credit point conversion to account
    # #     credit_point = Credit_point.objects.filter(LOGIN = Login.objects.get(id=request.session['lid']))
    # #     workerbank = Bank.objects.filter(LOGIN = Login.objects.get(id=request.session['lid']))
    # #     balance = int(workerbank[0].amount) + int(credit_point[0].credit_point)
    # #     workerbank.update(amount = balance)
    # #     credit_point.update(credit_point = 0)
    # #
    # #     return HttpResponse("<script>alert('credit inserted to bank');window.location='/worker_view_credit_point/"+cid+"'</script>")
    # #
    # #
    # # def ajax_view_credit_points(request):
    # #     amt = request.session['orginalamount']
    # #     q = Credit_point.objects.filter(LOGIN = Login.objects.get(id=request.session['lid']))
    # #
    # #     if q.exists():
    # #         if int(q[0].credit_point)>0:
    # #             payable = q[0].credit_point  # credit point to amount conversion (10 points = 1rupee)
    # #             balance = int(amt) - int(payable)  # calculating balance amount
    # #             request.session['gtm'] = balance
    # #             request.session['credit'] = payable
    # #
    # #             return JsonResponse({"data": "ok", "credit": q[0].credit_point, "payable": payable, "balance": balance})
    # #         else:
    # #             return JsonResponse({"data": "no"})  # no credit points
    # #
    # #     else:
    # #         return JsonResponse({"data": "no"})  # no credit points
    #
    # def credit_payment_mode(request):
    #     rid = request.session['requestid']
    #     bobj = Bookings.objects.get(id=rid)
    #     request.session['paymode'] = 'using credit point'
    #     return redirect('/user_bank_details/' + rid + '/' + str(bobj.SERVICE.WORKER.LOGIN.id) + '/' + str(request.session['gtm']))

    # def logout(request):
#     request.session["lg"]=""
#     return redirect('/')