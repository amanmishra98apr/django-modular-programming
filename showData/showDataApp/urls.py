from django.urls import path
from .views import studentInfo 
from .views import branch 
from .views import year 
from django.conf.urls import url, include

urlpatterns = [

    path('hello/', studentInfo.showStdDetails),
    path('branch/', branch.showBranch),
    path('year/', year.showYear)
]
