"""TN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = {
    path('', views.first),

    path('complaintsend', views.complaintsend),
    # path('complaint', views.complaint),
    path('feedbacks', views.feedbacks),
    path('Categoryadd', views.Categoryadd),
    path('view_rating/<id>', views.view_rating),
    path('viewuser', views.viewuser),
    path('workers', views.workers),
    path('adminhome', views.adminhome),
    path('approvedworker', views.approvedworker),
    path('change', views.change),
    path('change_post', views.change_post),
    path('Viewcategory', views.Viewcategory),
    path('login_post', views.login_post),
    path('addcategory_POST', views.addcategory_POST),
    path('Approveworkers/<id>', views.Approveworkers),
    path('Rejectworkers/<id>', views.Rejectworkers),
    path('categorydelete/<id>',views.categorydelete),
    path('categoryupdate/<id>',views.categoryupdate),
    path('categoryupdate_post/<id>',views.categoryupdate_post),
    path('logout', views.logout),
    path('complaint_view',views.complaint_view),
    path('admin_send_reply/<id>',views.admin_send_reply),
    path('admin_send_reply_post/<id>',views.admin_send_reply_post),


##############################################################################################################


    path('add_service',views.add_service),
    path('add_service_post',views.add_service_post),
    path('register',views.register),
    path('view_profile',views.view_profile),
    path('register_post',views.register_post),
    path('View_bookings/<id>',views.View_bookings),
    path('View_category',views.View_category),
    # path('View_payment',views.View_payment),
    path('View_service',views.View_service),
    path('View_serviceupdate/<id>',views.View_serviceupdate),
    path('Upload_works',views.Upload_works),
    path('Upload_works_POST',views.Upload_works_POST),
    path('Upcoming_works',views.Upcoming_works),
    path('worker_home',views.worker_home),
    path('approve_booking/<id>',views.approve_booking),
    path('reject_booking/<id>',views.reject_booking),
    path('Approvebookings',views.Approvebookings),
    path('Rejectbookings',views.Rejectbookings),
    path('update_service_post/<id>',views.update_service_post),
    path('View_servicedelete/<id>',views.View_servicedelete),
    path('View_uploadworks',views.View_uploadworks),
    path('Delete_uploadworks/<id>',views.Delete_uploadworks),
    path('Update_uploadworks/<id>',views.Update_uploadworks),
    path('Update_uploadworksPOST/<id>',views.Update_uploadworksPOST),
    path('Viewpayment/<id>',views.Viewpayment),
    path('Viewapprovedbookings',views.Viewapprovedbookings),
    path('update_work_status/<id>',views.update_work_status),
    path('update_work_status_post/<id>',views.update_work_status_post),
    path('chatt/<u>',views.chatt),
    path('chatsnd/<u>',views.chatsnd),
    path('chatrply',views.chatrply),

# =============================User============================================================================
    path('user_register',views.user_register),
    path('user_home',views.user_home),
    path('user_register_post',views.user_register_post),
    path('user_view_profile',views.user_view_profile),
    path('user_view_category',views.user_view_category),
    path('user_view_service/<id>',views.user_view_service),
    path('user_view_worker/<id>',views.user_view_worker),
    path('user_booking_map/<id>',views.user_booking_map),
    path('user_send_request/<id>',views.user_send_request),
    path('user_view_request',views.user_view_request),
    path('user_view_bill/<id>',views.user_view_bill),
    path('user_add_rating/<rid>',views.user_add_rating),
    path('user_add_rate_post/<rid>',views.user_add_rate_post),
    path('user_view_service_worker/<id>',views.user_view_service_worker),
    path('user_chat/<u>',views.user_chat),
    path('user_chatsnd/<u>',views.user_chatsnd),
    path('user_chatrply',views.user_chatrply),
    path('user_make_payment/<rid>',views.user_make_payment),
    path('user_make_payment_post/<rid>',views.user_make_payment_post),
    path('payment_success/<id>', views.payment_success),
    path('user_send_complaint', views.user_send_complaint),
    path('user_send_complaint_post', views.user_send_complaint_post),
    path('user_view_reply', views.user_view_reply),
    path('user_view_uploads/<id>', views.user_view_uploads),
    path('user_view_booking', views.user_view_booking),



}