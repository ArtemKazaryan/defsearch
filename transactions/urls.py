"""
URL configuration for transactions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from transaction import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signup'),
    path('logout/', views.logoutuser, name='logout'),
    path('login/', views.loginuser, name='login'),

    # Transactions
    path('', views.home, name='home'),

    path('special_cost_calculations/', views.transactions_special_cost_calculations, name='special_cost_calculations'),
    path('specialcalculation1/', views.specialcostcalculation1, name='specialcalculation1'),
    # path('specialcalculation/<int:pk>', views.specialcostcalculation, name='specialcalculation'),

    path('specialcalculation2/', views.specialcostcalculation2, name='specialcalculation2'),
    path('specialcalculation3/', views.specialcostcalculation3, name='specialcalculation3'),
    path('specialcalculation4/', views.specialcostcalculation4, name='specialcalculation4'),
    path('specialcalculation5/', views.specialcostcalculation5, name='specialcalculation5'),

    path('recorded/', views.recordedtransactions, name='recorded'),
    path('createpro/', views.createprotransaction, name='createpro'),
    path('createexp/', views.createexptransaction, name='createexp'),

    path('protransaction/<int:protransaction_pk>/', views.viewprotransaction, name='viewprotransaction'),
    path('exptransaction/<int:exptransaction_pk>/', views.viewexptransaction, name='viewexptransaction'),
    path('protransaction/<int:protransaction_pk>/delete', views.deleteprotransaction, name='deletepro'),
    path('exptransaction/<int:exptransaction_pk>/delete', views.deleteexptransaction, name='deleteexp'),
]
